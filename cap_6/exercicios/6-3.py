# Glossário: Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo 
# de glossário.
# Pense em cinco palavras relacionadas ã programação que você conheceu nos capítulos anteriores. Use essas plavras como chaves em seu glossario
# e armazene seus significados como valores:

glossario = {'Tupla': 'Se parece com uma lista, exceto por usar parêntes',
'str': 'Utilizado para converter dados numéricos em strings',
'Input': 'Utilizado para criar um dado de entrada pelo usuário',
'Laço': 'pode ser um for ou um while, cria um loop no programa',
'dicionário': 'cria uma lista com chaves e valores assim expressos'}

# Mostre cada palavra e seu significado em um saída formatada de modo elegante. Você pode exibir a palavra seguida de dois pontos e depois
# o seu significado, ou apresentar a palavra em uma linha e então exibir seu significado indentado em uma segunda linha. Utilize o caractere
# quebra de linha para inserir uma linha em branco entre cada par palavra siginificado em sua saída:

for palavra, significado in glossario.items():
    print(palavra + ': ' + '\n' + '   '+ significado)