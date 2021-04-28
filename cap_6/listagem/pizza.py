# Igredientes de pizza
# armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Resumo do pedido
print('You ordered a ' + pizza['crust'] + ' crust pizza ' + 'with the follwing toppings:')

for topping in pizza['toppings']:
    print('\t' + topping)                   