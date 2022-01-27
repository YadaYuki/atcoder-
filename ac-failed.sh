#!/bin/sh

dir=$(dirname $(which $0))
poetry run python $AC_ROOT/shell/failed.py $(git symbolic-ref --short HEAD) $1