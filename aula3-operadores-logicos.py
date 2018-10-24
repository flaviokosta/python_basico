var_verdade = True
var_falso = False

#print(type(var_verdade), type(var_falso))
#print(var_falso)

# Comparações: == != > < >= <=
# Lógicos: and  or  not

print('Menu:\n1 = Escreve Guilherme\n2 = Escreve Lucas\n3 = Escreve Rafaela\n')

opcao = input('Escolha uma opção: ')

if opcao == '1':
    print('Guilherme')
elif opcao == '2':
    print('Lucas')
elif opcao == '3':
    print('Rafaela')
else:
    print('Opção inválida')

#numero = float(input('Digite um número maior que cinco: '))

'''
if numero > 5:
    print('Você seguiu o comando corretamente')
    print('Fim!!')
else:
    print('Você não seguiu as ordens!!')
'''