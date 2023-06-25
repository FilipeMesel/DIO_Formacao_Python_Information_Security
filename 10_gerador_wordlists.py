#WORDLISTS são arquivos de texto contendo uma palavra por linha
#São usadas em ataques de força bruta; para tentar descobrir senhas

#Biblioteca que fornece condições para iterações como permutação e combinação
import itertools

palavra = input("Digite a string a ser permutada: ")
qtd_permutations = int(input("Digite a quantidade de permutações: "))

#Entre () devem ir as palavras a serem permutadas e a quantidade strings a serem geradas
resultado = itertools.permutations(palavra, qtd_permutations)

#Para cada caractere gerado, vamos printá-lo, juntando com o próximo caracter
for i in resultado:
    print(''.join(i))
    print('\r\n')
    