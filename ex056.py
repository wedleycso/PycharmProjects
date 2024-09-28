somaIdade = 0
mediaIdade = 0
maiorIdaM = 0
nomevelho = ''
totMulher20 = 0
for i in range(1,5):
    print('--- {}° pessoa ---'.format(i))
    nome = str(input('Digite seu nome: ')).strip()
    sexo = str(input('Digite qual seu sexo: [M/F]')).strip()
    idade = int(input('Digite a sua idade: '))
    somaIdade += idade
    if i == 1 and sexo in 'Mm':
        maiorIdaM = idade
        nomevelho = nome
    if sexo in 'mM' and idade > maiorIdaM:
        maiorIdaM = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é {} anos'.format(mediaIdade))
print('O homem  mais velho tem {} anos e se chama {}'.format(maiorIdaM, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totMulher20))