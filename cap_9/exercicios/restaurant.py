"""
    Exercício 9.6 para ser utilizado no Exercício 9.10.
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