# Estágios da Vida: Escreva uma cadeia if-elif-else que determine o estágio da vida de uma pessoa.
# Defina um valor para a variável age (idade) e então:

# Se a pessoa tiver menos de 02 anos de idade, mostre uma mensagem dizendo que ela é um bebê.
while True:
    
    idade = int(input('Digite a idade da pessoa, ou digite 0 para sair:\n'))
    if idade <= 0:
        print('Programa Encerrado!')
        break

    elif idade < 2:
        print('Você ainda é um bebê!')

# Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem dizendo que ela é uma criança:

    elif idade >= 2 and (idade < 4):
      print('Você é uma criança!')

# Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma mensgem dizendo que ele(a) é um garoto(a):

    elif idade >= 4 and (idade < 13):
        print('Você um(a) garoto(a)!')

# Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma mensgem dizendo que ele(a) é um(a) adolescente:

    elif idade >= 13 and (idade < 20):
        print('Você é um(a) adolescente!')

# Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma mensagem dizendo que ele(a) é um adulto:

    elif idade > 20 and (idade < 65):
        print('Você é um adulto')

# Se a pessoa tiver pelo menos 65 anos, mostre uma mensagem dizendo que ele é um idoso.

    else:
        print('Você um idoso!') 