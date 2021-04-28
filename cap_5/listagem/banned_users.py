#O código a seguir percorre uma lista de nomes de usuários e verifica se foi banida ou não.

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
        print(user.title() + " , can post a response if you wish!")
