#!/bin/sh
poetry run python $AC_ROOT/shell/failed.py $(git symbolic-ref --short HEAD) $1
git add $AC_ROOT/$CONTEST_NAME/$1.py $AC_ROOT/failed.csv
git commit -m "Failed to solve $CONTEST_NAME $1 😢"