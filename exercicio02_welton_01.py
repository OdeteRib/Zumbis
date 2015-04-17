# coding:utf8
#
# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser 
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

import os
os.system("clear") # Limpando a tela

a = int(input("Digite o valor para o lado --> a: "))
b = int(input("Digite o valor para o lado --> b: "))
c = int(input("Digite o valor para o lado --> c: "))

if a == b and a == c and b == c:
	print ("Este triângulo é equilátero")
elif a != b and a != c and b != c:
	print ("Este triângulo é escaleno")
else:
	print ("Este triângulo é isósceles")	
