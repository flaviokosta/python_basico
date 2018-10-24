'''
EXERCICIO: Faça um formulário que pergunte o nome,
CPF, enderçeo, idade, altura e telefone e
imprima isso em um relatório organizado
'''

nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')
endereco = input('Digite seu endereço: ')
idade = input('Digite sua idade: ')
altura = input('Digite sua altura: ')
telefone = input('Digite seu telefone: ')

print('Você chama-se', nome, 'e tem', idade, 'anos de idade.')
print('Sua altura é ' + str(altura) + ', seu CPF é', cpf, 'e você mora em ' + endereco + '.')
print('Ah, sim, já ia esquecendo. Seu telefone é', telefone)
print('\n')
print('Nome:\t' + nome)
print('CPF:\t' + cpf)
print('Endrço:\t' + endereco)
