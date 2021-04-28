# Passando um número arbitrário de argumentos

"""
Considere uma função que prepare um a pizza. Ela deve aceitar vários ingredientes,
mas não é possível saber com antecedência quanos ingredientes uma pessoa vai
querer. A função a seguir tem um parâmetro +toppings, mas esse parâmetro agrupa
tantos argumentos quantos forem fornecidos na linha de chamada:
"""

def make_pizza(*toppings):
    """Exibe a lista de ingredientes pedidos."""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)

make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')