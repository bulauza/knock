#!/usr/bim/python3
# cording:utf-8

import MeCab
import os

fname = 'neko.txt'
fname_parsed = 'neko.txt.mecab'

def parse_neko():
    with open(fname) as f, open(fname_parsed, 'w') as outf:
        tagger = MeCab.Tagger()
        outf.write(tagger.parse(f.read()))
    
def read_parsed():
    with open(fname_parsed, 'r') as f:
        morphemes = []
        for line in f:
            line = line.split('\t',1)

            if len(line) < 2:
                continue

            morpheme_list = line[1].split(',')

            if line[0] =='一' or morpheme_list[1] =='空白':
                continue

            morpheme = {
                    "surface": line[0],
                    "base": morpheme_list[6],
                    "pos": morpheme_list[0],
                    "pos1": morpheme_list[1]
            }
            morphemes.append(morpheme)

            if morpheme_list[1] =='句点':
                yield morphemes
                morphemes = []

if __name__ == '__main__':
    # .mecab がないときに生成
    if not os.path.isfile(fname_parsed):
        parse_neko()

    morpheme = []
    for result in read_parsed():
        for line in result:
            if line['pos'] == '名詞' and line['pos1'] == 'サ変接続':
                morpheme.append(line['base'])
    tmp = list(set(morpheme))
    tmp.sort()
    print(tmp)
