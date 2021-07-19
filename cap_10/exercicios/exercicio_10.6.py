"""Adição: Um problema comum quando pedir entradas numéricas ocorre quando as pessoas fornecem
texto em lugar de números. Ao tentar converter a entrada para um int, você obterá um TypeError
Escreva um programa que peça dois números ao usuário. Some-os e mostre o resultado. Capture o
TypeError caso algum dos valores de entrada não seja um número e apresente uma mensagem de
erro simpática. Teste seu programa fornecendo dois números e, em seguida, digite um texto no
lugar de um número"""

class Soma():
    """Modela a soma de dois números inteiros."""
    
    def __init__(self, numero1, numero2):
        """Inicializa os atributos do programa soma!"""
        self.numero1 = numero1
        self.numero2 = numero2
    
    def soma_numero(self, soma):
        """Soma dois números"""
        soma = numero1 + numero2
        return soma
        
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

adicao = Soma(numero1, numero2)
print(numero1 + numero2)
