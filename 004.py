#!/usr/bim/python3
# cording:utf-8

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

num_use_farst = (1, 5, 6, 7, 8, 9, 15, 16, 19)
s = s.replace('.', '')
words = s.split()

result = {}
for i, word in enumerate(words):
    if i in num_use_farst:
        result[word[0:1]] = i
    else:
        result[word[0:2]] = i
print(result)
