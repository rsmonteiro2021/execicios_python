#Cubos: um número elevado à terceira potência ~e chamado de cubo. Por exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez primeiros
#cubos (isto é, o cubo de cads inteiro de 1 a 10), e utilze um laço for para exibir o valor de cada cubo.

#Opção 1:

cubos = []
for numero in range(1,11):
    cubo = numero ** 3
    cubos.append(cubo)
print(cubos)
