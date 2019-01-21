#!/usr/bim/python3
# cording:utf-8

def n_gram(target, n):
    result = []

    for i in range(len(target)-n+1):
        result.append(target[i:i+n])
        
    return result

if __name__ == '__main__':

    target1 = "paraparaparadise"
    target2 = "paragraph"
    
    unionX = set(n_gram(target1, 2))
    unionY = set(n_gram(target2, 2))
    
    print("X:{}".format(unionX))
    print("Y:{}".format(unionY))

#   和集合
    cup = unionX.union(unionY)
    print("X ∪ Y:{}".format(cup))

#   積集合
    cap = unionX.intersection(unionY)
    print("X ∩ Y:{}".format(cup))

#   差集合
    dif = unionX.difference(unionY)
    print("X差集合Y:{}".format(dif))

    target = 'se'
    if target in cup:
        print('Yes')
    else:
        print('No')
