'''Faça um programa para ler diversos valores para duas variáveis inteiras até que a primeira seja menor que a segunda. '''

if __name__ == '__main__':

    while True:
        n1 = int(input("Digite um valor para n1: "))
        n2 = int(input("Digite um valor para n2: "))
        if n1 < n2:
            break

    print("n1 é menor do que n2.")

