#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um 
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
# intercalados dos dois outros vetores. Imprima os três vetores.
#
import os
os.system("clear") # Limpando a tela

import random

lista = []
lista_x = []
lista_y = []

while len(lista_x) < 10:
    x = random.randint(1,100)
    if x not in lista_x:
       lista_x.append(x)
       
while len(lista_y) < 10:
    y = random.randint(1,100)
    if x not in lista_y:
       lista_y.append(y)

print ("Lista x: ",lista_x)
print ("\n")
print ("Lista y: ",lista_y)
print ("\n")

i = 0
j = 0
k = 0

# Executa a intercalação dos dois vetores recebidos

while i < len(lista_x)+len(lista_y):
    if j < len(lista_x):
        lista.append(lista_x[j])
        i = i + 1
        j = j + 1
    if k < len(lista_y):
        lista.append(lista_y[k])
        i = i + 1
        k = k + 1

print ("Lista intercalada: ", lista)
