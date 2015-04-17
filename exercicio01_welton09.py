# encoding:utf8
#
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo 
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

import os
os.system("clear")

por_dia = 60
por_kms = 0.15
 
km_per = float(input("Digite a quantidade de km(s) percorridos -------------->: "))
dias_alug = float(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))

cal_dias = dias_alug * por_dia
cal_kilometragem = km_per * por_kms

print ("O preço a pagar é de: %5.2f reais" %(cal_dias + cal_kilometragem))
