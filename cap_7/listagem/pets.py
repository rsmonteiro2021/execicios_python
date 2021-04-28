# Suponha que tenhamos uma lista de animais de estimação com o valor 'cat' repetido várias vezes. Para
# remover todas as instâncias desse valor, podemos executar um laço while até 'cat' não estar mais na lista
# como vemos a seguir:

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)