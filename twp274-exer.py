# coding:utf8
#
# Faça um Programa que leia um vetor de 10 caracteres
# minúsculos, e diga quantas consoantes foram lidas

import os
os.system("clear") # Limpando a tela

listastring = []
i = 1
contador = 0

while i <= 10:
	letras = input("Digite uma string: ")
	listastring.append(letras)
	i += 1
i = 0
while i <= 9:
	if listastring[i] not in 'aeiou':
		contador += 1
	i += 1
print ("Foi digitado, %d consoantes no vetor " % contador)

