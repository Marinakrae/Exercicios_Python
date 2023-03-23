def imprime_msg(msg):
# Use a breakpoint in the code line below to debug your script.
    print(f'Mensagem: {msg}') # Press Ctrl+F8 to toggle the breakpoint.


def media(n1, n2):
    media = (n1 + n2) / 2
    print(f'Média: {media}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    imprime_msg('Olá Mundo')
    media(15, 89)
    '''c = int(input("Digite um número inteiro: ")) #forma decente de solicitar input
    print(c)'''

# exemplo desvio condicional
x = int(input("Digite um valor para x: "))
'''if x > 10:
print(("Maior que 10"))
elif x < 10:
print("Menor que 10")
else:
print("Eh 10")'''

# Operadores lógicos e encadeamento
if x > 10 and x < 100: # 10 < x < 100 alternativa
    print("O número esta entre 10 e 100")


# Funções retornando vários valores
def exemploFunc():
    base = float(input("Valor da base: "))
    alt = float(input("Valor da altura: "))
    return base, alt

b, h = exemploFunc()
print("Base: %.2f , Altura: %.2f" % (b, h))

#Inicialização de parametro com valor
def exemplFunc(r, pi=3.14):
    return pi * (r ** 2)

raio = float(input("Valor do raio: "))
area = exemplFunc(raio)
print("Area total: %.2f" % area)