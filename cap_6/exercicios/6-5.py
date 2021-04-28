# Rios: Crie um dicionário que contenha três rios importantes e o país que cada rio corta. Um par chave-valor poderia ser:
# Nilo: Egito.

# Resposta:

rios = {'São Francisco': 'Brasil',
'Amarelo': 'China',
'Ghandi': 'Índia'}

# Use um laço para exibir uma frase sobre cada rio, por exemplo, O rio Nilo corre pelo Egito.

for rio, pais in rios.items():
    if rio == 'São Francisco':
        print('O Rio ' + rio + ' percorre o ' + pais + '.')
    elif rio == 'Amarelo':
        print('O Rio ' + rio + ' percorre a ' + pais + '.')
    else:
        print('O Rio ' + rio + ' percorre a ' + pais + '.')

# Use um laço para exibir o nome de cada rio incluído no dicionário:
print('\nRios contidos na relação:')
for rio in rios.keys():
    print(rio)
# Use um laço para exibir o nome de cada país incluído no dicionário:
print('\nPaíses contidos na relação:')
for pais in rios.values():
    print(pais)