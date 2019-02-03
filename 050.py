#!/usr/bim/python3
# cording:utf-8

import re

fname = "nlp.txt"

def nlp_lines():
    '''
    入力：ファイルから1行ずつ
    出力：区切られた文
    '''
    with open(fname) as f:
        
        r = re.compile(r"(.*?[\.|;|:|\?|!]) +([A-Z].*)", re.MULTILINE + re.DOTALL)

        for line in f:
            while len(line) > 0:
                result = r.match(line)
                if not result:  # ピリオドなしで改行とか
                    yield(line.strip())
                    break
                
                sentens = result.group(1).strip()
                if len(sentens)>0:
                    line = result.group(2).strip()
                    yield(sentens)
                else:
                    yield line
                    line = ''


if __name__ == '__main__':
    for result in nlp_lines():
        print(result)

