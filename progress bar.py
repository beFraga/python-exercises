import os
import time

porcentagem = 1
progress = '■' * porcentagem

while porcentagem < 100:
    for var in progress:
        print('{}% - Em progresso'.format(porcentagem))
        print(progress)
        time.sleep(0.001)
        os.system('cls')
        porcentagem += 1
        progress = '■' * porcentagem
        if porcentagem == 101:
            print('Concluido!')
            break

time.sleep(2)
