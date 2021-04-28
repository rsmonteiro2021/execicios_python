"""
Grandes mágicos: Comece com uma cópia de seu programa do Exercício 8.9. Escreva uma
função chamada make_great() que modifique a lista de mágicos acrescentando a expressão
"o Grande" ao nome de cada mágico. Chame show_magicians() para ver se a lista foi 
realmente modificada.
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