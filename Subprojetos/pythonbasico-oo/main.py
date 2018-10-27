from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6, 'Agrale', 10)

#print(caminhao_rosa)
#print(type(caminhao_rosa))

print('CAMINHÃO ROSA')
print('Cor:', caminhao_rosa.cor)
print('Marca:', caminhao_rosa.marca)
print('Tanque:', caminhao_rosa.tanque)
print('\n')

carro_azul = Carro('azul', 'BMW', 30)

print('CARRO AZUL - ', type(carro_azul))
print('Cor:', carro_azul.cor)
print('Marca:', carro_azul.marca)
print('Tanque:', carro_azul.tanque)

carro_azul.abastecer(10)
print('Tanque:', carro_azul.tanque)

carro_azul.abastecer(70)
print('Tanque:', carro_azul.tanque)
