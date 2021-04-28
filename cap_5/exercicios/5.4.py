# Cores de Alienígenas #2: Escolha uma cor para um alienígena como foi feito no exercício 5.3, e escreva uma cadeia if-else.


alien_color = ['verde', 'amarelo', 'vermelho', 'preto', 'rosa']
x = 0
print('Intruções do jogo:\n')
print('Tudo o que tem a fazer é escolher uma cor (ex. preto). A cada acerto, você soma uma pontuação, se repetir a cor ou escolher uma cor que não esteja '
      'na lista o jogo acaba.')
print('Vamos Começar? Boa sorte!')
while True:
    color = input('\nEscolha uma cor: \n')
    if color in alien_color:
        if color == 'verde':
            print('Você acaba de somar 5 pontos')
            x += 5
            alien_color.remove(color)
        elif color == 'amarelo':
            print('Você acaba de somar 10 pontos')
            x += 10
            alien_color.remove(color)
        elif color == 'vermelho':
            print('Você acaba de somar 15 pontos')
            x += 15
            alien_color.remove(color)
        else:
            print('Você não somou pontos')
            alien_color.remove(color)
    else:
        print('Game Over! Você errou!')
        print(f'Você marcou {x} pontos')
        break
        
