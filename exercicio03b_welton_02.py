#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu 
# algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando 
# os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que 
# nenhuma delas esteja em falta no caixa.

import os
os.system("clear")

preco = int(input("Digite o valor da compra: "))
dinheiro = int(input("Digite a quantia de dinheiro pago: "))

valor = dinheiro - preco

cedulas = 0
atual = 50
apagar = valor
while True:
	if atual <= apagar:
		apagar -= atual
		cedulas += 1
	else:
		print ("%d cédulas(s) de R$%d" %(cedulas, atual))
		if apagar == 0:
			break
		if atual == 50:
			atual = 20
		elif atual == 20:
			atual = 10
		elif atual == 10:
			atual = 5
		elif atual == 5:
			atual = 2
		elif atual == 2:
			atual = 1
		cedulas = 0
			
		
	
