#!/bin/sh
# NOTE: $1は小文字のアルファベット一文字。
CONTEST_NAME=$(git symbolic-ref --short HEAD)
git add $AC_ROOT/$CONTEST_NAME/$1.py # TODO: Python以外の言語にも対応する
git commit -m "Solved  $CONTEST_NAME $1"
echo "You solved $1. Well Done 👍"