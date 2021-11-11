import random

true = True
while true is True:
    iniciar = input('2d6 - 2 dados de 6 lados - ')
    dado = iniciar.split('d')
    resultados = []

    n = 0
    while n < int(dado[0]):
        res = random.randrange(1, (int(dado[1]) + 1))
        resultados.append(res)
        n += 1

    soma = sum(resultados)
    resultados.sort(reverse=True)

    print('\n{} ← {} {}'.format(soma, resultados, iniciar))
    
    finalizar = input('Continuar?')
    if finalizar is True:
        true = False
    else:
        true = True
