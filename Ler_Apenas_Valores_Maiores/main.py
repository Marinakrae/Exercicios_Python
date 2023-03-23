'''Desenvolva um algoritmo que somente permita a leitura de valores maiores que os lidos anteriormente.
Você deve definir uma condição de parada para o programa. '''

if __name__ == '__main__':

    maior_valor = float('-inf')  # Inicializa como um valor muito baixo

    print("Para parar a execução do programa, digite qualquer letra.")

    while True:
        valor = input("Digite um valor: ")
        if valor.isalpha():  # Verifica se o valor é uma letra
            break
        valor = int(valor)  # Converte o valor para inteiro
        if valor > maior_valor:
            maior_valor = valor
        else:
            print("O valor é menor do que os lidos anteriormente.")

    print("Fim do programa.")