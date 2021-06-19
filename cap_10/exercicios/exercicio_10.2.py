"""Aprendendo C: Você pode usar o método replace() para substituir qualquer palavra por uma
palavra diferente em uma string. Eis um exemplo rápido que mostra como susbtituir a palavra
'dog' por 'cat' em uma frase:
>>> message = 'I really link dogs.'
>>> message.replace('dog', 'cat')
'I really like cats.'+

Leia cada linha do arquivo learning_python.txt que você acabou de criar e substitua a palavra
Python pela nome de outra linguagem, por exemplo, C. Mostre cada linha modificada na tela.
"""

message = 'Python'
message.replace('Python', 'C')

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
exercicio_10_2 = ''
for line in lines:
    exercicio_10_2 += line.strip()
    
print(exercicio_10_2)
