#Ferramenta para coleta de dados de sites da web. Convertendo os dados de maneira estruturada para
#posterior análise. É uma forma de mineração de dados.

#Biblioteca para extração de dados de arquivos HTML e XML
#pip install beautifulsoup4
#pip install beautifulsoup
from bs4 import BeautifulSoup

#Biblioteca para envio de solicitações HTTP em Python
#pip install requests
import requests

#Pegando todo o conteúdo da requisição http do site especificado
site = requests.get("https://www.climatempo.com.br/").content

#Gerando um objeto para parsear o conteúdo de "site" ao formato html
#Baixando o html do site
soup = BeautifulSoup(site, 'html.parser')

#Transforma o html em string e exibe o HTML
print(soup.prettify())

#Buscando um dado específico do stie:
print(soup.title.string)



