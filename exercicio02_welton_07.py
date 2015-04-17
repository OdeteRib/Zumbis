# coding:utf8
#
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
# compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
#
import os
os.system("clear") # Limpando a tela

metros_quadrados = float(input("Digite o valor em metros quadrados da área a ser pintada: "))

if metros_quadrados % 54 != 0:
	lata_tinta = int(metros_quadrados / 54) + 1
else:
	lata_tinta = (metros_quadrados / 54)

valor_tinta = lata_tinta * 80

print ("Para pintar sua área de%8.2f metros quadrados" %(metros_quadrados))

print ("Você vai precisar de %d lata(s) de tinta ao preço de R$%8.2f" %(lata_tinta,valor_tinta))
