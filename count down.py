from time import sleep
import time
n = 3
stri = str(n) + '..\n'
true = True
while true is True:
    current_time = time.localtime()
    timestamp = time.strftime("%H:%M:%S", current_time)
    if true is True:
        while n > 0:
            for var in stri:
                tempo = 1 / len(stri)
                time.sleep(tempo)
                print(var, end='', flush=True)
            n -= 1
            stri = str(n) + '..\n'
    if n == 0:
        print('Happy new year!!!')
        true = False
