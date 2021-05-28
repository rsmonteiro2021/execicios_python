"""
    Dados: O módulo randm contém funções que geram números aleatórios de várias maneiras
    A função randint() devolve um inteiro no intervalo especificado por você. O código 
    a seguir devolve um número entre 1 e 6.
"""

"""
    from random import randint
    x = randint(1, 6)
"""

class Die():
    """Tentaiva simples de modelar um jodo de dados."""

    def __init__(self, sides):
        """Inicializa o atributo do número."""
        self.sides = 6

    def roll_die(self):
        """Exibe um número aleatório entre 1 e o número de lados do dado."""
        from random import randint
        x = randint(1, self.sides)
        return x
    
die = Die('sides')
print('Dado Rolado!')
print("\t-Seu resultado foi: " + str(die.roll_die()))        