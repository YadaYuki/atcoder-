#!/bin/sh
# NOTE: $1は小文字のアルファベット一文字。
gh pr merge
echo ""$(git symbolic-ref --short HEAD)" Finished. Good Work \U1F619"