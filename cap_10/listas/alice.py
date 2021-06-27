"""Vamos chamar um arquivo de texto que não fora salvo no mesmo diretório e gerar um traceback.
"""
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)