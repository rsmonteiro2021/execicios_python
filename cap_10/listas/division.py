"""Vamos observar um erro simples que faz Python levantar uma exceção. Provavelmente, 
você sabe que é impossível dividir um número por zero, mas vamos pedir que Python
faça isso, de qualquer modo."""

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")