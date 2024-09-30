anoAtual = 2024
anoNasc = int(input('Digite o ano de seu nascimento: '))
idade = anoAtual - anoNasc

if idade <= 9:
    print('Você é um atleta mirim!')

elif 9 < idade == 14 :
    print('Você é um atleta infantil!')

elif 14 < idade == 19 :
    print('Você é um atleta júnior')

elif 19 < idade == 20 :
    print('Você é um atleta sênior')

else:
    print('Você é um atleta master.')