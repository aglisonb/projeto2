import random
import string

frase_alvo = "METHINKS IT IS LIKE A WEASEL"
tamanho_populacao = 100
chance_mutacao = 0.05
geracao = 0

frase_atual = ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(len(frase_alvo)))
    
while frase_atual != frase_alvo:
    populacao = [''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(len(frase_alvo))) for _ in range(tamanho_populacao)]
    aptidao = [(sum(1 for t, s in zip(frase_alvo, seq) if t == s), seq) for seq in populacao]
    melhor_sequencia = max(aptidao, key=lambda x: x[0])
    frase_atual = melhor_sequencia[1]
    
    if geracao % 100 == 0: 
