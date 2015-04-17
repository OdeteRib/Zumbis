#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao 
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

import os
os.system("clear")

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    if senha == login:
      print("A senha não pode ser igual ao login")
      continue
    else:
      break
print ("A senha correta, você esta logado")
