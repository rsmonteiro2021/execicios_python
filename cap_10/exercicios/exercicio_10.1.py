"""Aprendendo Python: Abra um arquivo em branco em seu editor de texto e escreva algumas
    linhas que sintetizem o que você aprendeu sobre Python até agora. Comece cada linha com
    a expressão Em Python podemos... Salve o arquivo como learning_python.txt no mesmo diretó
    -rio em que estão seus exercícios deste capítulo. Escreva um programa que leia o arquivo e
    mostre o que você escreveu, três vezes. Exiba o conteúdo uma vez lendo o arquivo todo, uma 
    vez percorrendo o objeto arqivo com um laço e outra armazenando as linhas em uma lista e
    então trabalhando com ela fora do bloco with.
"""
    
filename = 'learning_python.txt'
    
x = 0
with open(filename) as file_object:
    contents = file_object.readlines()
    print(contents)
while x > 0 and x < 4:
    print(contents)
    x += 1
