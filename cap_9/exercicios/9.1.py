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
        self.number_served = 0
     
    def describe_restaurant(self):
        """Exibe a descrição do restaurante."""
        print("O restaurante " + self.name.title() + " é especialista na culinária " + self.cuisine.title() + ".")

    def open_restaurant(self):
        print(self.name.title() + " restaurant's encontra-se aberto!\n")

    def set_number_served(self):
        print("Estão sendo atendidos no momento " + str(self.number_served) + " clientes.")
    
    def increment_number(self, number):
        self.number = number
        print('No último dia de funcionamento foram atendidos ' + str(self.number) + ' clientes.')

restaurant = Restaurant('Xian', 'Chinesa')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 25
restaurant.set_number_served()
restaurant.increment_number(150)



