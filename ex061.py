a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = int(input('Digite o termo que deseja exibir: '))
contador = 0
termo = a1
print('Progressão aritmética: ')
while contador < n:
    print(termo, end=" -> ")
    termo += r
    contador += 1
print('Fim!')