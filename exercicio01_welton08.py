# encoding:utf8
#
# Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
#
import os
os.system("clear")

fahrenheit = int(input("Digite a temperatura em Fahrenheit -->: "))

celsius = (( fahrenheit - 32) / 9) * 5

print ("A temperatura de %5.2f grau(s) Fahrenheit, convertida para %5.2f grau(s) celsius " %(fahrenheit,celsius))
