"""
    Exercício 9.8 para ser importado no Exercício 9.11.
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