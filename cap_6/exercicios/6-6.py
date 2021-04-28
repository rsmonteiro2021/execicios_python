# Resolução de Equação do Segundo Grau Completa:
# ax2 + bx + c = 0

a = int(input('Digite o coeficiente angular da equação:\n'))
b = int(input('Digite o coeficiente linear da equação:\n'))
c = int(input('Digite o coeficiente:\n'))

# Veriricar o Delta:
delta = (b**2) - (4 * a * c)

if delta == 0:
    x1 = (-b/(2*a))
    x1 = x2
    print(f'x1 = {x1} e x2 = {x2}')
if delta < 0:
    print('A equação não possui raíexes Reais!')
else:
    x1 = ((-b + (delta**0.5))/(2*a))
    x2 = ((-b - (delta**0.5))/(2*a))
    print(f'x1 = {x1} e x2 = {x2}')
