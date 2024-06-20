#!/bin/bash

# Check if the first argument is empty
if [ -z "$1" ]; then
    echo 'commit: '
    read x
else
    x=$1
fi

# Add current directory to git
git add "${PWD}"

# Commit with the message
git commit -m "${x}"

# Push the commit
git push
