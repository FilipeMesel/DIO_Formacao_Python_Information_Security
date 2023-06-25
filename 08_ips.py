#Biblioteca que permite a manipulação de IPs
import ipaddress

ip = '192.168.0.1'

#Convertendo a string em um objeto ipaddress
endereco = ipaddress.ip_address(ip)

print(endereco)
print(endereco + 100)
print(endereco + 256)

#Também atua com redes
rede = '192.168.0.0/24'
#Convertendo a string em um objeto ipaddress
rede_obj = ipaddress.ip_network(rede, strict = False)
print('rede: ', rede_obj)

for ip in rede_obj:
    print('Ip: ', ip)