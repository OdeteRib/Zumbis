# Problem Set "Estrutura de Repeticao"
# Fonte: http://www.python.org.br/wiki/EstruturaDeRepeticao 
# Exercicio 37
# Name: Diego Tostes
# Time: 4'30"
 
print("Lojas Tabajara")
 
fim = 1
while fim !=0:
    soma = 0
    i = 1
    valor = float(input("digite o valor do produto ou 0 para finalizar ---> "))
    while valor > 0:
        soma = soma + valor
        print ("Produto ",i,": R$ ", float(valor))
        i = i + 1
        valor = float(input("digite o valor do produto ou 0 para finalizar ---> "))
 
    if soma > 0:
        print ("Total --> R$", soma)
        formaPagamento = input("Forma de pagamento - digite 1 para cheque ou 2 para dinheiro ---> ")
        if formaPagamento == 2:
            qtyDinheiro = input("Informe o valor pago ---> ")
            troco = qtyDinheiro - soma
        else:
            troco = 0
        print ("troco de R$", troco)
        troco = 0
    fim = input("digite 0 para sair ou 1 para continuar -> ")
