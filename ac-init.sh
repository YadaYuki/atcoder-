#!/bin/sh

if git branch | grep $1; then
    echo "$1 already exist 😏"
    git checkout $1
else
    echo "$1 does not exist 😋"
    git checkout -b $1
fi
mkdir $1
git commit --allow-empty -m "Start $1 Contest"
gh pr create --base master --title "$1 Contest" --body "Let's Solve $1 Contest!"
code $1
