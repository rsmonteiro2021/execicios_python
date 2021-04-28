# Igredientes para Pizza: Escreva um laço que peça ao usuário para fornecer uma série de igredientes para
# uma pizza até que o valor 'quit' seja fornecido. À medida que cada igrediente é especificado, apresente
# uma mensagem informando que você acrescentará esse igrediente à pizza.
disponibilidade = {'Tradicionais': ['mussarela', 'calabresa', 'napolitana', 'marguerita',
'portuguesa', 'frango com milho'],
'Doces': ['Romeu e Julieta', 'Cartola', 'Brigadeiro', 'Beijinho'],
'Especiais': ['Frango com Catupiry', 'Carne do Sol com Catupiry', 'Camarão com Catupiry']
 }
print('Sabores disponíveis:')
for tipo, sabores in disponibilidade.items():
    print(tipo)
    for sabor in sabores:
        print(f'\t{sabor}')
sabor = input('Digite o sabor desejado:\n')

igredientes_adicionais = ['catupiry', 'cebola', 'azeitonas', 'tomate', 'ovos']
igredientes_adicionados = []

print('\nVocê pode adiconar à sua pizza os seguintes igredientes:')
for igrediente in igredientes_adicionais:
    print(f'\t{igrediente}')
adicione = input('\nDeseja adionar algum igrediente a sua pizza (digite s ou n)?\n')
if adicione == 'n':
    print('Tudo bem, seu pedido está fechado, sua pizza está sendo preparada!')
elif adicione == 's':
    adição = ''
    while adição != 'quit':                                           # condição de parada do laço (loop)
        adição = input('Digite o igrediente que deseja adicionar à sua pizza.'
         'Quando desejar encerrar digite quit\n')
        if adição == 'quit':                                          # condição de parada do laço (loop)
            print('\nMuito obrigado, seu pedido está sendo processado!')
            print(f'Estes foram os igredientes adicionados à sua pizza de {sabor}:')
            for igrediente in igredientes_adicionados:
                print(f'\t{igrediente}')
                print('\nObservação:\nO tempo de entrega é de até 60 minutos!')
        
        else:
            if adição in igredientes_adicionais:
                igredientes_adicionados.append(adição)
            else:
                print('O Igrediente digitado não consta na lista!')
                print('Digite da mesma forma que se encontra na lista!')