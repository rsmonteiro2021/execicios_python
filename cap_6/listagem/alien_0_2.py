# Considere um jogo com alienígenas que possam ter cores e valores de pontuação diferentes. O dicionário simples a seguir armazena
# informações sobre um alienigena em particular:

# vamos monitorar a posição de um alienígena que pode se deslocar com velocidades diferentes:

alien_0 = {'color': 'green', 'points': 0}

# Move o alien para a direita
# Determina a distância que o alien deve se deslocar de acordo com sua velocidade atual

x_position = int(input('Digite a posição x para onde seu alien deve se mover:\n '))
alien_0['x_position'] = x_position

if x_position >= 0 and x_position <= 25:
    alien_0['speed'] = 'stoped'
elif x_position > 25 and x_position <= 50:
    alien_0['speed'] = 'slow'
elif x_position >= 50 and x_position < 100:
    alien_0['speed'] = 'medium'
elif x_position >= 100:
    alien_0['speed'] = 'fast'
else:
    print('Posição inválida!')


if alien_0['speed'] == 'stoped':
    x_increment = 0
    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print('New x-position x: ' + str(alien_0['x_position']))
    print('Seu alien ficou parado e foi atigido!')
    print('Você marcou ' + str(alien_0['points']) + ' pontos nessa rodada!')
elif alien_0['speed'] == 'slow':
    x_increment = 15
    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print('New x-position x: ' + str(alien_0['x_position']))
    print('Seu alien se moveu lento demais e foi atigido de raspão!')
    print('Você marcou ' + str(alien_0['points']) + ' pontos nessa rodada!')
elif alien_0['speed'] == 'medium':
    x_increment = 25
    alien_0['x_position'] = alien_0['x_position'] + x_increment
    alien_0['points'] = 25
    print('New x-position x: ' + str(alien_0['x_position']))
    print('Seu alien escapou de ser atigido por pouco!')
    print('Você marcou ' + str(alien_0['points']) + ' pontos nessa rodada!')
else:
    # Este deve ser um alien rápido
    x_increment = 0
    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print('New x-position x: ' + str(alien_0['x_position']))
    print('Seu alien foi muito rápido mas retornou a posição de origem e foi atingido!')
    print('Você marcou ' + str(alien_0['points']) + ' pontos nessa rodada!')