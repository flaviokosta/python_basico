'''
EXERCICIO
Escreva uma função que receba um objeto de coleção
e retorna o valor do maior número dentro dessa coleção.
Faça outra função que retorna o menor número dessa coleção
'''

def maior_valor(colecao):
    maior = colecao[0]
    item = 1
    for item in range(len(colecao)):
        if colecao[item] > maior:
            maior = colecao[item]
    return maior

def menor_valor(colecao):
    menor = colecao[0]
    item = 1
    for item in range(len(colecao)):
        if colecao[item] < menor:
            menor = colecao[item]
    return menor

minha_lista = [5, 6, 4, 10, 12, 3.5, 18]

print('Maior valor: ', maior_valor(minha_lista))
print('Menor valor: ', menor_valor(minha_lista))
