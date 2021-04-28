# Sem Usuários: Acrescente um teste if em hello_admin.py para garantir que a lista de usuários
# não esteja vazia.

# Se um usuário for 'admin', mostre uma saudação especial, por exemplo, Olá admin, gostaria de ver um
# relatório de status?
# Caso contrário, mostre uma saudação genérica, como Olá Éric, obrigado por fazer login novamente.

users = []
user = input('Digite o nome de usuário:\n')

if user in users:
    if user == 'admin':
        print(f'Olá {user.title()}, gostaria de visualizar o resumo de acesso da semana?')
    else:
        print(f'Olá {user.title()}, você está logado, seja bem vindo!')
else:
    print('Precisamos cadastrar alguns usuários!')
