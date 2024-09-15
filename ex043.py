altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso!')

elif 18.5 <= imc < 25:
    print('Você está com o peso ideal!')

elif 25 <= imc < 30:
    print('Você está com sobrepeso!')

elif 30 <= imc < 40:
    print('Você está obeso!')

else:
    print('Alerta de Thaís Carla detectada.')