num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 > num2 and num1 > num3:
    print('{} é maior'.format(num1))
elif num2 > num1 and num2 > num3:
    print('{} é maior!'.format(num2))
else:
    print('{} é maior!'.format(num3))