# Usando uma função com um laço 'while':

def city_country(city, country):
    """Informa sobre o país em que uma dada cidade se encontra."""
    information_city = city + ', ' + country
    return information_city

# Embora a questão não solicite vou utilizar aqui um laço while

while True:
    print('\nPlease tell me a city and a country:')
    print("(Enter 'q' at any time to quit.)")     # informamos ao usuário que ele pode encerrar o programa quando
                                                      # quiser digitando a tecla 'q'.
    city = input('City: ')
    
    if city == 'q':                  # aplicamos a condição de parada
        break
    country = input('Country: ')      # como é em qualquer momento, aqui também aplicamos a mesma condição
                                          # de parada.
    if country == 'q':
        break
        
    formatted_city = city_country(city, country)
    print('\n\tformatted_city')
