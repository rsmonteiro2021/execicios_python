""" Album: Escreva uma função chamada make_album() que construa um dicionário descrevendo um álbum musical.
A função deve aceitar o nome de um artista e o título de um álbum e devolver um dicionário contendo essas
duas informações. Use a função para criar três dicionários que representem álbuns diferentes. Apresente
cada valor devolvido para mostrar que os dicionários estão armazenando as informações do álbum corretamente.
Apresente um parâmetro opcional em make_album() que permita armazenar o número de faixas em um álbum. Se a
linha que fizer a chamada incluir um valor para o número de faixas, acrescente esse valor ao dicionário do
álbum. Faça pelo menos uma nova chamada da função incluindo o número de faixas em um álbum."""

def make_album(name, title):
    """Exibe o título de um álbum e o nome do artista autor do álbum."""
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
    informação_completa = make_album(name, title)
    
    for name, title in informação_completa.items():
        print(name + ': ' + title)