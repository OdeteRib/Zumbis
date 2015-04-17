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
# pesquisar Pares

i = 0

print ("Vetor Recebido        : ",vetor)
print ("Elemento pares        :  [",end="")
while i < len(vetor):
    if vetor[i] % 2 == 0:
        print (vetor[i], end=",")
    i = i + 1
print (end="]\n")
