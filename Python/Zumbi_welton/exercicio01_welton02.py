# encoding:utf8
#
# Curso: Python para Zumbies - exercício 2
#
# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
#
import os
os.system("clear") # Limpando a tela

numero1 = float(input("Digite um valor em metros: "))
convmili = (numero1 * 1000)
print ("O Valor de %5.2f metro(s) convertido em milimetro(s) fica em: %d mm" %(numero1,convmili))
