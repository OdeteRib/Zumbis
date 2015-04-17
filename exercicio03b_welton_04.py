#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Dado um número inteiro positivo, determine a sua decomposição em fatores primos 
# calculando também a multiplicidade de cada fator.

import os
import itertools

os.system("clear")

def factor(n):
	for f in itertools.product(range(1,n), repeat=n):
		if reduce(lambda x,y: x*y, f) == n:
			return filter(lambda x: x>1, list(f))
		return [n]

for i in range(1,10):
	print (factor(i))
