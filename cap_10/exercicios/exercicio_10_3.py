"""Exercicio 10.3 - Convidado: Escreva um programa que pergunte o nome ao usuário.
Quando ele responder, escreva o nome em um arquivo chamado guest.txt"""

usuario = input("Seja bem vindo qual o seu nome?\n")
filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write('Usuário: ' + usuario)