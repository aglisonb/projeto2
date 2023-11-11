"""Dawkin's Weasel Program"""

import random
import string

objetivo = 'METHINKS IT IS LIKE A WEASEL'
frase_inicial = 'JDN CHDJNS OWIU C HDSJMNVPME'
frase_pai = frase_inicial
melhor_pontuacao = 0


def mutacao():
    chance_de_mutacao = random.random()
    return chance_de_mutacao


def score(replica):
    pontos = 0
    for n in range(28):
        if replica[n] == objetivo[n]:
            pontos += 1
    return pontos


while melhor_pontuacao < 27:
    for n in range(100):
        replica = frase_pai
        for letra in frase_pai:
            check_mutacao = mutacao()
            if check_mutacao <= 0.05:
                replica = frase_pai.replace(letra, random.choice(string.ascii_uppercase))
        check_pontuacao = score(replica)
        if check_pontuacao == 27:
            break
        elif check_pontuacao > melhor_pontuacao:
            melhor_resultado = replica

    frase_pai = melhor_resultado
