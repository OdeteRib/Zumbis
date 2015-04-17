#coding: utf8
#
#
import os
os.system("clear")
vetor = []
n = int(input("Digite a quantidade de elementos a ser adicionada --> "))
i = 0

while i < n:
    temp = int(input("Digite o elemento a ser adicionado --> "))
    vetor.append(temp)
    i = i + 1
# Laço de seleção do menor e do maior
maior = vetor[0]
menor = vetor[0]
i = 0

while i < len(vetor):
    if vetor[i] < menor:
        menor = vetor[i]
    if vetor[i] > maior:
        maior = vetor[i]
    i = i + 1

# Imprime o resultado
print ("Vetor dado    : ", vetor)
print ("Menor valor   : ", menor)
print ("Maior valor   : ", maior)
