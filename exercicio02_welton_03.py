# coding:utf8
#
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de 
# seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do 
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você 
# faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na 
# variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais 
# variáveis com o conteúdo ZERO.

import os
os.system("clear") # Limpando a tela

variavel_excesso = 0
variavel_multa = 0

peso_de_peixes = int(input("Digite o peso dos peixes de hoje: "))
if peso_de_peixes > 50:
	variavel_excesso = ((peso_de_peixes - 50) * 4)
	variavel_multa = variavel_excesso
print (variavel_multa)
print (variavel_excesso)
