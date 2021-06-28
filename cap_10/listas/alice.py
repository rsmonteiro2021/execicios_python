"""Vamos chamar um arquivo de texto que não fora salvo no mesmo diretório e gerar um traceback.
"""
filename = 'alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    #conta o número aproximado de palavras no arquivo
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
