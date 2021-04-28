# Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com nomes de vários sanduiches:
# garanta que que o sanduiche pastrami apareça pelo menos três vezes.
sandwich_orders = ['Hamburguer', 'Pastrami', 'Hot Dog', 'Minuano', 'Pastrami', 'Passa Frango', 'Pastrami']
# Acrescente um código próximo ao início de seu programa para exibir uma mensagem informando que a lanchonete
# está sem patrami e, então, use um laço while para remover todas as ocorrências de pastrami em sandwich_orders.
print('\nDesculpe, gostaríamos de informar que estamos sem Pastrami!')
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
    # Garanta que nenhum sanduiche de pastrami acabe em finished_sandwiches.
    if 'Pastrami' not in sandwich_orders:
        break
print('Mas você ainda pode escolher entre os seguintes sanduíches:')
for sandwich in sandwich_orders:
    print(f'\t{sandwich}')

# Em seguida, crie uma lista vazia chamada finished_sandwiches.
finished_sandwiches = []

# Percorra a lista de pedidos com um laço e mostre uma mesngem para cada pedido, por exemplo, 'Preparei seu
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