# encoding:utf8
#
# Curso: Python para Zumbies - exercício 3
#
# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
# Calcule o total em segundos.
#
import os
os.system("clear") # Limpando a tela

dias = int(input("Digite a quantidade de dia(s): "))
horas = int(input("Digite a quantidade de hora(s) : "))
segundos = int(input("Digite a quantidade de segundo(s) : "))

total = ((dias * 86400) + (horas * 1440) + segundos)

print ("Calcule o total em segundos é de ", total)
