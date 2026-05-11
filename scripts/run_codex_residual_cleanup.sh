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
batches=("$BATCH_DIR"/residual-[0-9][0-9].txt)
if [[ "${#batches[@]}" -eq 0 ]]; then
  echo "No residual cleanup batches found" >&2
  exit 1
fi

status_line() {
  local done_count fail_count running_count
  done_count=$(find "$DONE_DIR" -maxdepth 1 -name 'residual-[0-9][0-9].done' 2>/dev/null | wc -l | tr -d ' ')
  fail_count=$(find "$FAIL_DIR" -maxdepth 1 -name 'residual-[0-9][0-9].fail' 2>/dev/null | wc -l | tr -d ' ')
  running_count=$(jobs -rp | wc -l | tr -d ' ')
  echo "$(timestamp) residual status done=$done_count failed=$fail_count running=$running_count total=${#batches[@]}"
}

run_residual_batch() {
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

This is a residual cleanup pass after the main Korean translation.
Batch name: $batch_name
Batch list file: $rel_batch
Expected file count: $count
Completion marker to create: translation-batches/done/$batch_name.done

Task:
1. Read every Markdown file path listed in the residual batch list.
2. Translate only remaining English natural-language prose into natural Korean.
3. Include English prose inside Swift comments, Markdown image alt text, and short description lines.
4. Preserve existing Korean text; do not rewrite it just for style.
5. Keep technical terms in English according to the translation guide.
6. Preserve front matter, URLs, Markdown syntax, code identifiers, API symbols, string literals, CSV/JSON data examples, and platform availability lines exactly.
7. Do not edit files outside this residual batch list.
8. If you use a script, use python3 and UTF-8-safe file IO.
9. After cleanup, create the completion marker file with the batch name and processed file count.
10. Reply with exactly one line: batch $batch_name done: $count files
EOF
)"

  echo "$(timestamp) residual start $batch_name ($count files)"
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
      echo "$(timestamp) residual done $batch_name"
    else
      echo "$(timestamp) residual fail $batch_name (missing completion marker)" >&2
      echo "missing completion marker" > "$FAIL_DIR/$batch_name.fail"
      return 1
    fi
  else
    local exit_code=$?
    echo "$(timestamp) residual fail $batch_name (exit $exit_code)" >&2
    echo "exit $exit_code" > "$FAIL_DIR/$batch_name.fail"
    return "$exit_code"
  fi
}

rm -f "$DONE_DIR"/residual-[0-9][0-9].done "$FAIL_DIR"/residual-[0-9][0-9].fail
echo "$(timestamp) residual run start batches=${#batches[@]} max_parallel=$MAX_PARALLEL model=$MODEL reasoning=$REASONING"

for batch in "${batches[@]}"; do
  while [[ "$(jobs -rp | wc -l | tr -d ' ')" -ge "$MAX_PARALLEL" ]]; do
    status_line
    sleep 15
  done
  run_residual_batch "$batch" &
  sleep 2
done

while [[ "$(jobs -rp | wc -l | tr -d ' ')" -gt 0 ]]; do
  status_line
  sleep 15
done

wait || true
status_line

if compgen -G "$FAIL_DIR/residual-[0-9][0-9].fail" > /dev/null; then
  echo "$(timestamp) residual run completed with failures" >&2
  exit 1
fi

echo "$(timestamp) residual run completed successfully"
