from random import randint

npc = randint(0,5)
print('-~-' * 20)
print('vou pensar em número entre 0 e 5. Tente Adivinhar.')
print('-~-' * 20)
jogador = int(input('Em qual número pensei? '))
if jogador == npc:
    print('Meus parabéns, você acertou!!!')
else:
    print('Infelizmente você errou! Se for chorar manda áudio.')