#!/usr/bin/python
# -*- coding: utf-8 -*-
 
mes_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio'}
aniver = input("Digite uma data, no formato dd/mm/aa : ")
dia, mes, ano = aniver.split("/")
print ('Data nascimento: %s' % (mes_ext[int(mes)]))
