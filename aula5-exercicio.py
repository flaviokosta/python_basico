'''
EXERCICIO
Faça um programa que leia a quantidade de pessoas que serão convidadas
para uma festa.
Após isso, o programa irá perguntar o nome de todas as pessoas e colocar
numa lista de convidados.
Após isso, irá imprimir todos os nomes da lista
'''

print('/...............::::...............\\')
print('|   Programinha de Festinhas 1.0   |')
print('\...............::::.............../\n')

quantidade = int(input('Quantidade de convidados: '))

convidado = 1
lista_convidados = []

while convidado <= quantidade:
    lista_convidados.append(input('Nome do convidado # ' + str(convidado) + ': '))
    convidado += 1

print('\n-- LISTA DE CONVIDADOS --')
print('Quantidade de convidados:', quantidade)
print('\n')
for i in range(quantidade):
    print('Convidado', (i+1), '-', lista_convidados[i])
