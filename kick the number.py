import random

true = True
acertos = 0
erros = 0
while true is True:
    chute = int(input('Insira um número inteiro de 0 a 10: '))


    # n1 = random.randrange(0,6)
    # n2 = random.randrange(0,6)
    result = random.randrange(0,11)

    if chute > 10 or chute < 0:
        print('Não consegue seguir simples instruções?')
    else:
        if chute == result:
            print('Acertou!!')
            acertos += 1
        else:
            print('Errou.. o resultado era {}'.format(result))
            erros += 1
    print('Acertos:{}\nErros:{}\n'.format(acertos, erros))
