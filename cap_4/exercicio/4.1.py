#Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os nomes dessas pizzas e, então, utilize o nome de cada pizza.
pizzas = ['Marguerita', 'Cartola', 'Portuguesa', 'Napolitana']
pizzas.sort()
for pizza in pizzas:
    print(f'{pizza} está entre os meus sabores de pizza favorita')
    if pizza == 'Marguerita':
        print('Constituída por mangericão, bastante tomate, mussarela e parmesão.' + '\n')
    elif pizza == 'Cartola':
        print('Constituída por banana, bastante queijo, canela e açúcar.'  + '\n')
    elif pizza == 'Portuguesa':
        print('Constituída por Ovos, tomate, bastante cebola, milho verde e mussarela.' + '\n')
    elif pizza == 'Napolitana':
         print('Constituída por muito Queijo Parmesão e tomate.' + '\n')
    else:
        print('Esse sabor não está no cardápio!')
print('Eu realmente amo pizza!')
