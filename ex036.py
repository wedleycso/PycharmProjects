valorCasa = float(input('Qual o valor da casa que deseja comprar? '))
sal = float(input('Qual o seu salário? ' ))
prazoDePagamento = int(input('Em quantos anos deseja pagar o empréstimo? '))
mensalidade = valorCasa / (prazoDePagamento * 12)
if mensalidade >= (sal*(30/100)):
    print('Infelizmente o empréstimo não foi aprovado pois a parcela é maior que 30% do seu salário.')
else:
    print('PARABÉNS!O seu empréstimo foi aprovado e valor da sua mensalidade será {:.2f}R$.'.format(mensalidade))