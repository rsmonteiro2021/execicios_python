# Números Favoritos: Modifique o seu programa do Exercício 6.2 para que cada pessoa possa ter mais de um
# número favorito. Em seguida, apresente o nome de cada pessoa, juntamente com seus números favoritos.

favorite_number = {'name': {'primeiro número': 'number_1','segundo número': 'number_2', 'terceiro número': 'number_3'}}
while True:
    name = input('Digite o nome da pessoa:\n')
    if name == 'sair':
        print('Programa Encerrado')
        break
    else:
        for name, number in favorite_number.items():
            favorite_number.update('name')
            number_1 = int(input('Digite o primeiro número favorito:\n'))
            number.update(number_1)
            number_2 = int(input('Digite o segundo número favorito:\n'))
            number.update(number_2)
            number_3 = int(input('Digite o terceiro número favorito:\n'))
            number.update(number_3)

for name, number in favorite_number.items():
    print(f'\nNome: {name}')
    numero_1 = number['primeiro número']
    numero_2 = number['segundo número']
    numero_3 = number['terceiro número']
    print(f'\tprimeiro número: {numero_1}')
    print(f'\tsegundo número: {numero_2}')
    print(f'\tterceiro número: {numero_3}')