"""Dawkin's Weasel Program"""

import random
import string

objetivo = 'METHINKS IT IS LIKE A WEASEL'
frase_inicial = 'JDN CHDJNS OWIU C HDSJMNVPME'
frase_pai = frase_inicial
melhor_pontuacao = 0
melhor_resultado = ''


def mutacao():
    chance_de_mutacao = random.random()
    return chance_de_mutacao


def score(frase):
    pontos = 0
    for n in range(28):
        if frase[n] == objetivo[n]:
            pontos += 1
    return pontos


while melhor_pontuacao < 27:
    for i in range(100):
        replica = ''
        for letra in frase_pai:
            check_mutacao = mutacao()
            if check_mutacao <= 0.05:
                replica += random.choice(string.ascii_uppercase)
            else:
                replica += letra
        if check_pontuacao == 27:
            break
        elif check_pontuacao > melhor_pontuacao:
            melhor_resultado = replica

    if melhor_resultado != '':
        frase_pai = melhor_resultado
    print(frase_pai)
