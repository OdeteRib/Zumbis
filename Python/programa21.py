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
    temp = input("Digite o elemento a ser adicionado --> ")
    vetor.append(temp)
    i = i + 1
print ("Vetor eh   :    ",vetor)

print ("Na Ordem inversa [",end="")

i  = (len(vetor) - 1)
while i >= 0:
   print ((vetor[i]),end=" ")
   i = i - 1
print ("]")
