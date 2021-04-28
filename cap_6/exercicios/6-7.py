# Pessoas: Comece com o programa que você escreveu no Exercício 6.1. Crie dois novos dicionários que
# representem pessoas diferentes e armazene os três dicionários em uma lista chamada people. Percorra
# sua lista de pessoas com um laço. À medida que percorrer a lista, apresente tudo que você sabe sobre
# cada pessoa.

information = {
    'kjoliveira':{'first_name': 'Kesia',
    'last_name': 'oliveira',
    'age': '47',
    'city': 'Maceió-Al'},
    'rsmonteiro':{'first_name': 'Roberto',
    'last_name': 'Monteiro',
    'age': '41',
    'city': 'Maceió-Al'},
    'emsantos': {'first_name': 'Eliene',
    'last_name': 'Santos',
    'age': '60',
    'city': 'União-Al'},
    'jlmonteiro': {'first_name': 'José',
    'last_name': 'Monteiro',
    'age': '64',
    'city': 'Atalaia-Al'}
}
for name, dates in information.items():
    print(f'\nuser_name: {name}')
    full_name = dates['first_name'] + ' ' + dates['last_name']
    location = dates['city']
    print(f'\tFull name: {full_name.title()}')
    print(f'\tLocation: {location.title()}')