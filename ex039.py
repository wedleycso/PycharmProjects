dateAniv = int(input('Digite o ano de seu aniversário: '))
anoAtual = 2024

if (anoAtual-dateAniv) == 18:
    print('Parabéns, você está no período de alistamento!')

elif (anoAtual-dateAniv) < 18:
    resultado = 18 - (anoAtual - dateAniv)
    print('Sinto muito, você não está no período de alistamento! Faltam {} anos para você se alistar.'.format(resultado))

elif (anoAtual-dateAniv) > 18:
    resultado = (anoAtual - dateAniv) - 18
    print('Atenção!!! Você passou do período de alistamento! Você está a {} anos atrasado para o seu alistamento.'.format(resultado))