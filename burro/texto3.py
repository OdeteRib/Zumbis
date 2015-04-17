# coding:utf8
#
# Faça um Programa que leia um vetor de 10 caracteres
# minúsculos, e diga quantas consoantes foram lidas

import os
os.system("clear") # Limpando a tela

palavra = "pythonicos"
k = 0
troca = []

while k < len(palavra):
	if palavra == palavra[k].startswith(tuple('python')):
		troca.append(palavra[k])
	else:
		print ("Não sei")
	k += 1
print (troca)
