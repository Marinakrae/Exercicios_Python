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