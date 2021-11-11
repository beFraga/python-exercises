import time
a = 1
while a > 0:
    current_time = time.localtime()
    timestamp = time.strftime("%H:%d:%M", current_time)
    # H = hora / M = minuto / m = mes / S = segundo / Y = 2021 / y = 21 / D = data
    time.sleep(1)
    print(timestamp)
    print(current_time)