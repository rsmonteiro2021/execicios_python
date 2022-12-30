"""
    Avalise de financiamento de um imóvel.
    Verificar o valor de uma casa, salário de uma pessoa, e em quantos anos ela pretende quitar
    a casa sem dar entrada (financiamento sem juros)
"""
    
valor = float(input('Informe o valor do financiamento:\n'))
parcelas = int(input('Digite o número de parcelas:\n'))
salario = float(input('Digite a sua renda mensal:\n'))
prestacoes = valor/parcelas
limite = 0.30 * salario

while prestacoes > limite:
    
    print('Financiamento REPROVADO - prestacoes acima do limite máximo permitido!\n')
    print('Altere o valor do financiamento ou o número de parcelas!')
    
    alterar = input('Para alterar o número de parcelas digite P, para alterar o valor do financiamento digite V:\n')
    
    if alterar == 'v' or alterar == 'V':
        valor = float(input('Digite o valor do financiamento:\n'))
    elif alterar == 'p' or alterar == 'P':
        parcelas = int(input('Digite o número de parcelas:\n'))
    else:
        print('ERROR!Verifique a opção digitada!!!')
    prestacoes = valor/parcelas
        
if prestacoes <= limite:
    print('\nPARABENS seu Financiamento APROVADO!')
    print('\nRESUMO:\n')
    print('\tValor Financiado R$%5.2f;\n\tNúmero de Parcelas %d meses;\n\tPrestações de R$%5.2fa.m' %(valor, parcelas, prestacoes))
