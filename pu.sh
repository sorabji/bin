#!/bin/sh

TESTS=${1:-"src/"}

./vendor/bin/phpunit --debug --coverage-html ./app/logs/report/ --testdox-html ./app/logs/testdox.html -c app/ $TESTS
