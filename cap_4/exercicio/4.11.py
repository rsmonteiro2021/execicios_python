#Minhas Pizzas: Comece com seu programa do Exercício 4.1. (página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizza. Então faça o seguinte:
#1 Adicione uma nova pizza à lista original.
#2 Adicione uma pizza diferente à lista friend_pizzas.
#3 Prove que você tem duas listas diferentes: Exiba a mensagem: Minhas pizzas favoritas são:; em seguida, utilize um laço for para exibir a segunda lista.
#Certifique-se de que cada pizza nova esteja armazenada na lista apropriada. 

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
