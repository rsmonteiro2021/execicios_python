# O programa a seguir que o usuário forneça um texto e, em seguida, exibe essa mensagem:

name = input("Please enter your name:\n")
print(f'\nHello, {name}!')

prompt = "If you tell us who you are, we can personalize tehe messages you see."
prompt += "\nWhats is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you?\n")
print(f'Your age old is {age}')

# age >= 18        # Python apresenta uma mensagem de Erro porque a entrada de age está como uma string
age = int(age)
print(age >= 18)