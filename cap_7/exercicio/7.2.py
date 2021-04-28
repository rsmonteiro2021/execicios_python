# Lugares em um restaurante: Escreva um programa que pergunte ao usuário quantas pessoas estão em seu grupo
# para jantar. Se a resposta for maior que oito, exiba uma mensagem dizendo que eles deverão esperar uma
# mesa. Caso contrário, informe que sua mesa está pronta:

pessoas = int(input("Você deseja uma mesa para quantas pessoas?\n"))
if pessoas > 8:
    resposta = input("Não temos mesa disponível para o momento, deseja aguardar?\n")
    if resposta == 'sim':
        print('Avisaremos assim que sua mesa estiver pronta!')
    else:
        print('Lamentamos!')
else:
    print('Sua mesa está pronta!')