'''
1 - Crie um dicionário e armazene nele os seus dados: nome, idade, telefone, endereço.
Imprima todos os dados usando o padrão chave: valor.

2 - Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário.
Leia os dados de todos os contatos do usuário de forma que a agenda fique completa e por fim imprima todos os contatos.
'''

if __name__ == '__main__':
    #1
    dicionario = {"nome": "Marina", "idade": 21, "telefone": 51982432302, "endereco": "Rua dos Andradas"}
    for chave in dicionario:
     print(chave, "\t" ,dicionario[chave])

    #2
    dict1 = {}
    tam = int(input("Digite o tamanho da agenda:"))

    for i in range(tam):
        nome = input("Digite o nome:")
        telefone = input("Digite o telefone:")
        dict1[nome] = telefone #nome eh a chave e telefone o valor

    print("Contatos:", dict1)


