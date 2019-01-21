#!/usr/bim/python3
# cording:utf-8

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechan"

s = s.replace(',', '')
words = s.split()

count=[]

for word in words:
    count.append(len(word))
result = count.sort()
print(count)
