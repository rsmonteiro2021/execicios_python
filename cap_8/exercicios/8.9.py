"""
Mágicos: crie uma lista de nomes de mágicos. Passe a lista para uma função chamada
show_magicians() que exiba o nome de cada mágico da lista.
"""
# Define uma função chamada show_magicians() com o parâmetro nomes
def show_magicians(nomes):
    """Exibe uma lista com nomes de mágicos."""
    magico = nome.title()                       # Atribui o valor nome.title() a variável criada mágico
    return magico                               # Desse modo a função devolve a variável mágico

magicians = []                                  # Cria uma lista vazia denominada magicians
while True:
    print('Clique Enter para encerrar.')
    nome = input('Digite o nome do mágico:\n')
    if nome == '':
      break
    else:
        magicians.append(nome)                 # Adiciona o valor da variável nome a lista magicians
for nome in magicians:
    print(f'\t {show_magicians(nome)}')        # Chama a função show_magicias com a variável nome presente na lista criada magicians e exibe a lista