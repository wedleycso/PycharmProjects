import random

opcoes = ['pedra', 'papel', 'tesoura']

def det_vencedor(usuario, npc):
    if usuario == npc:
        return 'Empate!'

    regras = {
        'pedra': ['tesoura'],
        'papel': ['pedra'],
        'tesoura': ['papel']
    }

    if npc in regras[usuario]:
        return 'Você venceu!!'
    else:
        return 'Você perdeu!!'

print('Escolha entre: pedra, papel e tesoura: ')
usuario = input().strip().lower()

if usuario not in opcoes:
    print('Opção inválida!! Escolha entre pedra, papel ou tesoura.')

else:
    npc = random.choice(opcoes)
    print(f'O computador escolheu: {npc}')

resultado = det_vencedor(usuario, npc)
print(resultado)