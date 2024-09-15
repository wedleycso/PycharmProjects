# + Adição
# Operadores Aritméticos
# - Subtração
# * Multiplicação
# / Divisão
# ** Potênciação
# // Divisão inteira
# % Resto da divisão
# Ordem de precedência:
# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - +, -

#n1 = int(input('Digite um número: '))
#n2 = int(input('Digite outro número: '))
#print('A soma vale {}'.format(n1+n2))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d =  n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {}'.format(s, sub, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))