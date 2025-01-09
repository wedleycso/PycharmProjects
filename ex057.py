sexo = str(input('Digite qual o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, digite os dados corretamente: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))