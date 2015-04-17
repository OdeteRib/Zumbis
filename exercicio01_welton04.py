# encoding:utf8
#
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor 
# do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
#
import os
os.system("clear")

salario = float(input("Digite o valor do Salário ------------>: "))
percentil = float(input("Digite o valor em porcetagem do Aumento: "))

aumento = ((salario * percentil) / 100)
novosalario = salario + aumento


print ("O valor do aumento é de: %5.2f, o salário com aumento é de: %5.2f" %(aumento,novosalario))
