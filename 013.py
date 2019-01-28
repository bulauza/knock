#!/usr/bim/python3
# cording:utf-8

if __name__ == '__main__':
    with open("col1.txt", "r") as f1,\
        open("col2.txt", "r") as f2,\
        open("013_out.txt", "w") as f3:

        for line1, line2 in zip(f1,f2):
            line1 = line1.replace('\n','')
            line2 = line2.replace('\n','')
            concat = line1+'\t'+line2+'\n'
            f3.write(concat)
