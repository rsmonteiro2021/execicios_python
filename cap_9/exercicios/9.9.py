"""
    Upgrade de bateria: User a última versão de Electric.car.py desta seção. Acrescente
    um método chamado upgrade_battery() na classe Battery. Esse método deve verificar
    a capacidade da bateria e defini-la como 85 se o valor for diferente. Crie um carro
    elétrico com uma capacidade de bateria default, chame get_range() uma vez e e, seguida
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
        self_battery = Battery()




