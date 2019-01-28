#!/usr/bim/python3
# cording:utf-8
import gzip
import json

fname='jawiki-country.json.gz'

def extract_UK():

    with gzip.open(fname, 'rt') as f1:

        for line in f1:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

if __name__ == '__main__':
    import re
    target = extract_UK()
    target = target.split('\n')

    target_Category = [contents for contents in target if "Category" in contents]
    [print(line) for line in target_Category]
