#coding: utf8
#
#
import os
os.system("clear")
vetor = []
n = int(input("Digite a quantidade de elementos a ser adicionada --> "))
i = 0
maior = 0
menor = 0
while i < n:
    temp = int(input("Digite o elemento a ser adicionado --> "))
    vetor.append(temp)
    i = i + 1
# Criar vetor Numeros Pares

i = 0

vetor_par = []

print ("Vetor Recebido        : ",vetor)

while i < len(vetor):
    if vetor[i] % 2 == 0:
        vetor_par.append(vetor[i])
    i = i + 1

print ("Vetor somente pares   :  [",vetor_par)
