#Animais: Pense em pelo menos três animais diferentes que tenham uma característica em comum. Armazene os nomes desses animais em uma lista e, então, utilize.
#um laço for para exibir o nome de cada animal.
animais = ['Leão', 'Leopardo', 'Tigre', 'Gato']
animais.sort()
for animal in animais:
    if animal != 'Gato':
        print(f'{animal} é um animal selvagem e não deve ser domesticado')
    else:
        print(f'{animal} é um animal que pode ser domesticado!')
print('\nSelvagens ou não, proteja os animais!')
