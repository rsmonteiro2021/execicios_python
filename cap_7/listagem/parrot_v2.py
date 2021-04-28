# O laço while.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n "

message = ""
while message != 'quit':
    if message == 'quit':
        break
    elif message == input(prompt):
        print(message)

# Fiz algumas alterações no programa utilizanda função 'break', 'if' e 'elif'.
    
