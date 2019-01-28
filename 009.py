#!/usr/bin/python3
# cording:utf-8

import random

def Typoglycemia(target):
    result = []
    target = target.replace('.','')
    words = target.split(' ')

    for word in words:
        if len(word) <= 4:
            result.append(word)
        else:
            tmp_str = list(word[1:-1])
            random.shuffle(tmp_str)
            result.append(word[0] + ''.join(tmp_str) + word[-1])
    return ' '.join(result)

if __name__ == '__main__':
    target = """
             I am the bone of my sword.
             Steel is my body, and fire is my blood.
             I have created over a thousand blades.
             Unknown to Death.
             Nor known to Life.
             Have withstood pain to create many weapons.
             Yet, those hands will never hold anything.
             So as I play, I call forth Unlimited Blade Works.
             """

    result = Typoglycemia(target)
   print(result)
