#Lista de Convidados: Se pudesse convidar alguem, vivo ou morto, para o jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
#que você gostaria de convidar para jantar. Em seguida, utilize sua lista para exibir uma mensagem para cada pessoa, convidando-a para jantar.
lista = ['Roberto Monteiro']
x = 1
while True:
    convidado = input('Quem você gostaria de convidar para jantar, ou digite encerrar e conclua: ')
    if convidado == 'encerrar':
        print(f'Temos que preparar um jantar para {len(lista)} pessoas! São elas: {lista}')
        break
    else:
        lista.append(convidado)
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

    
