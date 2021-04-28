# Livro favorito: Escreva uma função chamada favorite_book() que aceite um parâmetro title. A função deve
# exibir uma mensagem como Um dos meus livros favoritos é Alice no País das Maravilhas. Chame a função e
# não se esqueça de incluir o título do livro como argumento na chamada da função:

def favorite_book(title, autor):
    """Exibe uma mensagem simples informando sobre o título do meu livro favorito."""
    print(f'\nUm dos meus livros favoritos é intitulado como {title.title()}, do(a) autor(a) {autor.title()}.\n')

favorite_book('stalker', 'karin slaugther')

# Aproveitei o item 'Passando Argumentos - argumentos posicionais' - para acrescentar mais de um argumento.
# No caso, além do título preferido, como pede a questão, também inclui o nome da autora do livro.