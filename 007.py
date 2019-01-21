#!/usr/bim/python3
# cording:utf-8

def generate_str(x, y, z):
    print("{}時の{}は{}".format(x,y,z))

if __name__ == '__main__':
    x = 12
    y = "気温"
    z = 22.4

    generate_str(x, y, z)
