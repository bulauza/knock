#!/usr/bin/python3
# cording:utf-8

with open("hightemp.txt", "r") as f,\
        open("col1.txt", "w") as f1,\
        open("col2.txt", "w") as f2:

    for line in f:
        line = line.split()
        f1.write(line[0]+'\n')
        f2.write(line[1]+'\n')
