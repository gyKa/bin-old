#!/bin/sh

find ~/Downloads/* -mtime +5 -exec rm -rf {} \;

# Explanation:
#
# find: the unix command for finding files / directories / links etc.
# ~/Downloads/*: the directory to start your search in.
# -mtime +5: specify the number of days old that the file is.
# -exec ... \;: for each such result found, do the following command in ...
# rm -rf {}: recursively force remove the directory; the {} part is where the find result gets substituted into from the previous part.
