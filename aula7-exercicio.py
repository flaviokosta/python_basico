'''
EXERCICIO
Escreva uma função que receba um objeto de coleção
e retorna o valor do maior número dentro dessa coleção.
Faça outra função que retorna o menor número dessa coleção
'''

def maior(colecao):
    maior_item = colecao[0]
    item = 1
    for item in range(len(colecao)):
        if colecao[item] > maior_item:
            maior_item = colecao[item]
    return maior_item

def menor(colecao):
    menor_item = colecao[0]
    item = 1
    for item in range(len(colecao)):
        if colecao[item] < menor_item:
            menor_item = colecao[item]
    return menor_item

minha_lista = [5, 6, 4, 10, 12, 3.5, 18]

print('Maior valor: ', maior(minha_lista))
print('Menor valor: ', menor(minha_lista))
