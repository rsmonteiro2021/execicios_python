import car

my_beetle = car.Car('Volkswagem', 'beetle', 2016)
print('\t-' + my_beetle.get_descriptive_name())

my_tesla = car.EletricCar('tesla', 'roadster', 2016)
print('\t-' + my_tesla.get_descriptive_name())