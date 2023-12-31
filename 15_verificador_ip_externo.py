#Biblioteca que permite operações com expressões regulares
import re
#Biblioteca que fornece operação de codificação e decodificação JSON
import json
#Biblioteca que sugere funções e classes que ajudam a abrir urls
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print("Detalhes do IP externo: ")
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg.: {0}'.format(org, regiao, pais, cid, ip))