# estrutura de repetição com teste lógico.
# while
'''for i in range(1, 11):
    print(i)
print('fim.')'''
'''i = 1
while i < 11:
    print(i)
    i = i + 1
print('fim.')'''

r = 'S'
while r == 'S':
    int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim.')