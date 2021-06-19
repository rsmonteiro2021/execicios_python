"""Trabalhando com o conteúdo de um arquivo
Você poderá fazer o que quiser com esses dados."""

filename = 'pi_digits.txt'

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    
pi_string =''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
