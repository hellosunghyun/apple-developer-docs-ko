#!/usr/bin/env bash
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BATCH_DIR="$ROOT/translation-batches"
PROMPT_FILE="$BATCH_DIR/TRANSLATION_PROMPT.md"
LOG_DIR="$BATCH_DIR/logs"
DONE_DIR="$BATCH_DIR/done"
FAIL_DIR="$BATCH_DIR/fail"

MAX_PARALLEL="${MAX_PARALLEL:-3}"
MODEL="${CODEX_TRANSLATION_MODEL:-gpt-5.4}"
REASONING="${CODEX_TRANSLATION_REASONING:-low}"

mkdir -p "$LOG_DIR" "$DONE_DIR" "$FAIL_DIR"

timestamp() {
  date '+%Y-%m-%dT%H:%M:%S%z'
}

shopt -s nullglob
batches=("$BATCH_DIR"/retry-31-[0-9][0-9].txt)
if [[ "${#batches[@]}" -eq 0 ]]; then
  echo "No retry batches found" >&2
  exit 1
fi

status_line() {
  local done_count fail_count running_count
  done_count=$(find "$DONE_DIR" -maxdepth 1 -name 'retry-31-[0-9][0-9].done' 2>/dev/null | wc -l | tr -d ' ')
  fail_count=$(find "$FAIL_DIR" -maxdepth 1 -name 'retry-31-[0-9][0-9].fail' 2>/dev/null | wc -l | tr -d ' ')
  running_count=$(jobs -rp | wc -l | tr -d ' ')
  echo "$(timestamp) retry status done=$done_count failed=$fail_count running=$running_count total=${#batches[@]}"
}

run_retry_batch() {
  local batch_file="$1"
  local batch_name count rel_batch rel_prompt marker log_file
  batch_name="$(basename "$batch_file" .txt)"
  count="$(wc -l < "$batch_file" | tr -d ' ')"
  rel_batch="${batch_file#$ROOT/}"
  rel_prompt="${PROMPT_FILE#$ROOT/}"
  marker="$DONE_DIR/$batch_name.done"
  log_file="$LOG_DIR/$batch_name.log"

  rm -f "$marker" "$FAIL_DIR/$batch_name.fail"

  local prompt
  prompt="$(cat <<EOF
Use the translation guide at $rel_prompt.

This is a retry for original batch-31, split into smaller chunks.
Batch name: $batch_name
Batch list file: $rel_batch
Expected file count: $count
Completion marker to create: translation-batches/done/$batch_name.done

Task:
1. Read the translation guide.
2. Read every Markdown file path listed in the retry batch list.
3. Translate each listed Markdown file in place into natural Korean.
4. If a file is already partly Korean, preserve the Korean and translate remaining English prose.
5. Preserve technical terms in English according to the guide.
6. Preserve front matter, URLs, Markdown syntax, code, API symbols, and platform availability lines exactly.
7. Do not edit files outside this retry batch list.
8. If you use a script, use python3 and UTF-8-safe file IO.
9. Verify at least one edited file no longer has its main description in English.
10. Create the completion marker file with the batch name and translated file count.
11. Reply with exactly one line: batch $batch_name done: $count files
EOF
)"

  echo "$(timestamp) retry start $batch_name ($count files)"
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
      echo "$(timestamp) retry done $batch_name"
    else
      echo "$(timestamp) retry fail $batch_name (missing completion marker)" >&2
      echo "missing completion marker" > "$FAIL_DIR/$batch_name.fail"
      return 1
    fi
  else
    local exit_code=$?
    echo "$(timestamp) retry fail $batch_name (exit $exit_code)" >&2
    echo "exit $exit_code" > "$FAIL_DIR/$batch_name.fail"
    return "$exit_code"
  fi
}

rm -f "$DONE_DIR"/retry-31-[0-9][0-9].done "$FAIL_DIR"/retry-31-[0-9][0-9].fail
echo "$(timestamp) retry run start batches=${#batches[@]} max_parallel=$MAX_PARALLEL model=$MODEL reasoning=$REASONING"

for batch in "${batches[@]}"; do
  while [[ "$(jobs -rp | wc -l | tr -d ' ')" -ge "$MAX_PARALLEL" ]]; do
    status_line
    sleep 15
  done
  run_retry_batch "$batch" &
  sleep 2
done

while [[ "$(jobs -rp | wc -l | tr -d ' ')" -gt 0 ]]; do
  status_line
  sleep 15
done

wait || true
status_line

if compgen -G "$FAIL_DIR/retry-31-[0-9][0-9].fail" > /dev/null; then
  echo "$(timestamp) retry run completed with failures" >&2
  exit 1
fi

rm -f "$FAIL_DIR/batch-31.fail"
printf 'batch-31\n29\n' > "$DONE_DIR/batch-31.done"
echo "$(timestamp) retry run completed successfully"
