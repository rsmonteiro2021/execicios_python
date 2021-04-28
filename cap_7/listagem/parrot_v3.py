# O laço while, determinando uma condição de parada através de uma flag.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n "

active = True               # Determinando uma Flag active = True

while active:               # Enquanto active receber True
    message = input(prompt)

    if message == 'quit':
        active = False      # Condição em que active é igual a False
    else:
        print(message)
    
