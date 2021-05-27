from user_admin import User, Privileges, Admin

first_name = input('Digite o primeiro nome do usuário:\n')
last_name = input('Digite o último nome do usuário:\n')
full_name = first_name.title() + " " + last_name.title()
usuarios = ['Roberto Monteiro', 'Kesia Jacqueline']
usuario = User(first_name.title(), last_name.title(), 1)
usuario_admin = Admin(first_name.title(), last_name.title(), 1)

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
                print(full_name.title() + ' não está cadastrado.')
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
                print(full_name.title() + ' não está cadastrado.')
                usuario.reset_login_attempts(0)
                print('Você deve esperar alguns minutos para tentar logar novamente!')
