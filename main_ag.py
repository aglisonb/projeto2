import random

TARGET_PHRASE = "METHINKS IT IS LIKE A WEASEL"
MUTATION_CHANCE = 0.05
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


def generate_phrase_rand():
    phrase_rand = ''

    for i in range(len(TARGET_PHRASE)):
        position_char = random.randint(0, len(CHARS) - 1)
        phrase_rand += CHARS[position_char]

    return phrase_rand


def mutate(phrase_rand):
    phrase = ''

    for i in range(len(phrase_rand)):
        if random.random() <= MUTATION_CHANCE:
            position_char = random.randint(0, len(CHARS) - 1)
            phrase += CHARS[position_char]
        else:
            phrase += phrase_rand[i]

    return phrase


def calculate_fitness(phrase):
    score = 0

    for j in range(len(TARGET_PHRASE)):
        if phrase[j] == TARGET_PHRASE[j]:
            score += 1

    return score

generation_count = 0
phrase_rand = generate_phrase_rand()


while phrase_rand != TARGET_PHRASE:
    best_phrase = ''
    best_score = 0

    for i in range(100):
        phrase = mutate(phrase_rand)
        score = calculate_fitness(phrase)

        if score >= best_score:
            best_phrase = phrase
            best_score = score

    print(f"Generation : {generation_count} - Phrase: {best_phrase} - Score: {best_score}")
    phrase_rand = best_phrase
    generation_count += 1
