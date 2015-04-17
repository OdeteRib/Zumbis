# coding:utf8
#
# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e imprima com
# nome do mês por extenso
#
import os
os.system("clear") # Limpando a tela

mes_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9:'setembro', 10: 'outubro', 11: 'novembro', 12:'dezembro'}

aniver = input("Digite uma data de nascimento, no formato dd/mm/aaaaa : ")

dia, mes, ano = aniver.split("/")

print ('Mês de aniversário por extenso: %s' % (mes_ext[int(mes)]))
