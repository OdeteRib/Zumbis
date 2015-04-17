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
# Declara a variável Soma
soma = 0

# Reincia o i
i = 0

# Laço para somar os elementos do vetor
while i < len(vetor):
    soma = soma + vetor[i]
    i = i + 1

# Declara a variável Média

media = float (soma)/len(vetor)

# Imprime o resultado

print ("Vetor dado     :    ",vetor)
print ("Média dos elementos ",media)

