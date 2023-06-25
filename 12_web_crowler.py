#Web crowler é um software usado para encontrar, ler e indexar páginas de um site. É como um robô
#que captura informações de cada um dos links que encontra pela frente, cadastra e compreende
#o que é mais relevante. Muito usado no processo de pentest


#Biblioteca para extração de dados de arquivos HTML e XML
#pip install beautifulsoup4
#pip install beautifulsoup
from bs4 import BeautifulSoup

#Biblioteca para envio de solicitações HTTP em Python
#pip install requests
import requests

#Biblioteca que exporta um conjunto de funções eficientes correspondentes aos operadores aritiméticos
#do Python como: +-*/not and
import operator

#Biblioteca que nos ajuda a preencher e manipular eficientemente as estruturas de dados de tuplas,
#discionários e listas
from collections import Counter

def start(url):
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')

    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    clean_list = []

    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/,.'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
             clean_list.append(word)
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word]+= 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))
    
    c = Counter(word_count)

    top = c.most_common(10)
    print("Top 10 palavras que mais aparecem: ", top)

if __name__ == "__main__":
    start("https://geeksforgeeks.org/python-programming-language/?ref=leftbar")

