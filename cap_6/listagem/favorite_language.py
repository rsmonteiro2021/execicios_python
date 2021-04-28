# VAmos criar uma equente pra saber qual a linguagem preferida pelos programadores.

# Enquete:

favorite_languages = {
    'Jen': 'python',
    'Sarah': 'C',
    'Eduward': 'Ruby',
    'Phil': 'python',
}

# Perorrendo as chaves de uma lista através do laço for:

for name in favorite_languages:
    print(name.title())

# Utilizando o método keys() (chaves) em um laço:

friends = ['Phil', 'Sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print('Hi ' + name.title() + ', I see your favorite language is ' + favorite_languages[name].title() + '!')

# Usando o método keys() para descobrir se uma pessoa em particular participou da enquente.

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

# A função sorted() organiza a sequência devolvida  no laço for:

for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll.')

# Agora vamos ver com percorrer os valores de uma lista:

print('\nThe following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())

# Quando utilizamos o set() em torno de uma lista que contenha itens duplicados
# Python identifica os itens únicos e cria um conjunto a partir desses intens.

for language in set(favorite_languages.values()):
    print(language.title())






