# Cidades - Escreva uma função chamada describe_city() que aceite o nome de uma cidade e seu país. A função
# deve exibir uma frase simples, como Reykjavik está localizada na Islândia. Forneça um valor default ao
# parâmetro que representa o país. Chame sua função para três cidades diferentes em que pelo menos uma
# delas não esteja no país default.

def describe_city(city, country = 'Brasil'):
    """Exibe informções de localização de uma cidade"""
    print(f'{city} está localizada no(a) {country}!')

describe_city(
    'Alagoas'
)
describe_city(
    'São Paulo'
)
describe_city(
    city = 'Philadefia', country = 'Estados Unidos da América'
)

