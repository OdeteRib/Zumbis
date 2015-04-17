def squirrel_play(temp, is_summer):
  if is_summer:
	  return 60 <= temp <= 100
  return 60 <= temp <= 90

temp = int(input("Digite temperatura: "))
squirrel_play(temp, 70)

print (temp)
print (is_summer)	
