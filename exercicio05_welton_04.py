#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995
'''
import os
os.system("clear")

x = 0
for s in range(18644, 33087):
    sortudo = str(s)
    if '2' in sortudo and '7' not in sortudo:
        x += 1

print("Na faixa de números, entre 18644 e 33087, existem %d elementos" % (x))
