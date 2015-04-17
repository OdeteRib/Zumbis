#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Questão B. Quantas vezes o trecho de pseudocódigo seguinte imprime 'oi'? (obs: na
nossa pseudo-linguagem, o laço inclui os extremos, ou seja, 1 até 4 significa 1, 2, 3, 4.)
para i = 1 até 9
se i != 3, então
para j = 1 até 6
imprime 'oi'

'''
import os
os.system("clear")

for i in range(0,9):
	if i != 3:
		for j in range(0,6):
			print ('oi', (i + j))
