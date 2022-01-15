#!/bin/sh

if git branch | grep $1; then
    echo "$1 already exist 😏"
    exit 0
else
    echo "$1 does not exist 😋"
    git checkout -b $1
fi

ac_root=../$(dirname $(which $0))

mkdir $AC_ROOT/$1
git commit --allow-empty -m "Start $1 Contest"
gh pr create --base master --title "$1 Contest" --body "Let's Solve $1 Contest!"
code $AC_ROOT/$1
