import os
import time

textoNaTela = "\ncomo limpar a tela do terminal cmd"

print(10 * textoNaTela)
print("\nLimparei a tela em 5 segundos!")
time.sleep(5)

os.system("cls")