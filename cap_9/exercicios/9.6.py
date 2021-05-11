"""
    Uma sorveteria é um tipo de específico de restaurante. Escreva uma classe chamada 
    IceCreamStand que herde da classe Restaurant escrita no Exercício 9.1 (página 232).
    Qualquer versão da classe funcionará; basta escolher aquela de que você mais gosta.
    Adicione o atributo flavors que armazene uma lista de sabores de sorvete. Escreva um
    método para mostrar esses sabores. Crie uma instância de IceCreamStand e chama esse
    método.
"""

class Restaurant():
    """Simula um restaurante informando."""
    def __init__(self, name, cuisine):
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

class IceCreamStand(Restaurant):
    """Tentativa simples de modelar uma sorveteria dentro da classe Restaurant."""
    def __init__(self, name, cuisine):
        """Inicializa os atributos da classe Pai - Restaurant. Em seguida inicia
        os atributos de IceCreamStand."""

        super().__init__(name, cuisine)
        self.flavors = 'flavors'

    def show_flavors(self):
        """Exibe os sabores de sorvetes disponíveis."""
        flavors = ['chocolate', 'morango', 'baunilha', 'cramberrie']
        print('Os sabores de sorvete disponíveis são:')
        for sabor in flavors:
            print('\t' + sabor)

restaurant = Restaurant('Xian', 'Chinesa')
restaurant = IceCreamStand('Xian', 'Chinesa')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 25
restaurant.set_number_served()
restaurant.increment_number(150)
restaurant.show_flavors()