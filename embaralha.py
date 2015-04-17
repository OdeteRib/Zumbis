#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")

def embaralha (s):
    import random
    lista = list(s)
    random.shuffle(lista)
    return ''.join(lista)
a = input("Digite uma palavra: ")

w = embaralha(a)
print (w)
