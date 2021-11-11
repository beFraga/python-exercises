import random

resultados = []
continuar = True
true = True
while true is True:
    if continuar is True:
        n1 = int(input('\nDigite o valor 1: '))
        n2 = int(input('Digite o valor 2: '))
    if n1 > n2:
        num = random.randrange(n2, (n1 + 1))
    else:
        num = random.randrange(n1, (n2 + 1))
    print('\nO valor foi: {}'.format(num))

    if resultados.__len__() != 0:
        print(resultados)
    if resultados.__len__() == 10:
        resultados.pop(0)
    resultados.append(num)

    cont = input('Digite alguma coisa para mudar o valor: ')
    if cont == '':
        continuar = False
    else:
        continuar = True

    if n1 == 'parar' or n2 == 'parar' or cont == 'parar':
        break
    if n1 == 'reset' or n2 == 'reset' or cont == 'reset':
        resultados.clear()
    print(resultados)



