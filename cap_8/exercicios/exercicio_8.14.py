"""
Carros: Escreva uma função que armazene informações sobre um carro em um dicionário. A função sempre deve receber o
nome de um fabricante e um modelo. Um número de arbitrário de argumentos nomeados deverá ser aceito. Chame a função
com as informações necessárias e dois outros pares nme-valor, por exemplo, uma cor ou um opcional. Sua função deve ser
apropriada para uma chama como esta:
car = make_car('subaru', 'outback', color='blue', tow_package = True) Mostre o dicionário devolvido para garantir que todas informa
ções foram armazenadas corretamente.
"""

def make_car(car, model, **car_info):
    """Exibe informações sobre um carro."""
    car_information = {}
    car_information['car'] = name_car
    car_information['model'] = modelo
    for key, value in car_info.items():
        car_information[key] = value
    return car_information
car_list = ['Argo', 'Onix', 'Nivus']
print('Escolha entre as opções listadas abaixo:')
for car in car_list:
    print('\t -' + car)
name_car = input('Digite o nome do carro:\n')
if name_car not in car_list:
    print('Escolha apenas os que estão na lista:')
elif name_car == 'Argo' or name_car == 'argo':
    modelo = 'Fiat'
    ano = 2021
elif name_car == 'Onix' or name_car == 'onix':
    modelo = 'Chevrolet'
    ano = 2021
else:
    modelo = 'VolksWagen'
    ano = 2020
car_profile = make_car('name_car', 'modelo', year = ano)
print(car_profile)


        

