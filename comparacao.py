# -*- coding: UTF-8 -*-

"""
  Este exemplo mostra como ordenar uma lista
  de strings baseado no tamanho de cada uma
"""

# define a função a ser usada na comparação
def comparar(x,y):
	if len(x) > len(y):
		return 1
	elif len(x) == len(y):
		return 0
	else:
		return -1

# cria uma lista de nomes
nomes = ['Carlos', 'Igor', 'Osmar', 'Fernanda']

# exibe a lista na ordem original
print (nomes)

# ordena a lista
nomes.sort(comparar)

# exibe a lista ordenada
print (nomes)
