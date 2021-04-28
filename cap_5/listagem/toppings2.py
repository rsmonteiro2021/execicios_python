#O código a seguir percorre uma lista de nomes de carros em um laço e procura o valor 'bmw'. Sempre que o valor for 'bmw', ele será exibido com letras
#maiusculas, e não somente a inicial maiuscula.

requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    if  requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_topping:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')
