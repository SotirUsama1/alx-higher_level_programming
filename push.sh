#!/bin/bash
echo 'commit: '
read x
git add ${PWD}
git commit -m ${x}
git push