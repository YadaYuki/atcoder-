# #!/bin/sh

CONTEST_NAME=$(git symbolic-ref --short HEAD)
poetry run python $AC_ROOT/shell/resolve.py $CONTEST_NAME $1
git add $AC_ROOT/$CONTEST_NAME/$1.py $AC_ROOT/failed.csv # 
git commit -m "Resolved $CONTEST_NAME $1"
echo "You solved $1. Well Done \U1F601"