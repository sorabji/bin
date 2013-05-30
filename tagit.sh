#!/bin/bash

# exec ctags -h ".php" -R \
# --exclude="\.git" \
# --exclude="\.js" \
# --totals=yes \
# --tag-relative=yes \
# --PHP-kinds=+cf

# ctags -R .
# find . -name '*.php' -print | xargs etags
ctags -eR --langmap=php:+.module.install.inc.engine --languages=php
