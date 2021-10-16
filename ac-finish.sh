#!/bin/sh
# NOTE: $1は小文字のアルファベット一文字。
git push
gh pr merge
echo ""$(git symbolic-ref --short HEAD)" Finished. Good Work \U1F619"
CONTEST_BRANCH=$(git symbolic-ref --short HEAD)
git checkout master
git branch --delete CONTEST_BRANCH
