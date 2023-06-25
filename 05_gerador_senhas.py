#Biblioteca para gerar caracteres aleatórios
import random

#Biblioteca para importar o objeto string
import string

#Constante que recebe o limite máximo de tamanho de caracteres desejado das senhas
TAMANHO = int(input("Digite o tamanho de senha que você deseja: "))

CHARS = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;:/?'

#Gerando números aleatórios a partir de fontes fornecidas do sistema operacional
rnd = random.SystemRandom()

#rnd.choice retorna uma lista para caracteres randomicos
#Para cada "i" no range tamanho, será gerada uma nova letra(string.ascii_letters), 
#número(string.digits) ou símbolo(!@#$%&*()-=+,.;:/?)
print(''.join(rnd.choice(CHARS) for i in range(TAMANHO)))