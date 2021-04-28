""" 
Albuns dos Usuários: comece com seu programa do exercício 8.7. Escreva um laço while que permita aos usuários
fornecer o nome de um artista e o título de um álbum. Depois que tiver essas informações, chame make_album() com
as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir um valor de saída no laço while.
"""

def make_album(name, title, faixas = ''):
    """Exibe o título de um álbum e o nome do artista autor do álbum."""
    if faixas:
        album_information = {'Artista': name.title(), 'Album': title.title(), 'Faixas': faixas}
    else:
        album_information = {'Artista': name.title(), 'Album': title.title()}
    return album_information

while True:
    print("Digite 's' em qualquer momento para encerrar o programa!")
    name = input('Digite o nome do artista:\n')
    if name == 's':
        break
    title = input('Digite o título do álbum:\n')
    if title == 's':
        break

    faixas_confirm = input('Deseja informar o número de faixas do álbum (s/n)?\n')
    if faixas_confirm == 'n':
        informação_completa = make_album(name, title)
        for name, title in informação_completa.items():
            print(name + ': ' + title)
    elif faixas_confirm == 's':
        faixas = int(input('Digite o número de faixas que o álbum contem:\n'))
        informação_completa = make_album(name, title, faixas)
        print(informação_completa)
        continue
    
    