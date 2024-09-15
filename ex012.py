preco = float(input('Digite o preço do produto: '))
desconto = (5/100) * preco
precoN = preco - desconto
print('O valor do seu produto é {}, após o desconto de 5% o valor é {}'.format(preco, precoN))