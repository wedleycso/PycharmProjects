carVelocidade = float(input('Qual a sua velocidade? '))
limiteVel = float(80.00)
if carVelocidade > limiteVel:
    multa = (carVelocidade - limiteVel) * 7
    print('Você recebeu uma multa de R${:.2f} por excesso de velocidade com acréscimo de R$7,00 por Km acima do limite.' .format(multa))
else:
    print('Parabéns! Você está dirigindo dentro do limite da via!')