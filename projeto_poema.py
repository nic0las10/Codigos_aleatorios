import random

def generate_poem(name, adjective, verb, noun):
    templates = [
        f"Querida {name}, você é tão {adjective}. Seu sorriso sempre me faz {verb} de alegria. Você é a {noun} dos meus sonhos.",
        f"Para {name}, minha fonte de {adjective}, você é a razão pela qual meu coração {verb} tão forte. Minha vida contigo é como um belo {noun}.",
        f"Você, {name}, é a pessoa mais {adjective} que já conheci. Cada dia ao seu lado me faz {verb} que finalmente encontrei minha {noun}."
    ]
    return random.choice(templates)

def main():
    her_name = input("Digite o nome dela: ")
    an_adjective = input("Digite um adjetivo para descrevê-la: ")
    a_verb = input("Digite um verbo que a faça pensar em você: ")
    a_noun = input("Digite um substantivo que a lembre de vocês: ")

    poem = generate_poem(her_name, an_adjective, a_verb, a_noun)
    print("\nAqui está um poema personalizado para ela:\n")
    print(poem)
