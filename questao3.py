# -*- coding: utf8 -*-                                                       
peso = input('Peso do peixe: ')
 
def calculo_multa(excesso,valor_multa):
     valor_multa = 4.0
     excesso = peso - 50
     multa = excesso * 4.0
     return multa
 
# excesso = peso - 50

if excesso <= 0:
	print ("Não há multa. Quantidade do excesso = %f e multa = %f" %(excesso))
else peso > 50:
	calculo_multa()
print ("Multa no valor %5.2f e excesso %5.2f" %(multa,excesso))
