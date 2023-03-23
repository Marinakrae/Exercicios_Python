'''Faça uma função que verifique se um valor é perfeito ou não.
Um valor é dito perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio.
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores).
A função deve retornar 1, caso o número seja perfeito ou 0, caso não seja.'''


def verifica_perfeicao(num):

    soma_divs = 0

    for i in range(1, num):
        if num % i == 0:
            soma_divs = soma_divs + i


    if num == soma_divs:
        return 1
    else:
        return 0

if __name__ == '__main__':

    num = (int(input("Digite um número e diremos se ele é perfeito: ")))

    if verifica_perfeicao(num) == 1:
        print('Ele eh pfto *u*')
    else:
        print('Ele nn eh perfeito :(')
