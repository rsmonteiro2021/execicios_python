#Lista de Convidados: Se pudesse convidar alguem, vivo ou morto, para o jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
#que você gostaria de convidar para jantar. Em seguida, utilize sua lista para exibir uma mensagem para cada pessoa, convidando-a para jantar.
lista = ['Roberto Monteiro']
x = 1
while True:
    convidado = input('Quem você gostaria de convidar para jantar, ou digite "E" e conclua: ')
    if convidado == 'encerrar':
        print(f'Temos que preparar um jantar para {len(lista)} pessoas! São elas: {lista}')
        break
    else:
        lista.append(convidado.title())
        print(f'Você convidou {convidado} para o jantar')
while x <= (len(lista) - 1):
    print(f'Sr(a) {lista[x]} você está sendo convidado(a) para jantar conosco amanhã as 20h')
    x += 1
while True:
    ausente = input('Qual convidado não confirmou a presença? (do contrário digite todos confirmaram): ')
    if ausente == 'todos confirmaram':
        print(f'Confirmaram presença os seguintes convidados: {lista}')
        print(f'Portanto, temos que preparar um jantar para {len(lista)} pessoas!')
        break
    else:
        print(f'O(a) Sr(a) {ausente} não poderá participar do jantar!')
        lista.remove(ausente)

#Agora você encontrou uma mesa de jantar maior, portanto agora tem mais espaço disponível.
#Pense em mais tres convidados para o jantar.
#Comece com seu programa do exercício 3.4 ou do exercício 3.5. Acrescente uma instrução print no final do seu programa informando às pessoas que você
#encontrou uma mesa de jantar maior.

while True:
    novo_convidado = input('Quem será o novo convidado? (ou E para encerrar): ')
#Utilize insert() para adicionar um novo convidado no início da sua lista.
    if novo_convidado == 'E' or novo_convidado == 'e':
        print(f'Temos que preparar um jantar para {len(lista)} pessoas!')
        print(lista)
        break
    else:
        lista.insert(0, novo_convidado.title())
        print(f'Você adicionou {novo_convidado.title()} a sua lista de convidados!')

#Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.
while True:
    excluido = input(f'Sua lista possui {len(lista)} convidados, são eles: {lista}! Quem você deseja excluir? (digite E para encerrar: ')
    if excluido == 'e' or excluido == 'E':
        print('Sua nova lista de convidados é composta por: ')
        print(sorted(lista))
        break
    else:
        x = int(input('Digite o número do seu convidado que deseja excluir: '))
        lista.pop(x)
        
        


