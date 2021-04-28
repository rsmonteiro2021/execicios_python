#Trabalhando com Tuplas -
#Um retangulo que sempre deve ter determinado tamanho, podemos garantir que seu tamanho não mudará colocando as dimensões em uma tupla.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print('portanto maior dimensão será:')
print(max(dimensions))
print('enquanto que a menor dimensão do retângulo será:')
print(min(dimensions))

#percorrendo todos os valores de uma tupla usando um laço for:

for dimension in dimensions:
    print(dimension)
