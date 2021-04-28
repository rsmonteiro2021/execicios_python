# Mais Testes Condicionais: Você não precisa limitar o número de testes que criar em dez. Se quiser testar mais comparações, escreva outros testes e
# acrescente-os em conditional_test.py. Tenha pelo menos um resultado True e um FAlse para cada um dos casos a seguir:

# Teste de igualdade com strings

print('Teste de Igualdade com Strings:')
name = 'Roberto'
print("My name == 'Roberto'? I predict True.")
print(name == 'Roberto')

print("\nMy name == 'Alberto'? I predict False.")
print(name == 'Alberto')

# Teste de igualdade com strings

print('\nTeste usando a função lower:')

favorite = 'Ice Cream'
print("My favorite == 'Ice Cream'? I predict True.")
favorit = favorite.lower()
print(favorit == 'ice cream')

print("\nMy favorite == 'Ice Cream'? I predict False.")
print(favorit == 'Ice Cream')

# Testes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e menor ou igual a:

print('\nTestes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e menor ou igual a:')

age_0 = 21
age_1 = 15
print(f'Idades {age_0} anos e {age_1} anos')

print("\nIdade_0 igual a Idade_1? Verdadeiro ou Falso?")
print(age_0 == age_1)

print("\nIdade_0 diferente de Idade_1? Verdadeiro ou Falso?")
print(age_0 != age_1)

print("\nIdade_0 maior que Idade_1? Verdadeiro ou Falso?")
print(age_0 > age_1)

print("\nIdade_0 menor que Idade_1? Verdadeiro ou Falso?")
print(age_0 < age_1)

print("\nIdade_0 maior ou igual a Idade_1? Verdadeiro ou Falso?")
print(age_0 >= age_1)

print("\nIdade_0 menor ou igual a Idade_1? Verdadeiro ou Falso?")
print(age_0 <= age_1)

# Teste usando as palavras reservadas and e or:

print('\nIdade_0 é maior que Idade_1 e Idade_0 é maior que 18?')
print((age_0 > age_1) and (age_0 > 18))

print('\nIdade_0 é maior que Idade_1 e Idade_0 é menor que 18?')
print((age_0 > age_1) and (age_0 < 18))

print('\nIdade_0 é maior que Idade_1 ou Idade_0 maior que 18?')
print((age_0 > age_1) or (age_0 > 18))

print('\nIdade_0 é menor que Idade_1 ou Idade_0 menor que 18?')
print((age_0 < age_1) or (age_0 < 18))

print('\n')
# Teste para verificar se um item está ou não está em uma lista

print('Teste para verificar se o aluno está matriculado: ')
alunos = ['Bidu', 'Wolverine', 'Dunga']
cao = input('\nDigite o nome do aluno: \n')
if cao in alunos:
    print(f'{cao.title()} está matriculado')
else:
    print('Este aluno não está matriulado!')
