"""
    Usuários: Crie uma classe chamada User. Crie dois atributos de nomes first_name e last_name e,
    então, crie vários outros atributos normalmente armazenados em um pefil de usuário. Escreva um
    método de nome describe_user() que apresente resumo das informações do usuário. Escreva o método
    chamado greet_user() que mostre uma saudação personalizada ao usuário.
    Crie várias instâncias que representem diferentes usuários e chame os dois métodos para cada usário.
"""

class User():
    """Tentativa de criar uma classe usuário."""
    
    def __init__(self, first_name, last_name, age, ocupation):
        """Inicia os atributos do usuário."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ocupation = ocupation

    def describe_user(self):
        """Exibe as características do usuário."""
        print('\nInformações do Usuário:\n')
        print('\tFirst Name = ' + self.first_name.title() + '\n\t' + 'Last Name: ' + self.last_name.title() + ';')
        print('\tAge: ' + str(self.age) + ';')
        print('\tOcupation: ' + self.ocupation + '.\n')
    
    def greet_user(self):
        print('Olá! seja bem vindo ' + self.first_name.title() + ' ' + self.last_name.title() + '!\n')
while True:
    print('Tecle Enter para encerrar a qualquer momento!')
    first_name = input('Digie o primeiro nome do usuário:\n')
    if first_name == '':
        break
    last_name = input('Digie o último nome do usuário:\n')
    if last_name == '':
        break
    age = int(input('Qual a idade do usuário?\n'))
    if age == '':
        break
    ocupation = input('Digite a ocupação do usuaário:\n')
    if ocupation == '':
        break
    name = User(first_name, last_name, age, ocupation)

    name.describe_user()
    name.greet_user()