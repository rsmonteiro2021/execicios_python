"""Enquete sobre programação:
Escreva um laço while que pergunte às pessoas por que elas gostam de programação. Sempre que
alguem fornecer um motivo, acrescente-o em um arquivo e armazene todas as respostas."""

while True:
    usuario = input('Qual o seu nome (ou digite Enter para sair)?\n')
    
    if usuario == '':
        break
    else:
        print('Seja bem vindo(a) ' + usuario + '!')
        
        idade = int(input('Digite a sua idade: \n'))
        enquete = input('Por que você gosta de programação?\n')
        
        filename = 'enquete.txt'
        with open(filename, 'a') as file_object:
            file_object.write('Usuário: ' + usuario + '\n')
            file_object.write('Idade: ' + str(idade) + '\n')
            file_object.write('Resposta: ' + enquete + '\n')
        
