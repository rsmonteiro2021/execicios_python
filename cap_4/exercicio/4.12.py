#Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços for para fazer exibições a fim de economizar espaço. Escolha uma versão de
#foods.py e escreva dois laços for para exibir cada ista de comidas. 

#Resposta:

pizzas = ['Marguerita', 'Cartola', 'Portuguesa', 'Napolitana']
friend_pizzas = pizzas [:]
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
pizzas.append('Carne do Sol')
friend_pizzas.append('Frango com Catupiry')
print('Esses são meus sabores de pizzas favoritos:')
print(pizzas)
print('Esses são os sabores de pizzas favoritos do meu amigo:')
print(friend_pizzas)
