# Veriricando nome de Usuários: Fa;a o seguinte para criar um programa que simule o modo como os sites garantem que todos todos
# tenham um nome de usuário único.

# Crie uma lista chamda current_users com cinco ou mais nomes de usuários:

users = ['admin', 'Admin', 'ADMIN', 'kesia', 'Kesia', 'KESIA', 
'eliene', 'Eliene', 'ELIENE', 'wolverine', 'Wolverine', 'WOLVERINE',
 'bidu', 'Bidu', 'BIDU', 'lucio', 'Lucio', 'LUCIO'
]

# Crie outra lista chamada new_users com cinco nomes de usuários. Garanta que um ou dois novos usuários também estejam na lista
# current_users.

new_users = []

# Percorra a lista new_users com um laço para ver se cada novo nome de usuário já foi usado. Em caso afirmativo, mostre uma mensagem
# infomrmando que a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi usado, apresente uma mensagem dizendo que o nome
# do usuário está disponível.


new_user = input('Digite o nome de usuário:\n')
new_users.append(new_user)

for user in new_users:
    if user in users and user in new_users:
        print('Este nome de usuário já existe, tente outro nome\n')
    else:
        print('Nome de usuário disponível\n')
        users.append(new_user)