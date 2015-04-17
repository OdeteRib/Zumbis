# encoding:utf8
#
# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o 
# preço a pagar.
#
import os
os.system("clear")

mercadoria = float(input("Digite o valor da Mercadoria--------->: "))
percentil = float(input("Digite o valor em porcetagem do Desconto: "))

registradora = ((mercadoria * percentil) / 100)
novopreco = mercadoria - registradora

print ("O valor do desconto é de: %5.2f, o preço a pagar é de: %5.2f" %(registradora,novopreco))
