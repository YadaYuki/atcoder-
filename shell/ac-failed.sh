#!/bin/sh
"$AC_ROOT"/.venv/bin/python $AC_ROOT/shell/failed.py $(git symbolic-ref --short HEAD) $1
git add $AC_ROOT/$CONTEST_NAME/* $AC_ROOT/csv/failed.csv
git commit -m "Failed to solve $CONTEST_NAME $1 😢"