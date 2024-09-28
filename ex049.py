n = int(input('Digite o número o qual você deseja saber a tabuada: '))
for i in  range(1,11):
    print('{} X {:2} = {}'.format(n, i, n*i))