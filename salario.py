s_hora = float(input('Quanto você ganha p/ hora? '))
horas = float(input('Quantas horas você trabalha no mês? '))

salario_bruto = s_hora * horas
ir = (salario_bruto / 100) * 11
inss = (salario_bruto / 100) * 8
sindicato = (salario_bruto / 100) * 5
salario = ((salario_bruto - ir) - inss) - sindicato

print('Salario bruto: {}'.format(salario_bruto))
print('IR (11%): {}'.format(ir))
print('INSS (8%): {}'.format(inss))
print('Sindicato (5%): {}'.format(sindicato))
print(salario)


