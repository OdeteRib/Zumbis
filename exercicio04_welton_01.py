#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, 
# sem usar as funções max e min.

import os
os.system("clear") # Limpando a tela

import random

lista = []

while len(lista) < 10:
    x = random.randint(1,100)
    if x not in lista:
       lista.append(x)

lista.sort()

print ("A lista sorteada é:\n",(lista))

print ("\nO menor número da lista é", lista[0])
print ("O maior número da lista é", lista[9])

