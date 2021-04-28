#Um Milhão: Crie uma lista de números de um a um milhão e, então, use um laço for para exibir os números.
#opção 1
# lista simples.
for number in range(1,10):
    print(number)

#uma outra opção é criar uma variável atrvés do comando list, lista, nesse caso é uma variável
lista = list(range(1,101))
print(f'você criou a seguinte lista nesta segunda opção: {lista}')
print(f'nesse caso o menor número da sua lista é: \n{min(lista)} \nenquanto o maior número da sua lista é {max(lista)}')

#lista mais completa
numbers = []
x = 1
for number in range(1,101):
    numbers.append(x)
    x += 1
print(f'sua lista é formada por: \n{numbers}')
print(f'o maior valor da lista é: \n{max(numbers)}')
print(f'o menor valor da lista é: \n{min(numbers)}')
print(f'e a soma dos valores da sua lista é: \n{sum(numbers)}')
 

