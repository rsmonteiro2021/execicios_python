#Contando até 20: Use um laço for para exibir os números de 1 a 20, incluindo-os.
#opção 1
# lista simples
numbers = []
print('O números de sua lista são:\n')
for number in range(1,21):
    print(number)

#lista mais completa
numbers = []
x = 1
for number in range(1,21):
    numbers.append(x)
    x += 1
print(f'sua lista é formada por: \n{numbers}')

