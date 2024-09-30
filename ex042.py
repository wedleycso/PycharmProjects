def triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))

if triangulo(a,b,c):
    print('Os valores digitados podem formar um triângulo.')

    if a == b == c:
        print('Os lados formam um triângulo equilátero.')

    elif a == b or a == c or b == c:
        print('Os lados formam um triângulo isósceles.')

    else:
        print('Os lados formam um triângulo escaleno ')
else:
    print('infelizmente os valores não podem formar um triângulo.')