"""Vamos chamar um arquivo de texto que não fora salvo no mesmo diretório e gerar um traceback.
"""
filename = 'alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
