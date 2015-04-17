#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Dizemos que um número natural é triangular se ele é produto de três números naturais 
# consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, 
# verificar se n é triangular.

import os
os.system("clear")

n = int(input("Determina se um número n é triangular. Digite o valor de n: "))
i = 0

while i * (i + 1) * (i + 2) < n:
	i = i + 1

if i * (i + 1) * (i + 2) == n:
	print("%d é triangular, pois, e produto %d * %d * %d " %(n,i,(i + 1),(i + 2)))
else:
	print("%d não é triangular" %(n))
	
