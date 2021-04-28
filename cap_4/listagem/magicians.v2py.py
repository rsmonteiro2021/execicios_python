#Vamos usar um laço for para exibir cada um dos elementos de uma lista de mágicos:
magicians = ['alice', 'david', 'carolina']#...........Começamos definindo uma lista de mágicos
magicians.sort()#.....................................classifica os valores da lista por ordem alfabética crescente
for magician in magicians:#...........................Aqui definimos um laço for dentro da lista e armazena-la na variável magician
    print(magician.title() + " , that was a great trick!")#..........................Onde cada elemento deve ser mostrado
    print("I can't wait to see hour next trick, " + magician.title() + ".\n")
print('Thank you, everyone. That whas a great magic show!')
