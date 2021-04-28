#Trabalhando com Tuplas -
#Um retangulo que sempre deve ter determinado tamanho, podemos garantir que seu tamanho não mudará colocando as dimensões em uma tupla.
#Alterando os valores de uma tupla

dimensions = (200, 50)
print('Original Dimesnions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)
