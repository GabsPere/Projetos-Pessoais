# modulos usados
import time
import random
import json
guerreiro = 'Jacthor'

# personagem
personagem = {"dano": 0, "defesa": 0, "sorte": 0}

# background cap1
print(f'{guerreiro} era muito astusto, você quer um exemplo? Ele nunca errava uma advinhação')
time.sleep(3)
print('Você acha isso fácil? Vamos tentar')

time.sleep(3)
print('Primeiro desafio! Valendo 10 pontos de dano.\n')

# jogo de adivinhação
print("Comecando o jogo...")
time.sleep(3)
chute = 0
vidas = 3
numerorandom = random.randint(0, 10)
while chute != numerorandom:
    chute = int(input('Chute um número entre 0 e 10\n> '))
    if chute == numerorandom:
        personagem["dano"] = 10
        print(
            f'Parabéns você acertou!\nParece fácil, mas futuramente irá dificultar\n'
            f'Seu dano agora é {personagem["dano"]}')
        with open("personagem.json", "w") as json_file:
            json.dump(personagem, json_file)
        break
    else:
        print(f'Eu disse que não era tão fácil assim!')
        vidas = vidas - 1
        print(f'Menos uma vida, restam {vidas}')
    if vidas == 0:
        print('suas vidas acabaram!')
        print('Bom, não é tão facil assim, certo?')
        break
