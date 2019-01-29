#!/usr/bim/python3
# cording:utf-8

import re

fname = "nlp.txt"

def nlp_lines():
    with open(fname) as f:
        
        r = re.compile(r"^.*?[\.|;|:|\?|!] [A-Z].*", re.DOTALL)

        for line in f:
            line = r.findall(line)            
            print(line)

if __name__ == '__main__':
    nlp_lines()
