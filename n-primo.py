#!/usr/bin/python3
#Verifica se é um número primo (primo= é unicamente divisivel por 1 e por ele próprio)
while True:
	try:
		np = int(input("Entre com um número inteiro: " ))	
		for x in range(2, np+1):
			x2 = np/x
			if x2.is_integer() == True and np != x:
				print(np,"não é número primo, tente novamente!")
				break
			elif x2.is_integer() == True and np == x:
				print(np,"é número primo!!!")
	except KeyboardInterrupt:
		print()
		exit(0)
	except ValueError:
		print("Valor digitado incorreto")
		pass
