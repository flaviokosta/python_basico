'''
Cada conta possui um cliente, saldo, um limite e tem
metodos SACAR, DEPOSITAR E CONSULTAR SALDO
'''

from cliente import Cliente

class Conta:


    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = float(saldo)
        self.limite = float(limite)

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def consultar_saldo(self):
        return self.saldo
