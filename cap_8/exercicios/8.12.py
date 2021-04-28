"""
sanduiches: Escreva uma função que aceite uma lista de itens que uma pessoa
quer em um sanduiche. A função deve ter um parâmetro que agrupe tantos itens
quantos forem fornecidos pela chamada da função e deve apresentar um resumo
do sanduiche pedido. Chama a função três vezes usando um número diferente de
argumentos a cada vez.
"""
def make_sanduiche(*intens):
    """Exibe um sanduiche personalizado"""
    sanduiche = [seu_sanduiche]
    return sanduiche

opcoes = ['pão', 'carne', 'queijo', 'frango', 'mussarela', 'ervilha', 'milho verde']
print('Estas são suas opções:\n')
selecionadas = []

while len(opcoes) > 0:
    print('Opções Restantes:\n')
    for opcao in opcoes:
        print(f'\t-{opcao}')
    item = input('Digite o item escolhido, ou clique Enter para sair:\n')
    
    if item == '':
        break
    
    elif item in selecionadas:
        print('Você já escolheu este item, por favor escolha outra oção:\n')
        print(f'Opõções:\n\t{opcoes}')
    
    elif item not in opcoes:
        print('Este item não está disponível em nosso cardápio!')
        print(opcoes)
        continue
    else:
        opcoes.remove(item)
        selecionadas.append(item)
seu_sanduiche = selecionadas
print(f'Seu sanduiche contem: {make_sanduiche(item)}')