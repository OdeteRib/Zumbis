#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Verifique se um inteiro positivo n é primo.
#
import os
os.system("clear")

entrada = int(input("Digite um numero positivo real qualquer: "));

i = 1;
j = 0;

entrada1 = (entrada/2);
 
while (i <= entrada):
 
   if (entrada % i==0):
      print ("É divisivel por %i"%i);
      i = i+1;
      j = j+1;
 
   if (i>=entrada1):
      i = entrada;
      print ("É divisivel por %i"%i);
      i = i+1;
      j = j+1;
 
   else:
      i = i+1;
if(j == 2):
   print ("O número digitado é primo!");
 
else:
   print ("Numero não é primo, possui %d divisores." %(j))
