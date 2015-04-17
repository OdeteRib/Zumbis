#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
# seja inválido e continue pedindo até que o usuário informe um valor válido

import os
os.system("clear")

while True:
    nota = int(input("Digite um valor para nota, entre 0 e 10: "))
        
    if 0 >= nota or nota >= 10:
      print("Nota errada, digite valor entre 0 e 10, por favor")
      continue
    else:
      break
print ("Nota valida")

