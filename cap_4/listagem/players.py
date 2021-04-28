#Trabalhando com parte de uma lista. Fatiando uma lista.O exemplo a seguir envolve uma lista de jogadores de um time.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4]) #inicia a liste em martina e conclui em florence)
print(players[:4]) #se omitido o índice de início da lista, será exibido desde o início
print(players[2:])
print(players[-3:]) #exibe os tres ultimos jogadores da lista

print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())
