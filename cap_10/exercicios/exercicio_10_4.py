"""Lista de Convidados: Escreva um laço while que pergunte o nome aos usuários. Quando
fornecerem seus nomes, apresente uma saudação na tela e acrescente uma linha que registre
a visita do usuário em um arquivo chamado guest_book.txt. Certifique-se de que cada
entrada esteja em uma nova linha do arquivo."""

while True:
    usuario = input('Digite o nome do usuário ou s para sair:\n')
    if usuario == 's':
        break
    else:
        print('Seja bem vindo ' + usuario + '!')
        filename = 'guest_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write(usuario + ' acessou o banco de dados!\n')
