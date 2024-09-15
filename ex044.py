valorProd = float(input('Digite o valor do produto: '))
print('Escolha forma de pagamento: ')
print('À vista no Dinheiro / Cheque: - 1')
print('À vista Cartão de crédito: - 2')
print('Parcelado em até 2x: - 3')
print('Parcelado em 3x ou mais: - 4')

opção = input('Digite a opção desejada: ')

if opção == '1':
    desc = valorProd - (valorProd * 0.10)
    print('O valor a ser pago com 10% de desconto é {}R$.'.format(desc))

elif opção == '2':
    desc = valorProd - (valorProd * 0.05)
    print('O valor a ser pago com 5% de desconto é {}R$.'.format(desc))

elif opção == '3':
    print('O valor a ser pago é {}R$.'.format(valorProd))

elif opção == '4':
    acresc = valorProd + (valorProd * 0.20)
    print('O valor a ser pago com 20% de juros é {}R$'.format(acresc))

else:
    print('Erro')