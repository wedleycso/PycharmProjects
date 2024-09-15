num = int(input('Digite um número para saber se ele é par ou ímpar: '))
result = num % 2
if result == 0:
    print('{} é par'.format(num))
else:
    print('{} é ímpar'.format(num))