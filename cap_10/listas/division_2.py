"""Vamos criar uma calculadora simples que faça apenas divisões:"""

print("Give me two numbers, and I'll divide them." )
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFisrt number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
  
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)