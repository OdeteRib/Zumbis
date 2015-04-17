#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")

import random

listas = []
limite_max = 15
limite_min = 0

while limite_min < limite_max:
    r = random.randint(10,100)
    if r not in listas:
        limite_min += 1
        listas.append(r)
listas.sort()
print (listas)
