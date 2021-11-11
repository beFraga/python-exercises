import time

current_time = time.localtime()
dia_atual = int(time.strftime('%d', current_time))
mes_atual = int(time.strftime('%m', current_time))

dia = int(input('Qual o dia do seu aniversário? '))
mes = int(input('Qual o mês do seu aniversário? '))

if mes < 1 or mes > 12 or dia > 31 or dia < 1:
    print('Data não reconhecida')
else:
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    calculo_data = [0]
    calculo_atual = [0]

    def_mes_data = mes - 2
    while def_mes_data > -1:
        calculo_data1 = meses[def_mes_data]
        def_mes_data -= 1
        calculo_data.append(calculo_data1)
    soma_data = sum(calculo_data) + dia

    def_mes_atual = mes_atual - 2
    while def_mes_atual > -1:
        calculo_atual1 = meses[def_mes_atual]
        def_mes_atual -= 1
        calculo_atual.append(calculo_atual1)
    soma_atual = sum(calculo_atual) + dia_atual

    distancia = 0

    while soma_data != soma_atual:
        if soma_atual == 365:
            soma_atual = 1
            distancia += 1
        else:
            soma_atual += 1
            distancia += 1
        
    diaS = 'dias'
    if distancia == 1:
        diaS = 'dia'
    if soma_data == soma_atual:
        if distancia == 0:
            print('FELIZ ANIVERSÁRIO!!')
        else:
            print('{} {} para seu aniversário.'.format(distancia, diaS))
