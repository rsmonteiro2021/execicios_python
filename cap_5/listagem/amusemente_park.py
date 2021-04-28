# As vezes se faz necessario testar mais de duas situações possíveis. Por exemplo, considere um parque de diversões que cobre preços distintos para grupos
# etários diferentes:

# A entrada para qualquer pessoa com menos de 4 anos é gratuita;
# A entreda para qualquer pessoa com idade entre 4 e 18 anos custa 5 dólares;
# A entrada para quaqluer pessoa com 18 anos ou mais custa 10 dólares.

visitante = input('Digite o nome do visitante:\nOu digite C para cancelar\n')

while True:
    if visitante == 'C' or (visitante == 'c'):
        print('Programa Encerrado!')
        break
    else:
        idade = int(input('Qual a idade do visitante? '))

        if idade < 4:
            print('Entrada gratuita!')

        elif idade > 4 and (idade < 18):
            print('Será cobrado o valor de U$ 5,00 dólares!')

        else:
            print('O valor da entrada é de US 10,00 dólares!')

    visitante = input('Digite o nome do visitante:\nOu digite C para cancelar\n')
