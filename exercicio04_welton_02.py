#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os 
# números ímpares na lista IMPAR. Imprima as três listas.

import os
os.system("clear") # Limpando a tela

import random

lista = []
lista_par = []
lista_impar = []

while len(lista) < 20:
    x = random.randint(1,100)
    if x not in lista:
       lista.append(x)

lista.sort()

for x in range (0,20):
	if lista[x] % 2 == 0:
		lista_par.append(lista[x])
	else:
		lista_impar.append(lista[x])

print ("A lista gerada com 20 elementos é: ", (lista))
print ("A lista com",len(lista_par),"numeros pares é: ", (lista_par))
print ("A lista com",len(lista_impar),"numeros impares é: ",(lista_impar))
