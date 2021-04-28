# Considere um programa que determina se as pessoas têm altura suficiente para andar em uma montanha-russa:

height = input("How tall are you, in inches:\n")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nyou'll be able to ride when you're a little older.")