""" Importando uma função
"""
""""
    Considere o arquivo pizza_v3.py criado
    Essa função aceita um tamanho para a pizza além de permitir que sejam escritos os 
    ingredientes.
    Criamos agora um arquivo no mesmo diretório chamado making_pizza.py. Este arquivo 
    importa a função criada em pizza_v3.py.
    Observe que existem duas maneiras de importar a função.
"""
import pizza_v3
"""
    Desse modo importamos todos os módulos da função pizza_v3.py
"""
pizza_v3.make_pizza(16, 'pepperoni')
pizza_v3.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Outra forma de importar a função make_pizza() pode ser chamando o módulo específico:
# from nome_do_módulo import nome_da_função
"""
from pizza_v3 import make_pizza
"""
# e para que seja exibido o mesmo resultado bastas escrever mais duas linhas de código:

""" 
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""