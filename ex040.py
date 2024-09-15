nota1 = float(input('Digite a sua nota de av1: '))
nota2 = float(input('Digite sua nota de av2: '))
média = (nota1 + nota2) / 2

if média < 5.0:
    print('Reprovado!!')

elif 5.0 <= média < 7.0:
    print('Recuperação!')

elif média >= 7:
    print('APROVADO!')