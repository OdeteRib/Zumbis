# coding:utf8
#
# Faça um Programa que leia três números e mostre o maior deles.
#
import os
os.system("clear") # Limpando a tela

a = int(input("Digite o valor para o lado --> a: "))
b = int(input("Digite o valor para o lado --> b: "))
c = int(input("Digite o valor para o lado --> c: "))

if a > b:
	print ("O maior número é", a)
elif b > c:
	print ("O maior número é", b)
else:
	print ("O maior número é", c)
