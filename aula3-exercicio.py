'''
EXERCÍCIO:
Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a ser do Exercito
Para entrar no exercito é preciso ter
mais de 18 anos,
pesar mais ou igual a 60 kilos e
medir mais ou igual a 1,70 metros
'''

idade = int(input('Escreva a sua idade: '))
peso = float(input('Escreva o seu peso (kg): '))
altura = float(input('Escreva a sua altura (m): '))

if (idade >= 18) and (peso >= 60) and (altura >= 1.70):
    print('\nVocê está apto a servir o Exército')
elif idade <= 18:
    print('\nVocê NÃO está apto a ser do Exército. Motivo:')
    print('Idade não é suficiente.')
elif peso < 60:
    print('\nVocê NÃO está apto a ser do Exército. Motivo:')
    print('Abaixo do peso.')
elif altura < 1.70:
    print('\nVocê NÃO está apto a ser do Exército. Motivo:')
    print('Abaixo da altura mínima.')
else:
    print('Parâmetros inválidos')

