# Considere um jogo com alienígenas que possam ter cores e valores de pontuação diferentes. O dicionário simples a seguir armazena
# informações sobre um alienigena em particular:

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])                                   # obtem o valor associado a uma chave, especifique o nome do dicionário e coloque a chave entre colchetes
print(alien_0['points'])                                  # Esta instrução devolve o valor associado a chave 'points'

# Pode-se acessar a pontuação de um alien. Se um jogador atingir esse alienígena, podemos consultar quantos pontos ele deve ganhar
# usando um código como este:

new_points = alien_0['points']
print('you just earned ' + str(new_points) + ' points!')
print(f'You just earned {new_points} points!')             # Essa é uma forma alternativa de devolver a mensagem.

# Posicionando o aline na tela:

alien_0['x_position'] = 0                                 # Esta ação adiciona um novo par chave-valor ao dicionário;
alien_0['y_position'] = 25
print(alien_0)