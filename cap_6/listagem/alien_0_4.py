# Um exemplo mais realista envolveria mais de tres alienígenas, com um código que gere automaticamente
# cada alienígena. No exemplo a seguir vamos usar um range() para criar uma frota de 30 alienígenas.
# informações sobre um alienigena em particular:

aliens = []                   # cria uma lista vazia para armazenar alienígenas
for number in range(30):      # cria 30 alienígenas verdes
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens:
    print(alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
for alien in aliens[:5]:
    print(alien)              # Mostra os cinco primeiros alienígenas

print('...')

print('Total number of alines: ' + str(len(aliens)))     # Mostra quantos alienigenas foram criados