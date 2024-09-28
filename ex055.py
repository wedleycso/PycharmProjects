maiorPeso = 0
menorPeso = 0
for pess in range(1,6):
    peso = float(input('digite o peso da {}° pessoa: '.format(pess)))
    if pess == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('O maior peso é {}.'.format(maiorPeso))
print('O menor peso é {}'.format(menorPeso))