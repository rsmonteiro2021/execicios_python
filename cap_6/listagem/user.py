# Vamos criar um dicionário contendo o nome de usuário, o primeiro nome e o sobrenome de uma pessoa:
user_0 = {
    'username': 'efermmi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

catálogo = {
    'Alface': 2.50,
    'Cebola': 1.30
}
compras = []
for produto, preço in catálogo.items():
    print(produto + ': R$', str(preço))
while True:
    produto = input('Digite o produto desejado (ou s para encerrar!):\n')
    if produto == 's':
        print('Compras em encerradas!')
        print(compras)
        break
    if produto in catálogo:
        quantidade = int(input('Digite a quantidade: '))
        print(preço * quantidade)
        compras.append(produto)
    else:
        print('O produto não faz parte do catálogo!')