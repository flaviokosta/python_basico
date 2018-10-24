minha_lista = ['Flávio', 'João', 'Gui', 'João', 'Gui']    #LISTA (list)
minha_tupla = ('Gui', 'João')       #TUPLA (tuple)
meu_dicionario = {'nome': 'Flávio', 'idade':40, 'altura': 1.80}   # DICIONARIO (dict)
meu_conjunto = {'Gui', 'João', 'Flávio', 'João', 'Gui'} # CONJUNTO (set)
#print(minha_tupla, '-', type(minha_tupla))
#print(minha_lista)
#print(meu_conjunto)

#minha_tupla = ('Gui', 'Lucas')
#print(minha_tupla, '-', type(minha_tupla))

'''
print(len(meu_dicionario))
if 'Flávio' in meu_dicionario.values():
    print('Flávio está lá')
for valores in meu_dicionario.values():
    print(valores)

meu_dicionario['endereco'] = 'Av Rosa e Silva'
meu_dicionario['telefone'] = '99965-0012'

print(meu_dicionario)
for valores in meu_dicionario.values():
    print(valores)

meu_dicionario.pop('telefone')
print(meu_dicionario)
'''

print(meu_conjunto)
meu_conjunto.add('Alector')
meu_conjunto.add('Verônica')
meu_conjunto.add('André')
meu_conjunto.add('Charlezon')
print(meu_conjunto)

loucura = [(1,2), (3,4), (5,6), ({'João', 'Gabriel'},{'João', 'Eduardo'})]
print(loucura)
loucura.clear()
print(loucura)
