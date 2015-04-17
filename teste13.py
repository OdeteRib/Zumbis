L = [1, 2, 3, 4]

for x in range(0,len(L)):
    for y in range(0,len(L)):
        if (int(L[x]) + (int(L[y]))) == 5:
            print ("Soma Possível")
            break
        else:
            print ("Soma Impossível")
            
