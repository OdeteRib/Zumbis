# coding:utf8
#
# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e imprima com
# nome do mês por extenso
#
dia, mes, ano = input('Data (dd/mm/aaaa)>: ').split('/')

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print ('Voce nasceu em: ')
print ('%s de %s de %s' % (dia, meses[int(mes) - 1], ano))
