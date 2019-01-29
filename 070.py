#!/usr/bim/python3
# cording:utf-8

import codecs
import random

if __name__ == '__main__':

    fname_pos = "rt-polaritydata/rt-polarity.pos"
    fname_neg = "rt-polaritydata/rt-polarity.neg"
    fname_smt = "sentiment.txt"
    fencoding = "cp1252"

    result = []

    with codecs.open(fname_pos, 'r', fencoding) as f_pos:
        for i_pos,line in enumerate(f_pos):
            result.append("+1 {}\n".format(line.strip()))

    with codecs.open(fname_neg, 'r', fencoding) as f_neg:
        for i_neg,line in enumerate(f_neg):
            result.append("-1 {}\n".format(line.strip()))

    random.shuffle(result)

    with open(fname_smt, 'w') as f_out:
        for line in result:
#            print(line)
            f_out.write(line)

    print("pos: {}, neg: {}".format(i_pos+1, i_neg+1))
