#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu 
# algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando 
# os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que 
# nenhuma delas esteja em falta no caixa.
#
import os
os.system("clear")

custo = float(input("Valor total dos produtos: "))
recebido = float(input("Valor recebido: "))

cedulas = [50.00, 20.00, 10.00, 5.00, 2.00, 1.00]
s = []
soma = 0
i = 1
n = 1
if i <= len(cedulas) and soma != n:
	if s + cedulas[i] <= n:
		s = s.append[i]
		soma =+ cedulas[i]
	else:
		i =+ 1
print (s)
