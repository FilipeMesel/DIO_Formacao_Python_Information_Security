#UDP: Protocolo de Datagrama do Usuário

#Importando a biblioteca socket que faz o relacionamento com a placa de rede de um sistema operacional
import socket

#Tentando criar um objeto de conexão socket IP(socket.AF_INET) no modelo UDP(socket.SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!")

host = 'localhost'
porta = 5432 #Porta do servidor

#Realizando a ligação cliente/ servidor por meio do host e da porta
s.bind((host, porta))

#Menssagem a ser enviada ao cliente
menssagem = 'Olaaaaaaa cliente! e ai? beleza?'

while 1:

    #Variavel "dados" e variavel "end" recebem 4096 bytes
    dados, end = s.recvfrom(4096)

    #Caso tenha recebido algum dado...
    if dados:
        print("Servidor enviando menssagem...")
        #Enviando pacotes ao cliente
        s.sendto(dados + (menssagem.encode()), end)