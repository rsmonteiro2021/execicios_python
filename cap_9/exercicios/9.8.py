"""
    Privilégios: Escreva uma classe Privileges() separada. A classe deve ter um atributo
    privileges que armazene uma lista de string conforme conforme descrita no exercício 9.7
    Transfira o método show_privileges() para essa classe. Crie uma instância de Privileges
    como um atributo da classe Admin. Crie uma nova instância de Admin e use seu método para
    exibir os privilégios.
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

class Privileges():
    """Tentativa de modelar os privilégios de um usuário administrador."""
    def __init__(self, privileges='You are Admin and can add post, delete post and ban user'):
        """Inicializa os atributos dos usuários administradores."""
        self.privileges = privileges
    
    def show_privileges(self):
        while True:
            user_admin = input('Tem permissão de administrador (s/n)?\n')
            if user_admin == 'n':
                print('usuario sem privilégios de administrador!')
                break
            elif user_admin == 's':
                print(self.privileges)
                break
            else:
                print('Opção não válida, digite s ou n.')

class Admin(User):
    """Tentativa simples de modelar um usuário com perfil de administrador."""

    def __init__(self, first_name, last_name, login_attempts):
        """Inicializa os atributos da classe User, em seguida inicializa os atributos
        da classe Admin"""
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = Privileges()


first_name = input('Digite o primeiro nome do usuário:\n')
last_name = input('Digite o último nome do usuário:\n')
full_name = first_name + " " + last_name
usuarios = ['Roberto Monteiro', 'Kesia Jacqueline']
usuario = User(first_name, last_name, 1)
usuario_admin = Admin(first_name, last_name, 1)

if full_name in usuarios:
    print('Informações do Usuário:')
    usuario.describe_user()
    print('Menagem de boas vindas:')
    print(usuario.greet_user())
    usuario.increment_login_attempts(1)
    usuario_admin.privileges.show_privileges()
else:
    print('Usuário não cadastrado. Você tem mais 3 tentaiva!')
    while usuario.login_attempts > 0 and usuario.login_attempts <= 3:
        first_name = input('Digite o primeiro nome do usuário:\n')
        last_name = input('Digite o último nome do usuário:\n')
        full_name = first_name + " " + last_name
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
                print('Você deve esperar alguns minutos para tentar logar novamente!')
