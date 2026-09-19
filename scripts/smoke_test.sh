#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:8000}"

check_endpoint() {
  local path="$1"
  local expected_key="$2"
  local response

  response="$(curl --fail --silent --show-error "${BASE_URL}${path}")"

  if [[ -n "$expected_key" ]] && ! grep -q '"'""$expected_key"'""' <<<"$response"; then
    printf 'Smoke test failed: %s response did not contain key %s\n' "$path" "$expected_key" >&2
    printf '%s\n' "$response" >&2
    exit 1
  fi

  printf 'PASS %s\n' "$path"
}

printf 'Running API smoke tests against %s\n' "$BASE_URL"
check_endpoint "/health" "status"
check_endpoint "/api/overview" ""
printf 'All smoke tests passed.\n'
