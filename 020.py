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
    print(extract_UK())
