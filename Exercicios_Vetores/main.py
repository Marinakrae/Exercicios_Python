'''
1 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
2 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
3 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
4 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
 Caso contrário, ele será classificado como "Inocente".
'''

def questao4():


def questao1():
    vet = []
    mult = 1
    soma = 0
    for i in range(5):
        vet.append(int(input("Digite um número inteiro: ")))
        soma = soma + vet[i]
        mult = mult * vet[i]

    print("Soma:", soma, "Multiplicação:", mult, "Números:", vet)


def questao2():
    alt = []
    idade = []
    for i in range(5):
        alt.append(float(input("Digite a altura:")))
        idade.append(int(input("Digite a idade:")))

    alt.reverse()
    idade.reverse()

    print("Alturas: ", alt, "Idades: ", idade)


def questao3():
    a = []
    soma = 0
    for i in range(10):
        a.append(int(input("Digite um numero inteiro:")))
        soma += a[i]*a[i]

    print("Soma dos quadrados dos elementos:", soma)


if __name__ == '__main__':
    # questao1()
    # questao2()
    #questao3()
