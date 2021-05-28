"""
    Comece com o Exercício 6.4 da página 155, em que usamos um dicionário-padrão para representar um glossário.
    Reescreva o progrma usando a classe OrderedDict e certifique-se de que a ordem de sáida coincida com a ordem
    em que os pares chave-valor foram adicionados ao dicionário.
"""
"""
Glossário 2: Agora que você já sabe com percorrer um dicionário com um
laço, limpe o código do Exercício 6.3, substituindo sua sequência de
instruções print por um laço que percorra as chaves e os valores do
dicionário.
Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos
de Python ao seu glossário. Ao executar seu programa novamente, essas palavras
e signficados novos deverão ser automaticamente incluídos na saída.
"""
from collections import OrderedDict

glossario = OrderedDict()

glossario['Tupla'] = 'Se parece com uma lista, exceto por usar parênteses'
glossario['str'] = 'Utilizado para converter dados numéricos em strings'
glossario['Input'] = 'Utilizado para criar um dado de entrada pelo usuário'
glossario['Laço'] = 'pode ser um for ou um while, cria um loop no programa'
glossario['dicionário'] = 'cria uma lista com chaves e valores assim expressos'

"""
    Mostre cada palavra e seu significado em um saída formatada de modo elegante. Você pode exibir a palavra seguida de dois pontos e depois
    o seu significado, ou apresentar a palavra em uma linha e então exibir seu significado indentado em uma segunda linha. Utilize o caractere
    quebra de linha para inserir uma linha em branco entre cada par palavra siginificado em sua saída:
"""
for palavra, significado in glossario.items():
    print(palavra + ': ' + '\n' + '   '+ significado)

"""
glossario.update({'print': 'exibe um dado de saída',
'if': 'condição de análise',
'while': 'laço em forma de loop condicional',
'for': 'trata-se de um laço definido'})

print('As chaves do glossário são:')
for key in glossario.keys():
    print(key)
print('Os valores do glossário são:')
for value in glossario.values():
    print(value)

for key, value in glossario.items():
    print(key.title() + ': ' + '\n' + '   '+ value)

"""