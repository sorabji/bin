#!/bin/sh

TESTS=${1:-"src/"}

./vendor/bin/phpunit  -c app/ $TESTS
