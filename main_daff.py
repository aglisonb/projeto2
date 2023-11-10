"""Dawkin's Weasel Program"""

import random
import string

objetivo = 'METHINKS IT IS LIKE A WEASEL'
frase_atual = 'JDN CHDJNS OWIU C HDSJMNAPME'


def mutacao():
    chance_de_mutacao = random.random()
    return chance_de_mutacao


for i in range(100):
    for letra in frase_atual:
        checar_mutacao = mutacao()
        if checar_mutacao <= 0.05:
            letra = random.choice(string.ascii_uppercase)

