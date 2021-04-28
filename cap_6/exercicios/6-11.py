# Cidades: Crie um dicionário chamado cities. Use os nomes de três cidades como chave em seu dicionário. 
# Crie um dicionário com informações sobre cada cidade e inclua o país em que a cidade está localizada,
# a população aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade devem ser
# algo como country, population e fact. Apresente o nome de cada cidade e todas as informações que você
# armazenou sobre ela.

cities = {'Maceió': {'Country': 'Brasil', 'Population': '1,2 milhões de hab', 'Fact': 'Paraíso das Águas'},
'Rio de Janeiro': {'Country': 'Brasil', 'Population': '4 milhões de hab', 'Fact': 'Cidade Maravilhosa'},
'São Paulo': {'Country': 'Brasil', 'Population': '11 milhões de hab', 'Fact': 'Terra da Garoa'}
}

for cidade, informações in cities.items():
    print(f'\nCidade: {cidade}')
    country = informações['Country']
    population = informações['Population']
    fact = informações['Fact']
    print(f'\tCountry: {country}')
    print(f'\tPopulation: {population}')
    print(f'\tFact: {fact}')
