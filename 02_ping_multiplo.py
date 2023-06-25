# Importação da biblioteca para usar comandos do sistema operacional
import os

#Acessando o arquivo hosts.txt
with open('02_hosts.txt') as file:
    #Armazenando os dados do arquivos na variável dump
    dump = file.read()
    #Considerando as linhas separadas na variávl dump
    dump = dump.splitlines()
    #Lendo os dados da variável e realizando o ping
    for ip in dump:
        print(ip)
        #Realizando o ping
        os.system('ping -n 2 {}'.format(ip))