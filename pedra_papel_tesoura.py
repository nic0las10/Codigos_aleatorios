import random

def play():
    jogador = input("Qual sua escolha?: 'PE' pra pedra, 'PA' for papel, 'TE' pra tesoura\n")
    oponente = random.choice(['PE', 'PA', 'TE'])
    escolha_aleatoria =(oponente)
    print("escolha alatoria:", escolha_aleatoria)

    if jogador == oponente:
        return 'Deu\'empate!'
    
    # PE > PA, PA > TE, TE > PE
    if vitoria(jogador, oponente):
         return 'Você venceu!'
    else:
        return 'Você perdeu!'


def vitoria(jogador , oponente):
    # return true if jogador ganhar do oponente!

    if (jogador == 'PE' and oponente =='TE') or (jogador == 'TE' and oponente == 'PA')\
        or (jogador == 'PA' and oponente == 'PE'):
        return True
    else:
        False

resultado = play()
print(resultado)





