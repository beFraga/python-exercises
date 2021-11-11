perguntas = ['Que horas são', 'Como está o clima', 'Como vai']
respostas = ['Agora é hora de beber água!', 'Normal', 'Bem, obrigado por perguntar :p']
pergunta = str(input('Faça uma pergunta: '))

if pergunta.lower() == perguntas[0].lower():
    print(respostas[0])

elif pergunta.lower() == perguntas[1].lower():
    print(respostas[1])

elif pergunta.lower() == perguntas[2].lower():
    print(respostas[2])

else:
    print('As perguntas possiveis são:\n{}\n{}\n{}\nObs: não é case sensitive.'.format(perguntas[0], perguntas[1], perguntas[2]))
