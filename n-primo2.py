primos = []
max = 1000000
min = 100000
for np in range(min,max):
	#np = int(input("Entre com um número inteiro: " ))
	for x in range(2, np+1):
		x2 = np/x
		if x2.is_integer() == True and np != x:
			#print(np,"não é número primo, tente novamente!")
			break
		elif x2.is_integer() == True and np == x:
			#print(np,"é número primo!!!")
			primos.append(np)
print (primos)
print ("Há %d números primos de 0 a %d" %(len(primos),max))
