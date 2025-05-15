#!/bin/bash

# Prompt for commit message
echo "Enter commit message:"
read commit_msg

# Run Git add, commit, and push
git add .
git commit -m "$commit_msg"
git push
