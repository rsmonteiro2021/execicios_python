# Números Favoritos: Modifique o seu programa do Exercício 6.2 para que cada pessoa possa ter mais de um
# número favorito. Em seguida, apresente o nome de cada pessoa, juntamente com seus números favoritos.

favorite_number = {
    'Kesia': {'primeiro número': 2,
    'segundo número': 7,
    'terceiro número': 79,},
    'Roberto': {'primeiro número': 4,
    'segundo número': 14,
    'terceiro número': 158,},
    'Lucio': {'primeiro número': 45,
    'segundo número': 17,
    'terceiro número': 56,},
    'Eliene': {'primeiro número': 60,
    'segundo número': 88,
    'terceiro número': 56,},
    'Renata': {'primeiro número': 88,
    'segundo número': 79,
    'terceiro número': 60,}
}
for name, number in favorite_number.items():
    print(f'\nNome: {name}')
    numero_1 = number['primeiro número']
    numero_2 = number['segundo número']
    numero_3 = number['terceiro número']
    print(f'\tprimeiro número: {numero_1}')
    print(f'\tsegundo número: {numero_2}')
    print(f'\tterceiro número: {numero_3}')