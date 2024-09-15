larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print('A dimensão da sua parede é {} metros de largura  e {} metros de altura que resultam em {} m².'.format(larg, alt, area))
print('Para pintar essa parede será necessário {} litros de tinta'.format(tinta))