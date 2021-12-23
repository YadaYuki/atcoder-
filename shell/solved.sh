#!/bin/sh
# NOTE: $1は小文字のアルファベット一文字。
git add $1.py # TODO: Python以外の言語にも対応する
git commit -m "Solved  "$(git symbolic-ref --short HEAD)" $1"
echo "You solved $1. Well Done \U1F601"