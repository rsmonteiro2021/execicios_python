# Misturando argumentos posicionais e arbitrário

"""
Considere uma função que prepare um a pizza. Ela deve aceitar vários ingredientes,
mas não é possível saber com antecedência quanos ingredientes uma pessoa vai
querer. A função a seguir tem um parâmetro +toppings, mas esse parâmetro agrupa
tantos argumentos quantos forem fornecidos na linha de chamada:
"""
# Essa função aceita um tamanho para a pizza além de permitir que sejam escritos os ingredientes:

def make_pizza(size, *toppings):
    """Apresenta uma pizza que estamos prestes a preparar."""
    print('\nMaking a ' + str(size) + ' -inch pizza with the following topping:')
    for topping in toppings:
        print('- ' + topping)

make_pizza(16, 'peperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')