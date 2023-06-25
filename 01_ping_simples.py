# Importação da biblioteca para usar comandos do sistema operacional
import os

#Input do ip ou host a realizar o ping
ip_ou_host = input("Digite Ip ou host a ser verificado: ")

#Realizando o ping
os.system('ping -n 6 {}'.format(ip_ou_host))