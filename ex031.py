distKM = float(input('Digite a distância da sua viagem em Km: '))
precoPassagem = 0
if distKM <= 200:
    precoPassagem = distKM * 0.50
    print('Para a distância da sua viagem a passagem vai custar R${}.'.format(precoPassagem))
else:
    precoPassagem = distKM * 0.45
    print('Para essa distância a passagem vai custar R${}'.format(precoPassagem))