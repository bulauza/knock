#!/usr/bim/python3
# cording:utf-8

from pprint import pprint
import json
import corenlp

fname = "nlp.txt"

def tokenization():
    corenlp_dir = "/home/masaharu/.local/lib/stanford-corenlp-full-2013-06-20/"
    parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)
    
    result = parser.parse("I am the born of my sword")
    json_text = json.loads(result)
    pprint(json_text)

if __name__ == '__main__':
    tokenization()
