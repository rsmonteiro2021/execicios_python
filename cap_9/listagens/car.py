"""
    Vamos escrever um conjunto de classes usado para representar carros à gasolina e 
    elétricos.
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
        print("\tThis car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        """Define o valor de leitura do hodômetro com valor especificado."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""

    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("\tThis car has a " + str(self.battery_size) + " -kwh battery.")
    
    def get_range(self):
        """Exibe uma frase sobre a distância que o carro pode percorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = 'This car can go approximetely ' + str(range)
        message += 'miles on a full charge.'
        print('\t' + message)

class EletricCar(Car):
    """Representa aspectos de um carro específicos de veículos elétricos."""
    
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico."""
        super().__init__(make, model, year)
        self.battery = Battery()
        self.details_car = 'details_car'
    
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print('\tThis car has a ' + str(self.battery_size) + '-kwh battery.')
    
    def describe_details(self):
        """Retorna os detalhes do carro elétrico."""
        
        while True:
            disponible_color = {1: 'White', 2: 'Black', 3: 'Silver', 4: 'Red'}
            print('Escolha a cor do seu Tesla Eletric Car. \nDisponible Color:')
            for number, color in disponible_color.items():
                print('\t' + str(number) + ': ' + color + '.')
            color = int(input('Digite aqui sua cor favorita:\n'))

            if color in disponible_color:
            
                if color == 1:
                    your_car = {'Color': 'White', 'Horse Power': '80 hp', 'Torque': '14 kNm', 'Style': 'Sedan'}
                    print('Congratulations!!!!\nDetails of the your Tesla Electric Car:')
                    for value, key in your_car.items():
                        print('\t' + value + ': ' + key)
                    break
                elif color == 2:
                    your_car = {'Color': 'Black', 'Horse Power': '80 hp', 'Torque': '14 kNm', 'Style': 'Hatch'}
                    print('Congratulations!!!!\nDetails of the your Tesla Electric Car:')
                    for value, key in your_car.items():
                        print('\t' + value + ': ' + key)
                    break
                elif color == 3:
                    your_car = {'Color': 'Silver', 'Horse Power': '90 hp', 'Torque': '16 kNm', 'Style': 'SUV'}
                    print('Congratulations!!!!\nDetails of the your Tesla Electric Car:')
                    for value, key in your_car.items():
                        print('\t' + value + ': ' + key)
                    break
                else:
                    your_car = {'Color': 'Red', 'Power': '116 hp', 'Torque': '18 kNm', 'Style': 'Cupê'}
                    print('Congratulations!!!!\nDetails of the your Tesla Electric Car:')
                    for value, key in your_car.items():
                        print('\t' + value + ': ' + key)
                    break
            else:
                print('Não estamos personalizando o carro elétrico no momento!')
