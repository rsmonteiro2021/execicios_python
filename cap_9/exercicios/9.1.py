"""
    Restaurante: crie uma classe chamada Restaurant. O método ___init___() de Restaurant
    deve armazenar dois atributos: restaurant_name e cuisine_type. Crie um método chamadao
    describe_restaurant() que mostre essas duas informações, e um método de nome open_restaurant()
    que exiba uma mensagem informando que o restaurante está aberto.
    Crie uma instancia chamada restaurant a partir de sua classe. Mostre os dois atributos
    individualmente e, em seguida, chame os dois métodos.
"""

class Restaurant():
    """Simula um restaurante informando."""
    def __init__ (self, name, cuisine):
        """Inicializa os atributos name e cuisine."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Exibe a descrição do restaurante."""
        print("O restaurante " + self.name.title() + " é especialista na culinária " + self.cuisine.title() + ".")

    def open_restaurant(self):
        print(self.name.title() + " restaurant's encontra-se aberto!\n")

restaurant = Restaurant('Xian', 'Chinesa')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('O Braseiro', 'Brasileira')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Divina Gula', 'Mineira')
restaurant.describe_restaurant()


