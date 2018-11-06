'''EXERCICIO

Crie um software de gerenciamento bancário.
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf e idade
Cada conta possui um cliente, saldo, um limite e tem 
metodos SACAR, DEPOSITAR E CONSULTAR SALDO
'''
from cliente import Cliente
from conta import Conta

def imprimir_menu():
    print('Software de Gerenciamento Bancário')
    print('----------------------------------\n')
    print('1 - Cadastrar cliente')
    print('2 - Criar conta bancária')
    print('3 - Listar clientes cadastrados')
    print('4 - Mostrar Saldo da Conta')
    print('5 - Depositar dinheiro')
    print('6 - Sacar dinheiro')
    print('9 - Sair')
    escolha = input('Escolha opção: ')
    return escolha

numero_cliente = 0
num_conta = 0
cliente = []
conta = []
opcao = imprimir_menu()

while opcao != '9':
    if opcao == '1':
        nome_cliente = input('Digite o nome do cliente: ')
        cpf_cliente = input('Digite CPF do cliente: ')
        idade_cliente = input('Digite idade do cliente: ')
        cliente.append(Cliente(nome_cliente, cpf_cliente, int(idade_cliente)))
        numero_cliente += 1
        print('-----------------------------')
        print('CLIENTE CADASTRADO')
        print('Cliente: ', nome_cliente)
        print('Idade: ', idade_cliente, '- CPF:', cpf_cliente)
        print('-----------------------------\n')
    elif opcao == '2':
        print('-----------------------------')
        print('Quantidade de clientes cadastrados: ', numero_cliente)
        for i in range(numero_cliente):
            print('Cliente ' + str(i + 1) + ': ' + cliente[i].nome)
        print('-----------------------------')
        este_cliente = int(input('Criação de conta. Escolha o número do cliente: '))
        limite_cliente = float(input('Limite de crédito para cliente: '))
        conta.append(Conta(cliente[este_cliente - 1], 0, limite_cliente))
        print('Foi criada uma conta para o cliente ', conta[num_conta].cliente.nome)
        print('Saldo: ', conta[num_conta].saldo, ' - Limite: ', conta[num_conta].limite)
        num_conta += 1
    elif opcao == '3':
        print('-----------------------------')
        print('Quantidade de clientes cadastrados: ', numero_cliente)
        for i in range(numero_cliente):
            print('Cliente ' + str(i+1) + ': ' + cliente[i].nome)
        print('-----------------------------')
    elif opcao == '4':
        print('-----------------------------')
        print('Quantidade de contas cadastradas: ', num_conta)
        for i in range(num_conta):
            print(str(i + 1) + '- Conta do Cliente ' + cliente[i].nome)
        print('-----------------------------')
        esta_conta = int(input('Escolha o número da conta: ')) - 1
        print('Saldo: R$', conta[esta_conta].saldo, 'Limite: R$', conta[esta_conta].limite)
        print('Saldo total: R$', (conta[esta_conta].saldo + conta[esta_conta].limite))
    elif opcao == '5':
        print('-----------------------------')
        print('Quantidade de contas cadastradas: ', num_conta)
        for i in range(num_conta):
            print(str(i+1) + '- Conta do Cliente ' + cliente[i].nome)
        print('-----------------------------')
        esta_conta = int(input('Escolha o número da conta: '))-1
        valor = float(input('Digite o valor a depositar:'))
        conta[esta_conta].depositar(valor)
        print('Depósito efetuado com sucesso')
        print('Saldo: R$', conta[esta_conta].consultar_saldo(), 'Limite: R$', conta[esta_conta].limite)
        print('Saldo total: R$', (conta[esta_conta].consultar_saldo() + conta[esta_conta].limite))
    elif opcao == '6':
        print('-----------------------------')
        print('Quantidade de contas cadastradas: ', num_conta)
        for i in range(num_conta):
            print(str(i+1) + '- Conta do Cliente ' + cliente[i].nome)
        print('-----------------------------')
        esta_conta = int(input('Escolha o número da conta: '))-1
        valor = float(input('Digite o valor a sacar:'))
        if valor <= (conta[esta_conta].consultar_saldo() + conta[esta_conta].limite):
            conta[esta_conta].sacar(valor)
            if conta[esta_conta].saldo < 0:
                print('Conta com saldo negativo!!!')
            print('Saque efetuado com sucesso')
        else:
            print('Insuficiência de fundos!!')
        print('Saldo: R$', conta[esta_conta].consultar_saldo(), 'Limite: R$', conta[esta_conta].limite)
        print('Saldo total: R$', (conta[esta_conta].consultar_saldo() + conta[esta_conta].limite))
    else:
        print('-----------------------------')
        print('Opção errada!!')
        print('-----------------------------')
    opcao = imprimir_menu()
