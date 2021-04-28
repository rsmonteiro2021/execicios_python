# Ingressos para o cimena: Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma
# pessoa. Se a pessoa tiver menos de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos
# o ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares. Escreva um laço
# em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso do cinema.

total = 0.00
comprados = {}
preços = {'Entre 1 e 3 anos': 'U$ 0.00', 'Entre 3 e 12 anos': 'U$ 10.00', 'Maior que 12 anos': 'U$ 15.00'}
print('Preços dos Ingressos por Idade\n')
for idade, preço in preços.items():
    # apresenta os preços dos ingressos para os usuários;
    print(f'\t{idade}: {preço}')                                                                           

while True:
    # solicita que o usuário digite a idade do cliente;
    idade = float(input('Qual a idade do cliente (digite 0 para sair)?\n'))                                
    
    # comando para encerrar a compra;
    if idade == 0:                                                                                         
        break
    
    elif idade > 0 and idade <= 3:
        ingresso = 0.00
        # informa o preço do ingresso para o cliente, com base na idade digitada;
        print('O ingresso sai grátis!')                                                                   
        # o cliente deve confirmar ou não a compra;
        confirma = input('Deseja adicionar ao carrinho (s/n?)\n')                                         
        if confirma == 'n':
        # caso não tenha interesse pela compra (ou tenha digitado a idade errada), o programa retorna para início;
            continue                                                                                      
        elif confirma == 's':
            # caso o cliente deseje comprar, ele pode determinar a quantidade de ingressos para a mesma categoria;
            quantidade = float(input('Quantos ingressos nessa categoria?\n'))                             
            # o programa calcula o valor dos ingressos para a mesma categoria e;
            semi_total = (quantidade * ingresso)                                                          
            # armazena o valor total da compra;
            total += semi_total
            comprados.update({quantidade: ingresso})
        else:
            print('ERRO! Digite apenas s para sim ou n para não!')
            continue                                                                           
                                                                                                          
    # A estutura se repete para os demais intervalos de idade:
    elif idade > 3 and idade <= 12:
        ingresso = 10
        print('O ingresso custa U$ 10.00.')
        confirma = input('Deseja adicionar ao carrinho (s/n?)\n')
               
        if confirma == 'n':
            continue
        elif confirma == 's':
            quantidade = float(input('Quantos ingressos nessa categoria?\n'))
            semi_total = (quantidade * ingresso)
            total += semi_total
            comprados.update({quantidade: ingresso})
        else:
            print('ERRO! Digite apenas s para sim ou n para não!')
            continue
    
    elif idade > 12:
        ingresso = 15
        print('O ingresso custa U$ 15.00.')
        confirma = input('Deseja adicionar ao carrinho (s/n?)\n')
        if confirma == 'n':
            continue
        elif confirma == 's':
            quantidade = float(input('Quantos ingressos nessa categoria?\n'))
            semi_total = (quantidade * ingresso)
            total += semi_total
            comprados.update({quantidade: ingresso})
        else:
            print('ERRO! Digite apenas s para sim ou n para não!')
            continue
    else:
        # caso o cliente digite uma idade com valor negativo, o programa retorna uma mensagem de erro!
        print('ERRO!Verifique a idade digitada!!')

# Finalizando a compra:
active = True
while active:
    # O programa apresenta o valor total dos ingressos adicionados ao carrinho;
    print('Você selecionou:')
    for quantidade, preço in comprados.items():
        print(f'\t{quantidade} igressos de {preço}')
    print('\nO valor total é de U$%5.2f' % total)
    # Solicita ao usuário que confirme ou não a compra;
    confirm = input('Deseja confirmar sua compra (s/n)?\n')
    # Em caso afirmativo, apresenta uma mensagem de Processamento de compra e de Boas Vindas!
    if confirm == 's':
        print('\nSeja Bem Vindo(a)!\nIremos processar sua compra. Retire seu(s) ingresso(s) na bilheteria!\nBom filme!')
        print('Necessário apresentar documento de identficação junto aos ingressos na entrada da sala.')
        active = False
# Em caso contrário, o carrinho é esvaziado e o total volta a ser zero!
    elif confirm == 'n':
        total = 0.00
        print('\nQue pena! Esvaziamos seu carrinho!')
        active = False
    else:
        print('ERROR! Digite apenas s para sim ou n para não!')
