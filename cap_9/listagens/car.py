"""
    Vamos escrever uma nova classe que represente um carro. Nossa classe armazenará informações
    sobre o tipo de carro com que estamos trabalhando e terá um método que sintetiza essa informação.
"""

class Car():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem os carros."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante ."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro """
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com valor especificado."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()