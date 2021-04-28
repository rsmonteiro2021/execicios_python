#Vamos usar um laço for para exibir cada um dos elementos de uma lista de mágicos:
magicians = ['alice', 'david', 'carolina']#...........Começamos definindo uma lista de mágicos
magicians.sort()#.....................................classifica os valores da lista por ordem alfabética crescente
for magician in magicians:#...........................Aqui definimos um laço for dentro da lista e armazena-la na variável magician
    excluir = input('Quem você deseja excluir da lista de mágicos? ')
    if excluir == 'e' or excluir == 'E':
        print(magicians)
        break
    elif excluir == magician:
        magicians.remove(excluir)
        print(magician)#..........................Onde cada elemento deve ser mostrado
    else:
        print('Digite um nome presente na lista.')
