# coding:utf8
#
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule 
# e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
# quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os 
# descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$
#
import os
os.system("clear") # Limpando a tela

salario_bruto = float(input("Digite o valor da hora tralhada  : "))
horas_mes = float(input("Digite o valor das horas trabalhadas no mês: "))

cal_salario = salario_bruto * horas_mes
imposto = (cal_salario * 0.11)
inss = (cal_salario * 0.08)
sindicato = (cal_salario * 0.05)
salario_liguido = cal_salario - (imposto + inss + sindicato)

print ("\n --------- Comprovante de Pagamento ------------------\n")
print ("+ Salário Bruto  -------------->: R$ %8.2f" % (cal_salario))
print ("- IR - (11%%) -------------------: R$ %8.2f" % (imposto))
print ("- INSS (8%%) --------------------: R$ %8.2f" % (inss))
print ("- Sindicato (5%%) ---------------: R$ %8.2f" % (sindicato))
print ("= Salário Liquido --------------: R$ %8.2f" % (salario_liguido))
