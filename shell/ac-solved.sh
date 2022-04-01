#!/bin/sh
# NOTE: $1は小文字のアルファベット一文字。
CONTEST_NAME=$(git symbolic-ref --short HEAD)
"$AC_ROOT"/.venv/bin/python $AC_ROOT/shell/solved.py $CONTEST_NAME $1
git add $AC_ROOT/$CONTEST_NAME/* $AC_ROOT/csv/solved.csv 
git commit -m "Solved  $CONTEST_NAME $1"
echo "You solved $1. Well Done 👍"