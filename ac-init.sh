#!/bin/sh
mkdir $1
git checkout -b $1
git commit --allow-empty -m "Start $1 Contest"
gh pr create --base master --title "$1 Contest" --body "Let's Solve $1 Contest!"
code $1
