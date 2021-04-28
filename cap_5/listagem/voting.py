# O código a seguir determina se a pessoa tem idade ou não para votar
# Este código é de minha autoria, portanto, difere do que é apresentado no livro (mais simples)

ano = 2021
limite = 16
x = 0
y = 0
validos = []
nao_validos = []

while True:

    eleitor = input('Digite o nome do eleitor: \nOu digite S para encerrar:\n')

    if eleitor == 's' or (eleitor == 'S'):
        print('Eleitores verificados com sucesso!')
        print(f'Foram registrados {x} eleitores válidos e {y} eleitores abaixo da idade de votação!\n')

        print('Eleitores válidos registrados:')
        for eleitor in validos:
            print(eleitor)

        print('\nEleitores não válidos registrados:')
        for eleitor in nao_validos:
           
            print(eleitor)
        break

    else:
        nascimento_ano = int(input('Digite o ano de nascimento: \n'))
        idade = ano - nascimento_ano
        
        if (ano - nascimento_ano) >= 16:
            print(f'Você é maior de {limite} anos, portanto tem idade para votar!')
            validos.append(eleitor.title())
            x += 1

        else:

            print(f'Prezado cidadão por você ser menor de {limite} anos ainda não tem idade para votar')
            print(f'Sua idade é {idade} anos!')
            nao_validos.append(eleitor.title())
            y += 1
