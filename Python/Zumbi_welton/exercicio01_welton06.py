# encoding:utf8
#
# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer
# e a velocidade média esperada para a viagem
#
import os
os.system("clear")

distancia = float(input("Qual a distância a ser percorrida ---------->: "))
veloc_media = float(input("Qual velocidade média esperada para a viagem ->: "))

tempo = distancia / veloc_media

print ("O tempo de uma viagem de carro é de", tempo)
