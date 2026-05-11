#!/usr/bin/env bash
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BATCH_DIR="$ROOT/translation-batches"
PROMPT_FILE="$BATCH_DIR/TRANSLATION_PROMPT.md"
LOG_DIR="$BATCH_DIR/logs"
DONE_DIR="$BATCH_DIR/done"
FAIL_DIR="$BATCH_DIR/fail"

MAX_PARALLEL="${MAX_PARALLEL:-4}"
MODEL="${CODEX_TRANSLATION_MODEL:-gpt-5.4}"
REASONING="${CODEX_TRANSLATION_REASONING:-low}"

mkdir -p "$LOG_DIR" "$DONE_DIR" "$FAIL_DIR"

if [[ "${RESET_MARKERS:-0}" == "1" ]]; then
  rm -f "$DONE_DIR"/batch-[0-9][0-9].done "$FAIL_DIR"/batch-[0-9][0-9].fail
fi

if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "Missing prompt file: $PROMPT_FILE" >&2
  exit 1
fi

shopt -s nullglob
batches=("$BATCH_DIR"/batch-[0-9][0-9].txt)
if [[ "${#batches[@]}" -eq 0 ]]; then
  echo "No batch files found in $BATCH_DIR" >&2
  exit 1
fi

timestamp() {
  date '+%Y-%m-%dT%H:%M:%S%z'
}

status_line() {
  local done_count fail_count running_count total_count
  done_count=$(find "$DONE_DIR" -maxdepth 1 -name 'batch-[0-9][0-9].done' 2>/dev/null | wc -l | tr -d ' ')
  fail_count=$(find "$FAIL_DIR" -maxdepth 1 -name 'batch-[0-9][0-9].fail' 2>/dev/null | wc -l | tr -d ' ')
  running_count=$(jobs -rp | wc -l | tr -d ' ')
  total_count="${#batches[@]}"
  echo "$(timestamp) status done=$done_count failed=$fail_count running=$running_count total=$total_count"
}

run_batch() {
  local batch_file="$1"
  local batch_name count rel_batch rel_prompt marker log_file
  batch_name="$(basename "$batch_file" .txt)"
  count="$(wc -l < "$batch_file" | tr -d ' ')"
  rel_batch="${batch_file#$ROOT/}"
  rel_prompt="${PROMPT_FILE#$ROOT/}"
  marker="$DONE_DIR/$batch_name.done"
  log_file="$LOG_DIR/$batch_name.log"

  if [[ -f "$marker" ]]; then
    echo "$(timestamp) skip $batch_name ($count files, marker exists)"
    return 0
  fi

  rm -f "$FAIL_DIR/$batch_name.fail"

  local prompt
  prompt="$(cat <<EOF
Use the translation guide at $rel_prompt.

Batch name: $batch_name
Batch list file: $rel_batch
Expected file count: $count
Completion marker to create: translation-batches/done/$batch_name.done

Task:
1. Read the translation guide.
2. Read every Markdown file path listed in the batch list file.
3. Translate each listed Markdown file in place into natural Korean.
4. Preserve technical terms in English according to the guide.
5. Preserve front matter, URLs, Markdown syntax, code, API symbols, and platform availability lines exactly.
6. Do not edit files outside the batch list.
7. After all listed files are translated, create the completion marker file with the batch name and translated file count.
8. Reply with exactly one line: batch $batch_name done: $count files
EOF
)"

  echo "$(timestamp) start $batch_name ($count files)"
  if codex exec \
    -C "$ROOT" \
    --sandbox danger-full-access \
    --dangerously-bypass-approvals-and-sandbox \
    --ephemeral \
    --ignore-rules \
    -m "$MODEL" \
    -c "model_reasoning_effort=\"$REASONING\"" \
    "$prompt" > "$log_file" 2>&1 < /dev/null; then
    if [[ -f "$marker" ]]; then
      echo "$(timestamp) done $batch_name"
    else
      echo "$(timestamp) fail $batch_name (missing completion marker)" >&2
      echo "missing completion marker" > "$FAIL_DIR/$batch_name.fail"
      return 1
    fi
  else
    local exit_code=$?
    echo "$(timestamp) fail $batch_name (exit $exit_code)" >&2
    echo "exit $exit_code" > "$FAIL_DIR/$batch_name.fail"
    return "$exit_code"
  fi
}

echo "$(timestamp) translation run start batches=${#batches[@]} max_parallel=$MAX_PARALLEL model=$MODEL reasoning=$REASONING"

for batch in "${batches[@]}"; do
  while [[ "$(jobs -rp | wc -l | tr -d ' ')" -ge "$MAX_PARALLEL" ]]; do
    status_line
    sleep 20
  done
  run_batch "$batch" &
  sleep 2
done

while [[ "$(jobs -rp | wc -l | tr -d ' ')" -gt 0 ]]; do
  status_line
  sleep 20
done

wait || true
status_line

if compgen -G "$FAIL_DIR/batch-[0-9][0-9].fail" > /dev/null; then
  echo "$(timestamp) translation run completed with failures" >&2
  exit 1
fi

echo "$(timestamp) translation run completed successfully"
