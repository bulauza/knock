#!/usr/bim/python3
# cording:utf-8

import sys

stop_words = ('a,about').lower().split(',')

def is_stopword(word):
    return word.lower() in stop_words

if __name__ == '__main__':

    args = sys.argv
    word = args[1]
    print(is_stopword(word))
