#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa 
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de 
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento

'''
import os
os.system("clear")

city_a = int(input("Digite o valor da população de A: "))
taxa_a = float(input("Digite o valor da taxa de cresimento da população de A: "))

city_b = int(input("Digite o valor da população de B: "))
taxa_b = float(input("Digite o valor da taxa de cresimento da população de B: "))

os.system("clear")

anos = 0

while True:
	if city_a < city_b:
		city_a = (city_a * (taxa_a/100)) + city_a
		city_b = (city_b * (taxa_b/100)) + city_b
		anos += 1
	else:
		break

print("A população do país A: %.0f" % city_a)
print("A população do país B: %.0f" % city_b)
print("\nApós %i anos o país A, ultrapasará o país B em número de habitantes." % anos)
