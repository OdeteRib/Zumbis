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
# pesquisar linear
m = int(input("Digite o numero a ser procurado no Vetor --> "))
i = 0
posicao = -1
while i < len(vetor):
    if m == vetor[i]:
       posicao = i 
    i = i + 1
print ("Vetor Recebido        : ",vetor)
print ("Elemento procurado    : ",m)
if posicao == -1:
    print ("Elemento não encontrado")
else:
    print ("Elemento encontrado na posição",posicao) 
