import random
import string

frase = "METHINKS IT IS LIKE A WEASEL"
populacao = 100
chancedemutacao = 0.05
geracao = 0 

string = ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(len(frase)))

while frase != string
    
