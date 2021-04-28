# Camiseta - Escreva uma função chamada make_shirt() que aceite um tamanho e o texto de um mensagem que
# deverá ser estambada na camiseta A função deve exibir uma frase que mostre o tamanho e a mensagem estampada.
# Chame a funão uma vez usando argumento posicionais para criar uma camiseta.
# Chame a função uma segunda vez usando argumentos nomeados.

def make_shirt(mensagem, tamanho = 'G'):
    """Exibe o tamanho de uma camiseta e uma mensagem"""
    print(f'Camiseta tamanho {tamanho}!')
    print(f'A mensagem da camiseta é {mensagem}\n')

make_shirt('P', 'I love Python!')

make_shirt(tamanho = 'M', mensagem = 'I know programer in Python!')