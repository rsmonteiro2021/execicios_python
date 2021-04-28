#O código a seguir percorre uma lista de nomes de carros em um laço e procura o valor 'bmw'. Sempre que o valor for 'bmw', ele será exibido com letras
#maiusculas, e não somente a inicial maiuscula.

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print('\nFinished making your pizza!')
