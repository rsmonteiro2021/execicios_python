# Elaboração de Prontuário de Paciente - CoViD-19

lista_de_sintomas = []
dados_do_paciente = {}
sinais_vitais = {'oximetria': 99, 'PA': '12/8', 'temperatura': 36}
# Dados do Paciente
while True:
    paciente = input('Digite o nome do paciente: (digite s para encerrar)\n')
    if paciente == 's':
        print('Programa encerrado com sucesso!')
        break
    idade = int(input('Digite a idade do paciente:\n'))
    profissao = input('Digite a sua profissáo?\n')
    dados_do_paciente.update({paciente: [idade, profissao]})
    
    if profissao == 's':
        atuacao = input('Qual a atuação?\n')

    while True:
        sintomas = input('apresentou sintomas? (s/n)\n')
        if sintomas == 'n':
            print('Mais nenhum sintoma a ser declarado!')
            break
        else:
            print('Confirme os sintmas abaixo:')
            sintoma_1 = input('Sentiu febre? (s/n)\n')
            if sintoma_1 == 's':
                lista_de_sintomas.append('febre')
            sintoma_2 = input('Sentiu dor de cabeça? (s/n)\n')
            if sintoma_2 == 's':
                lista_de_sintomas.append('dor de cabeça')
            sintoma_3 = input('Teve tosse? (s/n)\n')
            if sintoma_3 == 's':
                lista_de_sintomas.append('tosse')
            sintoma_4 = input('Sentiu coceira no fundo da garganta? (s/n)\n')
            if sintoma_4 == 's':
                lista_de_sintomas.append('coceira na garganta')
tomo = input('Paciente fez exame de tomografia (s/n)?\n')
if tomo == 's':
    dias = input('Com quantos dias de sintomas fez o exame?\n')
    comprometimento = int(input('Qual a porcentagem de comprometimento?\n'))
elif tomo == 'n':
    print('Ok então!')

repeticao = input('Repetiu a tomografia (s/n)?\n')
if repeticao == 's':
    q_dias = int(input('Com quantos dias repetiu?\n'))
    q_comprometimento = int(input('Qual o percentual de comprometimento dos pulmões?\n'))

print("\nRelatório do Paciente:")
for dados, especifico in dados_do_paciente.items():
    print(dados, especifico)
print('Sinais Vitais do Paciente:')
for sinal, vital in sinais_vitais.items():
    print(sinal, vital)
print('\nEstes foram os sintomas declarados:')
for sintoma in lista_de_sintomas:
    print(sintoma)
print(f'Paciente apresentou {q_comprometimento}% de comprometimento dos pulmões aos {q_dias} dias de sintomas.')