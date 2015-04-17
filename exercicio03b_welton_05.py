#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321

cdu = int(input("Digite um número qualquer de 4 unidades: "))
milhar = cdu%100//100
centena = cdu%100//100
dezena = (cdu%100)//10
unidade = cdu%10
udc = unidade*1000 + dezena*100 + centena*10 + milhar
print("O valor invertido eh ", udc)
