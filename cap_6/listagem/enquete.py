# VAmos criar uma equente pra saber qual a linguagem preferida pelos programadores.

# Enquete:

favorite_langues = {}
Python = 0
C = 0
Ruby = 0
participantes = 0
nenhum = 0
votacao = []
while True:
    participante = input('Nome do participante (digite fim para encerrar):\n')
    if participante == 'fim':
        print('Enquente Encerrada!\nResultado:\n')
        break
    else:
        print("""\nOpções:
    Python = P;
    C;
    Ruby = R;
    nenhum = N
    """)
        favorite = input('Linguagem favorita: \n')
        favorite_langues['participante'] = participante
        participantes += 1
        favorite_langues['langues'] = favorite
        if favorite_langues['langues'] == 'P':
            Python += 1
            
        elif favorite_langues['langues'] == 'C':
            C += 1
           
        elif favorite_langues['langues'] == 'R':
            Ruby += 1
            
        elif favorite_langues['langues'] == 'N':
            nenhum += 1
            
        else:
            print('A linguagem não faz parte da lista')

print(f'Foram computados {participantes} votos.')
votacao = [Python, Ruby, C, nenhum]

if votacao[0] > votacao[1] and votacao[0] > votacao[2]:
    print(f'Python foi a mais votada com {max(votacao)} votos.')
elif votacao[1] > votacao[0] and votacao[1] > votacao[2]:
    print(f'Ruby foi a mais votada com {max(votacao)} votos.')
elif votacao[2] > votacao[0] and votacao[2] > votacao[1]:
    print(f'C foi a mais votada com {max(votacao)} votos.')
elif votacao[0] == votacao[1] and votacao[0] > votacao[2]:
    print(f'Python e C receberam o mesmo número de votos, {max(votacao)} voto(s) cada.')
elif votacao[0] == votacao[1] and votacao[0] == votacao[2]:
    print(f'Python, Ruby e C empataram com {max(votacao)} voto(s) cada.')
elif votacao[0] == votacao[2] and votacao[0] > votacao[1]:
    print(f'Python e Ruby empataram com {max(votacao)} voto(s) cada.')

print(f'{nenhum} participantes não preferem nenhuma dessas linguagens')