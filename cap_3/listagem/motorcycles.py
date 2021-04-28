#Motorcycles removendo um valor (elemento) de uma lista.
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + '.')
print(motorcycles)
motorcycles.remove("Yamaha")
print(motorcycles)
