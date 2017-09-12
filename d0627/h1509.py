#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hi, %s, you have $%d.' % ('Michael', 1000000))
def fact(n):
    if n == 1 :
        return 1 ;
    return n * fact(n - 1)

n =  fact(100)
print(n)