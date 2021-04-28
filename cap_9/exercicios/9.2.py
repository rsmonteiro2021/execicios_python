"""
    Comece com a classe do Exercício 9.1. Crie três instâncias diferentes da classe
    chame describe_restaurant() para cada instância.
"""
class Restaurant():
    """Tentativa de Simular um restaurant."""
    def __init__ (self, name, cuisine):
        """Inicializa os atributos name e cuisine."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """ Exibe a descrição do restaurante."""
        print("O restaurante " + self.name.title() + " é especialista na culinária " + self.cuisine.title() + ".")

restaurantes = ['massarela', 'xian', 'chefranco']

while len(restaurantes) > 0:
    print('Escolha o restaurante na lista abaixo:')
    for restaurante in restaurantes:
        print(f'\t-{restaurante.title()}\n')
        
    restaurant = input("Digite o nome do restaurante:\n")

    if restaurant == '':
        break

    elif restaurant not in restaurantes:
        print('O restaurante escolhido não encontra-se em nossa lista!')
        continue

    elif restaurant == 'massarela':
        restaurant = Restaurant(restaurant, 'italiana')
        restaurant.describe_restaurant()
        restaurantes.remove('massarela')
             
    elif restaurant == 'xian':
        restaurant = Restaurant(restaurant, 'chinesa')
        restaurant.describe_restaurant()
        restaurantes.remove('xian')
  
    elif restaurant == 'chefranco':
        restaurant = Restaurant(restaurant, 'japonesa')
        restaurant.describe_restaurant()
        restaurantes.remove('chefranco')