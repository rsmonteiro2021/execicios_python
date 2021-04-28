# Vamos criar um programa de enquete em que cada passagem pelo laço solicita o nome do participante e uma,
# resposta. Armazenaremos os dados coletados em um dicionário, pois queremos associar cada resposta a um
# usuário em particular:

responses = {}
# define uma flag para indicar que a enquente está ativa
polling_active = True

while polling_active:
    # pede o nome da pessoa e a resposta
    name = input('\nWhat is your name?\n')
    response = input('Which mountain would you like to climb someday?\n ')

    # Armazena a resposta no dicionário
    responses[name] = response

    # Responde se a outra pessoa vai responder à enquente
    repeat = input('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False

# A enquete fi concluída. Mostra os resultados
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")