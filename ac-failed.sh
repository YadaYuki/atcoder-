#!/bin/sh

dir=$(dirname $(which $0))
"$AC_ROOT"/.venv/bin/python $AC_ROOT/shell/failed.py $(git symbolic-ref --short HEAD) $1