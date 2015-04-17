#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Seja o statement sobre diversidade: “The Python Software Foundation and the global Python 
# community welcome and encourage participation by everyone. Our community is based on 
# mutual respect, tolerance, and encouragement, and we are working to help each other live up 
# to these principles. We want our community to be more diverse: whoever you are, and 
# whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com 
# split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras 
# “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais 
# e cuidado com maiúsculas e minúsculas.

import os
os.system("clear")

texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

cont = 0
for p in texto:
    if len(p) > 4:
        for c in p:
            if c in "python":
                cont += 1
                break
