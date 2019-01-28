#!/bin/bash
# cording:utf-8

echo -n "N="
read N

count=$(cat hightemp.txt | wc -l)
div=$((count/N))
