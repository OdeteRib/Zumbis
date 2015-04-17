arquivo = open('números.txt','r')
for linha in arquivo.readlines():
    print (linha,end="")
arquivo.close()
