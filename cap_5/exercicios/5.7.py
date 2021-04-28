# Fruta Favorita:Faça uma lista de suas frutas favoritas e, então, escreva uma série de instruções if.
# independetes que verifiquem se determinadas frutas estão em sua lista:

frutas = ['laranja', 'melão', 'melancia', 'maracujá', 'mamão', 'banana']
while True:
    
    fruta = input('Digite o nome de uma fruta ou s para encerrar:\n')
    
    if fruta == 's' or (fruta == 'S'):
        print('Programa Encerrado!')
        break

    if fruta in frutas:
        print(f'{fruta} está entre as minhas favoritas!')
        frutas.remove(fruta)
    
    if fruta == 'banana':
        print(f'Eu realmente gosto de {fruta.upper()}')
    
    if fruta == 'melancia':
        print(f'Eu realmente gosto de {fruta.upper()}')

    else:
        print(f'{fruta} não está entre as minhas frutas favoritas')
        print('Tente outra vez!')