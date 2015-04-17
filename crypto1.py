#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")

statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

statement.lower()

frase_cortada = statement.split()

for frase_cortada in texto.readlines():
    for letra in frase_cortada:
        if letra in 'python':
            saida.write('*')
        else:
            saida.write(letra)
texto.close()
saida.close()
