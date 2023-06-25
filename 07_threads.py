#Importando a biblioteca que permite o multithreading no python
from threading import Thread

#Biblioteca de delay
import time

# def carro1(velocidade):
#     trajeto = 0 #carrinho inicia no km 0

#     while trajeto <= 100:
#         print('Carro1: ', trajeto)
#         trajeto+= velocidade

# def carro2(velocidade):
#     trajeto = 0 #carrinho inicia no km 0

#     while trajeto <= 100:
#         print('Carro2: ', trajeto)
#         trajeto+= velocidade

#Modo sequencial
# carro1(10)
# carro2(20)

def carro(velocidade, piloto):
    trajeto = 0 #carrinho inicia no km 0

    while trajeto <= 100:
        trajeto+= velocidade
        time.sleep(0.5)
        print('Piloto: {} Km {} '.format(piloto, trajeto))


#Modo multithread
# A velocidade é indicada em "args"
t_carro1 = Thread(target = carro, args = [1, 'Bruno'])
t_carro2 = Thread(target = carro, args = [10, 'Python'])

t_carro1.start()
t_carro2.start()