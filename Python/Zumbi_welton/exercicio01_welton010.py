# encoding:utf8
#
# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a 
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante 
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. 
# Exiba o total de dias.
#
import os
os.system("clear")

cigarros_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
idade_fuma = int(input("Digite há quantos anos você fuma: "))

death = ((cigarros_dia * 365) * idade_fuma) / 1440

print ("Você já perde %d dia(s) da sua vida" %(death))
