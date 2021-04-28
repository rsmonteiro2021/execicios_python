"""
Suponha que tenhamos uma lista de usuários e queremos exibir uma saudação a cada um.
O exemplo a seguir envia uma lista de nomes a uma função chamada greet_users(), que
saúda cada pessoa da lista individualmente.
"""
def greet_users(names):
    """Exibe uma saudação simples a cada usuário da lista."""
    msg = 'Hello, ' + name.title() + '!'
    return msg

username = []
while True:
    name = input('Digite o nome do usuário, ou tecle Enter para encerrar:\n')
    if name == '':
        print('Programa Encerrado!\n')
        break
    else:
        username.append(name)

for name in username:
    print(f'\t{greet_users(username)}')