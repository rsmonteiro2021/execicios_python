# Camisetas grandes - Modifique a função make_shirt() de modo que as camisetas sejam grandes por default,
# com uma mensagem Eu amo Python. Crie uma camiseta grande e outra média com a mensagem Default, e uma
# camiseta de qualquer tamanho com uma mensagem diferente.

def make_shirt(mensagem = 'I love Python', tamanho = 'G'):
    """Exibe o tamanho de uma camiseta e uma mensagem"""
    print(f'Camiseta tamanho {tamanho}!')
    print(f'A mensagem da camiseta é {mensagem}\n')

make_shirt()

make_shirt(tamanho = 'M')

make_shirt(tamanho = 'P', mensagem = 'I know programmer in Python!')