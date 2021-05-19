"""
    Tentativas de Login: Acrescente um atibuto chamado login_attempts à sua classe User
    do Exercício 9.3 (página 226). Escreva um método chamado increment_login_attempts()
    que incremente o valor de login_attempts em 1. Escreva outro método chamado
    reset_login_attempts() que reinicie o valor de login_attempts com O.
"""
"""
    Crie uma instância da classe User e chame increment_login_attempts() várias vezes.
    Exiba o valor de login_attempts para garantir que ele foi incrementado de forma apropriada
    e, em seguida, chame reset_login_attempts(). Exiba login_attempts novamente para garantir
    que seu valor foi reiniciado com O.
"""
# Relembrando o exercício 9.3

"""
    Usuários: Crie uma classe chamada User. Crie dois atributos de nomes first_name e last_name e,
    então, crie vários outros atributos normalmente armazenados em um perfil de usuário. Escreva
    um método de nome describe_user() que apresente um resumo das informações do usuário. Escreva
    Escreva outro método chamado greet_user() que mostre uma saudação personalizada ao usuário.
    Crie várias instâncias que representem diferentes usuários e chame os dois métodos para cada
    usuário.
"""

class User():
    """Tentativa simples de descrever um usuário."""
    def __init__(self, first_name, last_name, login_attempts):
        """Inicia os atributos do usuário."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        """Exibe os atributos do usuário."""
        description = {'First name': self.first_name.title(), 'Last name': self.last_name.title(),'Login_Attempts': str(self.login_attempts)}
        for value, key in description.items():
            print(value + ': ' + key)
    
    def greet_user(self):
        """Retorna uma saudação personalizada"""
        saudacao = '\tOlá, Sr(a) ' + self.first_name.title() + ' ' + self.last_name.title() + '!\n' + '\tSeja bem vindo(a)!'
        return saudacao

    def increment_login_attempts(self, login):
        self.login_attempts += login

    def reset_login_attempts(self, login):
        self.login_attempts = login

first_name = input('Digite o primeiro nome do usuário:\n')
last_name = input('Digite o último nome do usuário:\n')
full_name = first_name.title() + " " + last_name.title()
usuarios = ['Roberto Monteiro', 'Kesia Jacquline']
usuario = User(first_name, last_name, 1)
if full_name in usuarios:
    print('Informações do Usuário:')
    usuario.describe_user()
    print('Menagem de boas vindas:')
    print(usuario.greet_user())
    usuario.increment_login_attempts(1)
else:
    print('Usuário não cadastrado. Você tem mais 3 tentaiva!')
    while usuario.login_attempts > 0 and usuario.login_attempts <= 3:
        first_name = input('Digite o primeiro nome do usuário:\n')
        last_name = input('Digite o último nome do usuário:\n')
        full_name = first_name.title() + " " + last_name.title()
        usuario = User(first_name, last_name, usuario.login_attempts)
        if usuario.login_attempts > 0 and usuario.login_attempts < 3:
            if full_name in usuarios:
                print('Informações do Usuário:')
                usuario.describe_user()
                print('Menagem de boas vindas:')
                print(usuario.greet_user())
                usuario.increment_login_attempts(1)
                break
            else:
                print('Informações do Usuário:')
                usuario.describe_user()
                print(full_name + ' não está cadastrado.')
                usuario.increment_login_attempts(1)
        else:
            if full_name in usuarios:
                print('Informações do Usuário:')
                usuario.describe_user()
                print('Menagem de boas vindas:')
                print(usuario.greet_user())
                usuario.increment_login_attempts(1)
                break
            else:
                print('Informações do Usuário:')
                usuario.describe_user()
                print(full_name + ' não está cadastrado.')
                usuario.reset_login_attempts(0)
                print('\t- Você Excedeu o número de tentativas de login.\n\t- Espere alguns minutos para tentar logar novamente!')