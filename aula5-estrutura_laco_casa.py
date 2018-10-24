nome = 'Flávio Roberto Gomes da Costa'
'''posicao = 0
passo = 1
for letra in nome:
    espaco = ''
    for i in range(posicao):
        espaco += '  '
    print(espaco + letra)
    posicao += passo
    if posicao > (float(len(nome)) / 2):
        passo = -1
'''
'''
i = 0
while i < 10:
    print('Ainda é menor: ', i)
    i += 1
print('Acabou o While. Valor do índice: ', i)
'''

lista_frutas = ['maçã', 'pera', 'uva', 'abacaxi', 'goiaba', 'melancia']

contador = 0

for fruta in lista_frutas:
    contador += 1

print(contador)