from car import EletricCar

my_tesla = EletricCar('tesla', 'model s', 2016)
my_tesla.describe_details()
print('\t' + my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()