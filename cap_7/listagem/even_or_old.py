# Podemos o módulo para determinar se um número é par (even) ou impar(odd):

number = input("Enter a number, and I'll tell you if it's even or odd:\n")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")