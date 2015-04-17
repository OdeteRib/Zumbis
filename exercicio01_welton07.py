# encoding:utf8
#
# Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
#
import os
os.system("clear")

celsius = int(input("Digite a temperatura em Celsius -->: "))

fahrenheit = ((9 * celsius ) / 5) + 32

print ("A temperatura de %5.2f grau(s) Celsius, convertida para %5.2f Fahrenheit" %(celsius,fahrenheit))
