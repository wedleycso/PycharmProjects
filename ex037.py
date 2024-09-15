num = int(input('Digite um número: '))
print('Deseja converter o número {} para qual base: '.format(num))
print('1 - Base binária.')
print('2 - Base octal.')
print('3 - Base hexadecimal.')
binário = bin(num)
octal = oct(num)
hexadecimal = hex(num)

opção = input('Digite o número da opção desejada: ')

if opção == '1':
    print('O {} na base binária é {}'.format(num, binário))

elif opção == '2':
    print('O {} na base octal é {}'.format(num, octal))

elif opção == '3':
    print('O {} na base hexadecimal é {}'.format(num, hexadecimal))

else:
    print('Erro!')