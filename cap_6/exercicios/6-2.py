# Números favoritos: Use um dicionário para armazenar os números favoritos de algumas pessoas. Pense em cinco nomes e use-os como 
# chaves em seu dicionário . Pense em um número favorito  para cada pessoa e armazene cada um como um valor em seu dicionário. Exiba
# o nome de cada pessoa e seu número favorito. Para que seja mais divertido ainda, faça uma enquete com alguns amigos e obtenha alguns
# dados reais para o seu programa.

favorite_number = {
    'Kesia': 16,
    'Roberto': 4,
    'Lucio': 21,
    'Eliene': 79,
    'Renata': 88
}
print('Kesia, ' + str(favorite_number['Kesia']) + ' is favorite number.')
print('Roberto: ' + str(favorite_number['Roberto']) + ' is favorite number.')
print('Lucio: ' + str(favorite_number['Lucio']) + ' is favorite number.')
print('Eliene: ' + str(favorite_number['Eliene']) + ' is favorite number.')
print('Renata: ' + str(favorite_number['Renata']) + ' is favorite number.')

# Enquete:
while True:
    name = input('Quem será o intrevistado (ou digite sair par encererrar)\n')
    if name == 'sair':
        break
    number = int(input('Qual o seu número favorito?\n'))
    if name == 'Roberto':
        favorite_number['Roberto'] = number
    elif name == 'Kesia':
        favorite_number['Kesia'] = number
    elif name == 'Lucio':
        favorite_number['Lucio'] = number
    elif name == 'Eliene':
        favorite_number['Eliene'] = number
    elif name == 'Renata':
        favorite_number['Renata'] = number
    else:
        print('O nome digitado não foi relacionado.')
        
print('Kesia, ' + str(favorite_number['Kesia']) + ' is favorite number.')
print('Roberto: ' + str(favorite_number['Roberto']) + ' is favorite number.')
print('Lucio: ' + str(favorite_number['Lucio']) + ' is favorite number.')
print('Eliene: ' + str(favorite_number['Eliene']) + ' is favorite number.')
print('Renata: ' + str(favorite_number['Renata']) + ' is favorite number.')