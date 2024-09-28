num = int(input('Digite um número: '))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\33[33m', end=' ')
        cont += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num,cont))
if cont == 2:
    print('O {} É PRIMO!'.format(num))
else:
    print('O número {} não é primo!'.format(num))