# coding:utf8
#
# Determine se um ano é bissexto. Verifique no Google como fazer isso...
# 
import os
os.system("clear") # Limpando a tela

bissexto = int(input("Digite o Ano com 4 digitos, ex: 1968 : "))
if bissexto % 400 == 0 or bissexto % 4 == 0:
	print ("Este ano é bissexto")
else:
	print ("Este ano NÃO é bissexto")
