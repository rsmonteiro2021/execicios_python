#Nomes - armazene os nomes de alguns de seus amigos em uma lista chamada names. Exiba o nome de cada pessoa acessando cada elemento da lista, um de cada vez.
list = []
x = 0
quantidade = int(input('Quantas pessoas deseja convidar? '))
while quantidade > 0:
    name = input("Qual amigo você deseja inserir a lista de convidados? ")
    list.append(name.title())
    quantidade -= 1
    x += 1
    print(f'você adicionou {list[x - 1]} a sua lista de convidados! Restam {quantidade} a convidar')
else:
    print(f'Sua lista de convidados é portanto: {list}')
    

