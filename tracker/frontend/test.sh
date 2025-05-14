#!/usr/bin/env bash
# save this as set-standalone.sh, make it executable (chmod +x), then run in your project root

CONFIG_FILE="next.config.ts"  # or next.config.js

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "❌ $CONFIG_FILE not found."
  exit 1
fi

# Determine sed’s in-place flag for macOS vs Linux
if [[ "$(uname)" == "Darwin" ]]; then
  SED_INPLACE=(-i "")
else
  SED_INPLACE=(-i)
fi

# do the replacement without backups
sed "${SED_INPLACE[@]}" -E \
  's@(^[[:space:]]*output:[[:space:]]*)(["'"'"'])[[:alnum:]]+\2@\1"standalone"@' \
  "$CONFIG_FILE"

echo "✅ Updated $CONFIG_FILE to output: \"standalone\""
