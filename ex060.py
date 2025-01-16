import math

nume = int(input('digite o número que você deseja fatorar: '))
if nume >= 0:
    resultado = math.factorial(nume)
    print('O fatorial de {}! é {}'.format(nume,resultado))
else:
    print('Digite um número positivo para fatorar!')