#coding:utf8
#
# implementa a função fatorial recursivamente
#
import os
os.system("clear")

def fat(n):
	if n < 0:
		return "Erro faturial de numero negativo não existe"
	elif n == 0:
		return 1
	else:
		return n * fat(n-1)
# fim da função
#
x = int(input("Digite o valor a ser calculado a fatorial --> "))
print ("Fatorial de ", x, " é ", fat(x))
