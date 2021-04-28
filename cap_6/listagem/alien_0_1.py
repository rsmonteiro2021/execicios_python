# Considere um jogo com alienígenas que possam ter cores e valores de pontuação diferentes. O dicionário simples a seguir armazena
# informações sobre um alienigena em particular:

# Começando com um dicionário vazio:

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print('Você acertou o alien ' + alien_0['color'] + ' na posição ' + 'x: ' + str(alien_0['x_position']) + ' y: ' + str(alien_0['y_position']) + '.')
print('Você marcou ' + str(alien_0['points']) + ' pontos!')

alien_0['color'] = 'yellow'
alien_0['points'] = 10
alien_0['x_position'] = 10
alien_0['y_position'] = 50

print('Você acertou o alien ' + alien_0['color'] + ' na posição ' + 'x: ' + str(alien_0['x_position']) + ' y: ' + str(alien_0['y_position']) + '.')
print('Você marcou ' + str(alien_0['points']) + ' pontos!')
