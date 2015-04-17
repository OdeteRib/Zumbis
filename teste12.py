lista = ['1', '1', '2', '4', '3', '4']
unico = []
[unico.append(item) for item in lista if item not in unico]
print (unico)
