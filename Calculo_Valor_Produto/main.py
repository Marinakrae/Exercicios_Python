'''Desenvolva um algoritmo que leia o valor a ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. Para realizar o cálculo, utilize os códigos a seguir referentes à condição de pagamento escolhida pelo cliente.
-Código Condição de pagamento;
-À vista em dinheiro ou cheque, recebe 10% de desconto.
-À vista no cartão de crédito, recebe 15% de desconto.
-Em duas vezes, preço normal de etiqueta mais juros de 10%.
'''

def calcula_preco(valor, cod):
    if cod == 1: #A.V dinheiro ou cheque
        valor = valor*0.9
    elif cod == 2:
        valor = valor*0.85
    elif cod == 3:
        valor = valor*1.1
    else:
        print("Código inválido.")
    print('O valor a ser pago é R$:%.2f'% valor)

if __name__ == '__main__':
    valor = float(input("Digite o preço de etiqueta do produto: "))
    cod = int(input("Digite o código da forma de pagamento (1 - A.V Dinheiro ou Cheque, 2 - A.V Cartão, 3 - Em 2x): "))
    calcula_preco(valor, cod)