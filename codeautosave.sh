#!/bin/bash

time=$(date -u +"%Y-%m-%d %H:%M:%S")

if [[ -n $(git status -s) ]]; then
    git add -A
    git commit -m "[AutoSave] Saved on $time"
    git push origin
    echo "Commit and push with message: [AutoSave] Saved on $time"
else
    echo "No changes to commit."
fi