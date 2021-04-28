# VAmos criar uma equente pra saber qual a linguagem preferida pelos programadores.

# Enquete:

favorite_languages = {
    'Jen': ['python', 'ruby'],
    'Sarah': ['C'],
    'Eduward': ['Ruby', 'go'],
    'Phil': ['python', 'haskel']
}

# Perorrendo as chaves de um docionário através do laço for:

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f'\n{name.title()} is favorite languages are: ')
        for language in languages:
            print(f'\t {language.title()}')
    else:
        print(f'\n{name.title()} favorite languages is {language.title()}')
    
        
