# coding:utf8
#
# Curso: Python para Zumbies - exercício 1 - listas
#
import os
os.system("clear") # Limpando a tela

listas = [8,7,6,9,9]
contador = 0
media = 0
while contador < (len(listas)):
	media = media + listas[contador]
	contador = contador + 1
print (listas)
print ("Média iqual há: ", (media / 5))
