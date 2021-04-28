#Usando a função for range() para colcoar os dez primeiros quadrados perfeitos em uma lista.
squares = []
for value in range(1,11):
    squares.append(value**2)
print('Esses são os 10 primeiros quadrados perfeitos:')
for square in squares:
    print(square)
    
