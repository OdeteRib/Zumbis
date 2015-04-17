# organizar_alfabeticamente.py - 20.07.2004
# por Luiz E. Lepchak Jr. <jr.lepchak@ig.com,br>

# Declaração da função
def organizar_alfabeticamente(lista):
	"Organiza alfabeticamente as strings contidas dentro de uma lista."
	for x in range (len(lista)):
		for y in range (len(lista)):
			if lista[x] < lista[y]:
				lista[x], lista[y] = lista[y], lista[x]

# Exemplo da aplicação
lista = ["linux", "google", "kde, kdf"]
print ("Antes:", lista)
organizar_alfabeticamente(lista)
print ("Depois:", lista)
