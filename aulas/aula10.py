#if carro.esquerda():
#    bloco True
#else:
#    bloco False

#tempo = int(input('Quantos anos de fabricação tem o seu carro? '))
#if tempo <= 10:
#    print('Seu carro é novo.')
#else:
#    print('Está na hora de trocar de carro!')
#print('--Fim!--')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m >= 7.0:
    print('Sua média foi boa! PARABÉNS!!')
else:
    print('Sua média precisa melhorar!!')