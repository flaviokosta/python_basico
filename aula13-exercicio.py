'''
Faça um programa que faça uma pesquisa "parametro s"
'''
import requests
import json

requisicao = None
filme = None
lista_filme = None

texto = input('Digite o termo para busca: ')

requisicao = requests.get('http://www.omdbapi.com/?s=' + texto + '&page=1&type=movie')

filme = json.loads(requisicao.text)

print(requisicao.text)

lista_filme = filme['Search']

print(len(lista_filme))

for film in lista_filme:
    print(film['Title'])

#print(filme['Error'])
