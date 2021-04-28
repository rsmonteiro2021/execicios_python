# Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
# Use um laço for para exibir cada prato oferecido pelo restaurante.
# Tente modificar um dos itens e certifique-se de que Python rejeita a mudança.
# O restaurante muda seu cardápio, substituindo dois dos itens com pratos diferentes. Acrescente um bloco de código que reescreva a tupla e, em seguida,
# um laço for para exibir cda um dos itens do cardápio revisado.

# Resposta:

cardapio_original = (
    'Macarronada', 'Lasanha', 'Feijoada', 'Peixada', 'Camarãozada'
    )
print('Este é o cardápio original:')

for prato in cardapio_original:
    print(prato)
    
cardapio_modificado = (
    'Macarronada', 'Lasanha', 'Inhoque', 'Cappelete', 'Pizza'
    )
print('\nEste é o cardápio modificado:')

for prato in cardapio_modificado:
    print(prato)
