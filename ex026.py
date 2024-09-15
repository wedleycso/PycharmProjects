frase = str(input('Digite algo: ')).strip().upper()
print('Na sua frase a letra A aparece {} vezes.'.format(frase.count('A')+1))
print('A primeira letra "a" apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra "a" apareceu na posição {}'.format(frase.rfind('A')+1))