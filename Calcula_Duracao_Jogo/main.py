'''Desenvolva um algoritmo com uma função que recebe por parâmetro a hora de início e término de um jogo,
ambas subdivididas em 2 valores distintos: horas e minutos.
A função deve apresentar a duração do jogo em horas e minutos,
considerando que o tempo máximo de duração de um jogo é de 24 horas e que o jogo pode começar em um dia e terminar no outro.'''


def calcula_duracao_jogo(hInicio, minInicio, hFim, minFim):
    hInicio = (hInicio * 60) + minInicio #Converter para mins
    hFim = (hFim * 60) + minFim
    duracao = hFim - hInicio
    hDuracao = duracao / 60
    minDuracao = duracao % 60

    print("A duração do jogo é de %d horas e %d horas" (hDuracao, minDuracao))


if __name__ == '__main__':

    hInicio = int(input("Digite a hora do horário de início do jogo: "))
    minInicio = int(input("Digite os minutos do horário de início do jogo: "))
    hFim = int(input("Digite a hora do horário de fim do jogo: "))
    minFim = int(input("Digite os minutos do horário de fim do jogo: "))

    calcula_duracao_jogo(hInicio, minInicio, hFim, minFim)
