#Importação da biblioteca que trabalha com hashes
#hashes são algoritmos de criptografia
import hashlib

valor = input("Digite a String para hashear: ")
menu = int(input('''### MENU - ESCOLHA O TIPO DE HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

#Criando uma variável para receber a string a ser transformada em hash
# O "b" dentro dos () converte a string em bytes
# resultado = hashlib.md5(b'Python para seguranca')
resultado = hashlib.md5(valor.encode('utf-8'))
if menu == 1:
    resultado = hashlib.md5(valor.encode('utf-8'))
elif menu == 2:
    resultado = hashlib.sha1(valor.encode('utf-8'))
elif menu == 3:
    resultado = hashlib.sha256(valor.encode('utf-8'))
elif menu == 4:
    resultado = hashlib.sha512(valor.encode('utf-8'))
else:
    print("Valor de entrada inválido")

print("O Hash da String é: ", resultado.hexdigest())