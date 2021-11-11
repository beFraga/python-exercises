f = float(input('Temperatura em Fahrenheit: '))
c = 5 * ((f - 32) / 9)
print('%.2f' % c)

c = float(input('Temperatura em Celso: '))
f = ((c / 5) * 9) + 32
print('%.2f' % f)