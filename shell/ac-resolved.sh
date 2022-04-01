# #!/bin/sh

CONTEST_NAME=$(git symbolic-ref --short HEAD)
"$AC_ROOT"/.venv/bin/python $AC_ROOT/shell/resolve.py $CONTEST_NAME $1
git add $AC_ROOT/$CONTEST_NAME/* $AC_ROOT/csv/failed.csv # 
git commit -m "Resolved $CONTEST_NAME $1"
echo "You solved $1. Well Done \U1F601"