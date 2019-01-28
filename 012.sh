#!/bin/bash
# cording:utf-8

cut -f 1 hightemp.txt > test1.txt
diff -s  col1.txt test1.txt
