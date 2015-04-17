'''
A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de 
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a 
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número 
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
'''
# coding:utf8
#
# serie de fibonacci recursiva
#
import os
os.system("clear")

def fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)
# fim da função

x = int(input("Digite o tamanho da série --> "))

print ("Série gerada : ", )

for i in range(1,x+1):
	print (fib(i), end=' ')
print ("\n")
# Fim do programa
