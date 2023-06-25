#UDP: Protocolo de Datagrama do Usuário

#Esse código funciona em conjunto com o código do servidor. Primeiro rode o código do servidor para depois rodar o código do cliente.

#Importando a biblioteca socket que faz o relacionamento com a placa de rede de um sistema operacional
import socket

#Tentando criar um objeto de conexão socket IP(socket.AF_INET) no modelo UDP(socket.SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente socket criado com sucesso!")

host = 'localhost'
porta = 5433 #Porta do cliente
menssagem = 'Olá Servidor! Firmeza?'

try:
    print("Cliente: " + menssagem)
    #Tentando empacotar a menssagem e enviar ao host que está escutando dados na porta 5432
    s.sendto(menssagem.encode(), (host, 5432))

    #Tanto a variavel "dados" quanto a variavel "servidor" vão receber do servidor a resposta de 4096 bytes
    dados, servidor = s.recvfrom(4096)

    #A variavel "dados" agora recebe os bytes recebidos e desempacotados
    dados = dados.decode()
    print("Cliente: " + dados)

finally:
    print("Cliente: Fechando a conexão!")
    #Evita que o código fique em loop
    s.close()
