import random

resultados = []
true = True
d6 = 7
d8 = 9
d10 = 11
d12 = 13
d20 = 21
d100 = 101
d10_100 = 11
dados = [d6, d8, d10, d12, d20, d100, d10_100]
dado = 0
print('Comandos extras, como:\ndados, parar e reset')
while true is True:
    iniciar = input('\nDigite qualquer coisa para rolar: ')

    if iniciar == 'reset':
        resultados.clear()
    if iniciar == 'parar':
        break
    if iniciar == 'dados':
        dado = int(input('Selecione o dado que você quer:\nd6 = 0 | d8 = 1 | d10 = 2 | d12 = 3 | d20 = 4 | d100 = 5 | d10V100 = 6: '))
        resultados.clear()

    selecionado = dados[dado]
    num = random.randrange(1, selecionado)
    if dado == 6:
        print('\nResultado:{}'.format((num * 10)))
    else:
        print('\nResultado:{}'.format(num))

    if resultados.__len__() != 0:
        print(resultados)

    if resultados.__len__() == 10:
        resultados.pop(0)

    resultados.append(num)
