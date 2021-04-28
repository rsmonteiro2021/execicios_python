""" Considere uma empresa que cria modelos de design submetidos pelos usuários e que são impressos
em 3D. Os designs são armazenados em uma lista e, depois de impressos, são transferidos para uma
lista separada. O código a seguir faz isso sem usar funções:"""

# Começa com alguns desingns que devem ser impressos

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_mmodels = []

# Simula a impressão de cada design, até que não haja mais nenhum
# Transfere cada design para completed-models após a impressão

while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simula a criação de uma impressão 3D a partir do design
    print('Priting model: ' + current_design)
    completed_mmodels.append(current_design)

# Exibe todos os modelos finalizados
print("\nThe following models have been printed:")
for completed_mmodel in completed_mmodels:
    print(completed_mmodel)