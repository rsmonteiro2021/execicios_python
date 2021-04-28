#Nomes - armazene os nomes de alguns de seus amigos em uma lista chamada names. Exiba o nome de cada pessoa acessando cada elemento da lista, um de cada vez.
list = ['bicicleta', 'Chevrollet Cruze', 'Dell G5', 'Iphone 12']
while True:
    desejo = input("Qual seu desejo? ou Digite 'sair': ")
    if desejo == 'sair':
        break
    elif desejo == 'bicicleta':
        print(f'Até o final de 2021 irei adquirir uma {desejo.title()}')
    elif desejo == 'Chevrollet Cruze':
        print(f'Entre os meus desejos materiais encontra-se o {desejo.title()} sport!')
    elif desejo == 'Dell G5':
        print(f'Se eu tiver condições, em 2022/2023 irei adquirir um {desejo.title()}!')
    elif desejo == 'Iphone 12':
        print(f'Logo eu voltarei a ser usuário Apple e comprarei um {desejo.title()}!')
    else:
        print(f'Escreva um desejo dentreo da lista {list}')
