import random

n_carac = int(input('Quantos digitos irá ter a senha?'))
n_carac_ = n_carac - 1

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.']
senha = []
while n_carac > 0:
    caractere_random = random.choice(caracteres)
    n_carac -= 1
    senha.append(caractere_random)

def juntar(lista):
    if not lista:
        return ''
    
    espacamento = ''.join(lista[:-1])
    return f'{espacamento}{lista[-1]}'

print(juntar(senha))
