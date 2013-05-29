#!/bin/bash

BRANCH=${1:-"dev"}

git checkout master && git pull origin master && git checkout $BRANCH && git rebase master
