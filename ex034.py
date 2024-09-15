salafun = float(input('Digite o seu salário para o calculo da promoção: '))
if salafun >= 1250:
    salpromo = salafun + (salafun * (10 / 100))
    print('O seu salário após a promo é {}'.format(salpromo))
else:
    salpromo = salafun + (salafun * (15 / 100))
    print('O seu novo salário é {}'.format(salpromo))