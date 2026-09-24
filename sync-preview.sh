#!/bin/bash
SRC="/Users/mysense/Desktop/MAXRENTAL v2/"
DST="/private/tmp/claude-501/-Users-mysense-Desktop/1bf20122-d1ba-4c8a-8037-69b2fb1154f2/scratchpad/mr2-preview/"
mkdir -p "$DST"
rsync -a --delete --exclude 'reference/' --exclude '__pycache__/' --exclude 'reference-stills/' "$SRC" "$DST"
echo "synced -> $DST"
