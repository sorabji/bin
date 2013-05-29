#!/bin/bash

TARGET=${1:-"src/"}

scp -r $TARGET herb@192.168.11.5:home/herb/public_html/getitfree
