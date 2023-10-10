# coding=utf-8

def encode(n):
    s = str(n)
    l = len(s)
    ls = str(l)
    ll = len(ls)
    return "0" * (2 - ll) + ls + s

def decode(s):
    return int(s[2:])

s = encode(123456)
print s, decode(s)
