#!/usr/bim/python3
# cording:utf-8

def n_gram(target, n):
    result = []

    for i in range(len(target)-n+1):
        result.append(target[i:i+n])
        
    return result

if __name__ == '__main__':

    target = "I am an NLPer"
    word_target = target.split()
    result = n_gram(target, 2)
    result = n_gram(word_target, 2)
    print(result)
