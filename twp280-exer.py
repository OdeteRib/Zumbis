# coding:utf8
#
# Faça um Programa que leia um vetor de 10 caracteres
# minúsculos, e diga quantas consoantes foram lidas

import os
os.system("clear") # Limpando a tela

palavra = input("Palavra: ")
k = 0
troca = ""

while k < len(palavra):
	if palavra[k] in "aeiou":
		troca = troca + "*"
	else:
		troca = troca + palavra[k]
	k += 1
print ("Nova palavra %s" %troca)

