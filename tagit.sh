#!/bin/bash

exec etags -h ".php" -R \
--exclude="\.git" \
--exclude="\.js" \
--totals=yes \
--tag-relative=yes \
--PHP-kinds=+cf
