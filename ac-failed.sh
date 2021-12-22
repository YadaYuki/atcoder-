#!/bin/sh

dir=$(dirname $(which $0))
poetry run python ${dir}/failed.py $(git symbolic-ref --short HEAD) $1