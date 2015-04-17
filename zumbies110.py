# encoding:utf8
#
# Curso: Python para Zumbies - exercício 2
#
import os
os.system("clear") # Limpando a tela

tarifa = 0
preco = int(input("Digite o valor em minutos, para calculo da conta mensal --> "))
if preco >= 800:
	tarifa = preco * 1.08
elif preco >= 400 or preco < 800:
	tarifa = preco * 1.15
elif preco >= 200 or preco < 400:
	tarifa = preco * 1.18
else:
	if preco < 200:
		tarifa = preco * 1.20
print ("Tarifa para este mês é de %6.2f" %tarifa)	
