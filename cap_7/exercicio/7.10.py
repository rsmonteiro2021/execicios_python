# Férias dos Sonhos: Escreva um programa que faça uma enquete sobre as férias dos sonhos dos usuários.
# Escreva um prompt semelhante a este: 'Se pudesse visitar um lugar do mundo, para onde você iria? Inclua
# um bloco de código que apresente os resultados da enquete.

lugar_dos_sonhos = {}

active = True
while active:
    nome = input('Qual o seu nome? (Digite s para encerrar!)\n')
    resposta = input('Se você pudesse visitar um lugar do mundo, para onde você iria?\n')

    lugar_dos_sonhos[nome] = resposta

    continuar = input('Deseja continuar a pesquisa? (s/n)\n')
    if continuar == 'n':
        active = False
print("\n--- Poll Results ---")
for nome, resposta in lugar_dos_sonhos.items():
    print(f'nome + " Gostaria de visitar " + resposta + ".")
