#!/usr/bim/python3
# cording:utf-8

import os
import subprocess
import xml.etree.ElementTree as ET

fname = "unlimited.txt"
fname_parsed = "unlimited.txt.xml"

def tokenization():
    if os.path.exists(fname_parsed):
        return
    subprocess.run('java -cp "/home/masaharu/.local/lib/stanford-corenlp-full-2013-06-20/*"\
                    edu.stanford.nlp.pipeline.StanfordCoreNLP -file '+fname, shell=True)

def read_xml():
    root = ET.parse(fname_parsed)
    for element in root.iter('token'):
        word = element.findtext('word')
        lemma = element.findtext('lemma')
        pos = element.findtext('POS')
        print("{}\t{}\t{}".format(word,lemma,pos))

if __name__ == '__main__':
    tokenization()
    read_xml()
