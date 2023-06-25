#Importação da biblioteca que trabalha com hashes
#hashes são algoritmos de criptografia
import hashlib

#Armazenando o nome dos arquivos a serem lidos e comparados
arquivo1 = '06_a.txt'
arquivo2 = '06_b.txt'

#Usando o algoritmo hash ripemd160
hash1 = hashlib.new('ripemd160')

#Realizando a comparação do hash do arquivo1, abrindo-o no modo 'rb'(binário)
hash1.update(open(arquivo1, 'rb').read())

#Usando o algoritmo hash ripemd160
hash2 = hashlib.new('ripemd160')

#Realizando a comparação do hash do arquivo2, abrindo-o no modo 'rb'(binário)
hash2.update(open(arquivo2, 'rb').read())

#O método digest() resume os dados passados pelo método update da classe Hash
if hash1.digest() != hash2.digest():
    print(f'O arquivo {arquivo1} é diferente do arquivo: {arquivo2}')
    #Resumindo o hash em hexadecimal e printando na tela
    print('Hash do arquivo1: ', hash1.hexdigest())
    print('Hash do arquivo2: ', hash2.hexdigest())
else:
    print(f'O arquivo {arquivo1} é igual ao arquivo: {arquivo2}')
    print('Hash do arquivo1: ', hash1.hexdigest())
    print('Hash do arquivo2: ', hash2.hexdigest())
