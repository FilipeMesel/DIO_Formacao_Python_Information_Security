#Importando a biblioteca socket que faz o relacionamento com a placa de rede de um sistema operacional
import socket

#Biblioteca que fornece o acesso a algumas variáveis e funções que tem forte interação com um interpretador
import sys

def main():
    try:
        #Tentando criar um socket IP(socket.AF_INET) no modelo TCP(0)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()
    
    print("Socket criado com sucesso!")
    host_alvo = input("Digite o Host ou Ip a ser conectado: ")
    porta_alvo = input("Digite a Porta a ser conectada: ")

    try:
        #Tentando estabelecer um cliente e conecta-lo ao host indicado
        s.connect((host_alvo, int(porta_alvo)))
        print("Cliente TCP Criado com sucesso no host " + host_alvo + " e na porta " + porta_alvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no host " + host_alvo + " e na porta " + porta_alvo)
        print("Erro: {}".format(e))
        sys.exit()
        
#TESTE: HOST => google.com PORTA => 80
if __name__ == "__main__":
    main()

