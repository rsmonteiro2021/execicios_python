#O código a seguir percorre uma lista de nomes de carros em um laço e procura o valor 'bmw'. Sempre que o valor for 'bmw', ele será exibido com letras
#maiusculas, e não somente a inicial maiuscula.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
