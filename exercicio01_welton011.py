# encoding:utf8
#
# Sabendo que str( ) converte valores numéricos para string, calcule 
# quantos dígitos há em 2 elevado a um milhão.
import os
os.system("clear")
number = int(2**1000000)
digitos = len(str(number))
print ("Há %d digitos em 2 elevado a um milhão." % (digitos))
