#Exibir uma citação
while True:
    famous_persona = int(input("Escolha sua opção: \n1 - Albert Einstein; \n2 - Voltaire; \n3 - Sair \nOpção: ")) 
    #famous_persona = int(input("""Escolha uma opção:
#1 - Albert Einstein;
#2 - Voltaire;
#3 - Sair:
#Opção: """))
    if famous_persona == 3:
        break
    elif famous_persona == 1:
        print("A mente se que expande para o conhecimento jamais voltará ao seu tamanhao original!")
    elif famous_persona == 2:
        print("Posso não concordar com nada do que dizes mas morrerei defendendo o direito de dizê-las!")
    else:
        print('Escolha entre as opções propostas!')
