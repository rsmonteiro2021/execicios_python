# Animais de Estimação: Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal
# de estimação. Em cada dicionário, inclua o tipo de animal e o nome do dono. Armazene esses dicionários em
# uma lista chamada 'pets'. Em seguida, percorra sua lista com um laço e, à medida que fizer isso, apresente
# tudo o que você sabe sobre cada animal de estimação.

pets = {
    'cão':{'raça': 'Dachshund',
    'nome': 'Wolverine',
    'idade': 7,
    'pelagem': 'pelo curto'},
    'cão2':{'raça': 'Shitzu',
    'nome': 'Bidu',
    'idade': 7,
    'pelagem': 'pelo longo'},
}
for pet, information in pets.items():
    print(f'\ntipo: {pet.title()}')
    raça = information['raça']
    print(f'\traça: {raça.title()}')
    nome = information['nome']
    print(f'\tnome: {nome.title()}')
    idade = information['idade']
    print(f'\tidade: {idade}')
    pelagem = information['pelagem']
    print(f'\tpelagem: {pelagem.title()}')