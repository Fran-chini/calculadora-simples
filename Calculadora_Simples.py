#Criar uma calculadora simples com Soma, Subtração, Multiplicação e Divisão
from time import sleep
valores = list()
print('-' * 30)
print('▣{:^28}▣'.format('CALCULADORA SIMPLES'))
sleep(1)
while True:
    print('-'*30)
    print('▣{:^28}▣'.format('OPÇÕES DE CALCULOS'))
    print('-' * 30)
    sleep(1)
    print(''' 
[ 1 ] Adição
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
''')
    comando = int(input('Escolha uma ação: '))
    for c in range(2):
        valores.append(float(input(f'Digite o {c+1}º número:')))
    sleep(1)
    if comando == 1:
        print(f'A soma entre {valores[0]} e {valores[1]} é: {valores[0] + valores[1]}')
    elif comando == 2:
        print(f'A subtração entre {valores[0]} e {valores[1]} é: {valores[0] - valores[1]}')
    elif comando == 3:
        print(f'A multiplicação entre {valores[0]} e {valores[1]} é: {valores[0] * valores[1]}')
    elif comando == 4:
        print(f'A divisão entre {valores[0]} e {valores[1]} é: {valores[0] / valores[1]}')
    else:
        print('Opção inválida! Tente novamente')
    resp = str(input('Quer continuar?[S/N]'))
    if resp in 'Nn':
        print('Finalizando processo', end='')
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        break

