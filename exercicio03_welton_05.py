#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando 
# o algoritmo de Euclides. 
#
import os
os.system("clear")

def gcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b

a = int(input("Digite o primeiro número para calculo do MDC --> "))
b = int(input("Digite o segundo número para calculo do MDC ---> "))

print ("Portanto, o máximo divisor comum dos inteiros %d e %d é" %(a, b), (gcd(a,b)))
