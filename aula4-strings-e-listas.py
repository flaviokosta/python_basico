frase = 'Oi, Tudo bem?'
print(frase[::-1])
print(frase.capitalize())
print(frase.lower())
print(frase.upper())

lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego']
lista_nomes.append('Lucas')

print(lista_nomes[::1])

lista_nomes.append('Rafaela')

print(lista_nomes[::1])

lista_nomes.remove('Maria')
lista_nomes.append('João')

print(lista_nomes[::1])
print(lista_nomes.count('João'))
print(len(frase))
print(len(lista_nomes))



nome_completo = ['Flávio', 'Roberto', 'Gomes', 'Costa']
print(nome_completo)
nome_completo.insert(3, 'da')
print(nome_completo)
