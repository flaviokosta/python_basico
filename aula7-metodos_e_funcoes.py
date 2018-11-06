def soma(numero1, numero2):
    resposta = numero1 + numero2
    return resposta

def imprime_oi():
    print('Oi')

def tem_sete_itens(objeto):
    return (len(objeto) == 7)

print(soma(12, 15))
print(soma('um', 'dois'))
print(soma(12.35, 75.6))
for i in range(10):
    imprime_oi()

print(tem_sete_itens('asdfgsh'))