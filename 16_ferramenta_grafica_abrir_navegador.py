#Biblioteca que fornece uma interface de alto nível para permitir a exibição de documentos web
#aos usuários
import webbrowser
#Biblioteca que fornece interface padrão do python para o kit de ferramentas gráficas Tk
from tkinter import *

#() vaziu indica que o sistema não tem nome
root = Tk( )

#Título do sistema
root.title('Abrir Browser')
#Tamanho da janela do sistema
root.geometry('300x200')

#Função para abrir o google
def google():
    webbrowser.open('www.google.com')

#Construção de um botão que ao ser clicado, abre o google
#pady é a posição do botão
mygoogle = Button(root, text='Abrir o google', command = google).pack(pady=20)

#Chamando a execução do sistema
root.mainloop()