# Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com nomes de vários sanduiches:
sandwich_orders = ['Hamburguer', 'Americano', 'Hot Dog', 'Minuano', 'Passa Carne', 'Passa Frango', 'Pastrami']

# Em seguida, crie uma lista vazia chamada finished_sandwiches.
finished_sandwiches = []

# Percorra a lista de pedidos com um laço emostre uma mesngem para cada pedido, por exemplo, 'Preparei seu
# sandwiche de atum'.
while True:
    for sandwich in sandwich_orders:
        print(f'Preparei seu {sandwich}!')
        # À medida que cada sanduíche for preparado, transfira-o para a lista de sanduíches prontos.
        finished_sandwiches.append(sandwich)
    else:
        break
# Depois que todos os sanduíches estiverem prontos, mostre uma mensagem que liste cada sanduíche preparado.
print('\nSandwiches preparados:\n')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich}')