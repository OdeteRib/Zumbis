# -*- coding: UTF-8 -*-

"""
  Este exemplo mostra como pesquisar uma
  substring em uma string usando a função find.
  A assinatura desta função é:

  find(substring[, start[, end]])

  onde substring é a substring a ser pesquisa e
  start e end são argumentos opcionais que definem
  os índices de início e fim da pesquisa.

  Se a substring não for encontrada, o valor -1 é
  retornado. Se for encontrada, o índice do primeiro
  caractere é retornado.
"""

frase = "Gosto de Python e JavaScript"

indice = frase.find("Python")
if indice != -1:
  print ("A palavra foi encontrada no índice", indice)
else:
  print ("A palavra não foi encontrada")
