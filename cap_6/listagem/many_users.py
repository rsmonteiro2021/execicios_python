# Armazenaremos informações sobre usuários - primeiro nome, sobrenome e localidade.
# As informações serão acessadas percorrendo os nomes dos usuários em um laço for e
# o dicionário de informações associado a cada nome de usuário.


users = {
    'aeinstein': {'first name': 'albert', 'last name': 'einstein', 'location': 'princeton'},
    'mcurie': {'first name': 'marie', 'last name': 'curie', 'location': 'paris',},}

# Perorrendo as chaves de um docionário através do laço for:

for username, user_infor in users.items():
    print(f'\nUsername: {username}')
    full_name = user_infor['first name'] + ' ' + user_infor['last name']
    location = user_infor['location']
    print(f'\tFull name: {full_name.title()}')
    print(f'\tLocation: {location.title()}')
    
        
