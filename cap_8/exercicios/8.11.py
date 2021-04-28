"""
Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com a lista de nomes de mágicos. Como
a lista original não será alterada, devolva a nova lista e armazene-a
em uma lista separada. Chame show_magicians() com cada lista para mostrar
que você tem uma lista de nomes originais e uma lista com a expansão o Grande
ao nome de cada mágico.
"""
def show_magicians(nomes):
    "Exibe uma lista de mágicos."
    magicians = nome.title()
    return magicians

magicos = []

while True:
    print('Tecle Enter para encerrar!')
    nome = input('Digite o nome do mágico:\n')
    if nome == '':
        break
    else:
        magicos.append(nome)

print('\n Executa o mesmo algoritmo com uma pequena alteração!')

def make_great(nomes):
    """Exibe uma alteração na lista de mágicos exibida."""
    magicians = 'O(A) grande ' + nome.title()
    return magicians

print('Lista Original de Mágicos:\n')
for nome in magicos:
    print(f'\t{show_magicians(nome)}!')

print('\nLista Alterada de Mágicos:\n')
for nome in magicos:
    print(f'\t{make_great(nome)}!')