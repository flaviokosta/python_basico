'''
EXERCICIO
Faça um programa que leia a quantidade de pessoas que serão convidadas
para uma festa.
Após isso, o programa irá perguntar o nome de todas as pessoas e colocar
numa lista de convidados.
Após isso, irá imprimir todos os nomes da lista
'''

quantidade = int(input('Quantidade de convidados: '))

convidado = 0
lista_convidados = []

while convidado < quantidade:
    lista_convidados.append(input('Nome do convidado número ' + str(convidado + 1) + ': '))
    convidado += 1

for i in range(quantidade):
    print('Convidado', (i+1), '-', lista_convidados[i])
