arquivo = open('mensagem.txt')
saida = open('cripto.txt', 'w')
for linha in arquivo.readlines():
    for letra in linha:
        if letra in 'aeiou':
            saida.write('*')
        else:
            saida.write(letra)
arquivo.close()
saida.close()
