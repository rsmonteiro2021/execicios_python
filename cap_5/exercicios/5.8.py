# Olá admin: Crie uma lista com cinco nomes de usuários, incluindo o nome 'admin'. Suponha que você
# esteja escrevendo  um código que exibirá uma saudação a cada usuário depois que eles fizerem login
# em um site. Percorra a lista com um laço e mostre uma saudação para cada usuário.

# Se um usuário for 'admin', mostre uma saudação especial, por exemplo, Olá admin, gostaria de ver um
# relatório de status?
# Caso contrário, mostre uma saudação genérica, como Olá Éric, obrigado por fazer login novamente.

users = ['admin', 'kesia', 'Renata',
'danieli', 'wolverine']
user = input('Digite o nome de usuário:\n')
if user in users:
    if user == 'admin':
        print(f'Olá {user.title()}, gostaria de visualizar o resumo de acesso da semana?')
    else:
        print(f'Olá {user.title()}, você está logado, seja bem vindo!')
else:
    print('Usuário não cadastrado!')
