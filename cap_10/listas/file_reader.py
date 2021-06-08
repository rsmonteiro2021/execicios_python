# Uma forma de ler um arquivo de texto em python:

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents + '\n')

# Essa é outra forma de ler um arquivo de texto em python sendo linha a linha:

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) # foi inserido a função rstrip() para que o resultado fosse igual ao anterior.

filename = 'pi_digits.txt'

"""Criando uma lista de linhas de um arquivo"""
with open(filename) as file_object:
    lines = file_object.readlines()
    
"""Essa lista pode ser chamada depois"""  
for line in lines:
    print(line.rstrip())