# Lugares Favoritos: Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chaves
# do dicionário, e armazene de um a três lugares favoritos para cada pessoa. Para deixar este exercício mais
# interessante, peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o dicionário com
# um laço e apresente o nome de cada pessoa e seus lugares favoritos.

favorite_places = {
    'Kesia':{'first place': 'Ipojuca/PE',
    'second place': 'Gramado/RS',
    'third place': 'Rio de Janeiro/RJ'},
    'Roberto': {'first place': 'Garanhuns/PE',
    'second place': 'Recife/PE',
    'third place': 'João Pessoa/PB'},
    'Lucio':{'first place': 'Maceió/AL',
    'second place': 'Atalaia/AL',
    'third place': 'Aracajú/SE'},
}
print('Lugares Favoritos:')
for name, location in favorite_places.items():
    print(f'\nNome: {name.title()}')
    lugar_1 = location['first place']
    print(f'\tPrimeiro Lugar: {lugar_1.title()}')
    lugar_2 = location['second place']
    print(f'\tSegundo Lugar: {lugar_2.title()}')
    lugar_3 = location['third place']
    print(f'\tTerceiro Lugar: {lugar_3.title()}')