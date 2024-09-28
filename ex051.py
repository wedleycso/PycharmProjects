primeiroT = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
decT = primeiroT + (10 - 1) * razao
for i in range(primeiroT, decT + razao, razao):
    print('{}'.format(i), end='-> ')
print('ACABOU!!')