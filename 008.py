#!/usr/bin/python3
# cording: utf-8

def cipher(target):
    '''文字列の暗号化、復号化
    以下の仕様で文字列を変換する
    ・英小文字ならば(219 - 文字コード)の文字に置換
    ・その他の文字はそのまま出力
    '''

    result = ''
    for c in target:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result

if __name__ == '__main__':

#   対象文字列の入力
    target = input('文字列を入力してください--> ')

#   暗号化
    encorded = cipher(target)
    print('暗号化:{}'.format(encorded))

#   復号化
    decorded = cipher(encorded)
    print('復号化:{}'.format(decorded))
