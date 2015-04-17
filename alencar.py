arq = open('pg29040.txt')
texto = arq.read()
texto = texto.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, ' ')
texto = texto.split()
 
dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
print ('Deus aparece %s vezes' %dic['deus'])
arq.close()
