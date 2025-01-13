numa = int(input('Digite um número: '))
numb = int(input('Digite o segundo número: '))
result = 0
while True:
    print('Use uma das opções a seguir para escolher o que deseja fazer: ')
    print('*~*' *20)
    print('[1]-Para SOMA.')
    print('[2]-Para MULTIPLICAR.')
    print('[3]-Para MAIOR.')
    print('[4]-Para NOVOS NÚMEROS.')
    print('[5]-Para SAIR DO PROGRAMA.')
    print('*~*' *20)
    escolha = input('Digite a opção desejada: ')
    if escolha == '1':
        result = numa + numb
        print('A soma entre {} e {} é {}.'.format(numa, numb, result))
    elif escolha == '2':
        result = numa * numb
        print('A multiplicação entre {} e {} é {}.'.format(numa, numb, result))
    elif escolha == '3':
        if numa > numb:
            print('O {} é maior'.format(numa))
        else:
            print('O {} é maior'.format(numb))
    elif escolha == '4':
        numa = int(input('Digite um número: '))
        numb = int(input('Digite o segundo número: '))
    elif escolha == '5':
        print('Você saiu do programa! Até a próxima.')
        break
    else:
        print('Opção inválida!')
print('Fim do programa!')