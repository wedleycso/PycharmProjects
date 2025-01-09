from random import randint

npc = randint(0,10)
palpite = 0
acertou = False
print('-~-' * 20)
print('vou pensar em número entre 0 e 10. Tente Adivinhar.')
print('-~-' * 20)
while not acertou:
    jogador = int(input('Em qual número pensei? '))
    palpite = palpite + 1
    if jogador == npc:
        acertou = True
    else:
        if jogador < npc:
            print('Tente um número maior.')
        elif jogador > npc:
            print('Tente um número menor.')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))