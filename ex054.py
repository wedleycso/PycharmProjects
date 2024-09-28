from datetime import date
anoAtual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    dataNasc = int(input('Em que ano a {}° pessoa nasceu: '.format(pess)))
    idade = anoAtual - dataNasc
    print('Essa pessoa tem {} anos'.format(idade))
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('e também tivemos {} pessoas menores de idade.'.format(totmenor))