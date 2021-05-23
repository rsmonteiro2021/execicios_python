"""
    Upgrade de bateria: User a última versão de Electric.car.py desta seção. Acrescente
    um método chamado upgrade_battery() na classe Battery. Esse método deve verificar
    a capacidade da bateria e defini-la como 85 se o valor for diferente. Crie um carro
    elétrico com uma capacidade de bateria default, chame get_range() uma vez e em, seguida
    chame get_ranger() uma segunda vez após fazer um upgrade da bateria. Você deverá ver
    um aumento na distância que o carro é capaz de percorrer.
"""
class car():
    """Tentativa simples de modelar um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos de um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_car(self):
        """ Retonra o nome do veículo de modo formatado."""
        long_name = str(self.year) + ', ' + self.make.title() + ', ' + self.model.title()
        return long_name

    def read_odometer(self):
        """ Exibe uma frase que mostra a milhagem do carro."""
        odometer = 'This car has a ' + str(self.odometer_reading) + ' miles on it.'
        return odometer
    
    def update_odometer(self, mileage):
        """ Define o valor de leitura do odometro do veículo."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You don't roll back an odometer.")
    
    def increment_odometer(self, miles):
        """Atualiza o valor do odômetro do veículo."""
        self.odometer_reading += miles
        return self.odometer_reading

class Battery():
    """Tentativa simples de modelar uma bateria para veículos elétrico."""

    def __init__(self, battery_size = 70):
        """Inicializa os atributos de uma bateria para carro elétrico."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Retorna uma mensagem com a capacidade da bateria."""
        message = 'This car has a ' + str(self.battery_size) + ' kwh battery.'
        return message

    def get_ranger(self):
        """Exibe uma frase acerca da distância que o carro é capaz de percorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = 'This car has a ' + str(self.battery_size) + ' kwh battery.'
        return message

    def upgrade_battery(self, battery_size = 85):
        """Exibe a capacidade da bateria."""
        self.battery_size = battery_size

class EletricCar(Car):
    """Tetantiva simples de modelar um veículo elétrico."""

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe pai. Em seguida, inicializa os atributos
        específicos de um carro elétrico."""

        super().__init__(make, model, year):
        self.battery = Battery()
        self.details_car = 'details_car'
    
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + " -kwh battery.")

    def describe_details(self):
        """Retorna detalhes do carro elétrico."""

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

"""my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
"""
my_tesla = EletricCar("tesla", "model's", 2022)
my_tesla.describe_details()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print('\t' + my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
print('\t' + my_tesla.get_descriptive_name())




