#!/bin/sh

poetry run python $AC_ROOT/shell/failed.py $(git symbolic-ref --short HEAD) $1