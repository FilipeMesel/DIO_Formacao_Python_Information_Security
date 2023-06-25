#Biblioteca que fornece diversos recursos de telefone; como informações básicas de um número de 
#telefone, validação de um número de telefone, etc.
#pip install phonenumbers
import phonenumbers

from phonenumbers import geocoder

phone = input("Digite o número de telefone no formato +551140028922: ")

phone_number = phonenumbers.parse(phone)

print("Geocoder: ", geocoder.description_for_number(phone_number, 'pt'))
