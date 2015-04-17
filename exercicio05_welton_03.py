#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
# divisíveis por 7? Resposta: 183

import os
os.system("clear")

pares = []

for x in range(1067,3628):
	if x % 2 == 0 and x % 7 == 0:
		pares.append(x)
		
		
print ("Lista de numeros pares e multiplos de  entre 1067-3627\n \n", (pares))
print ("\nA lista tem %d elementos" % len(pares))
