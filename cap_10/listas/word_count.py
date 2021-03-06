def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo."""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass #falha silenciosamente
        """msg = "Sorry, the file " + filename + " does not exist."
        print(msg)"""
    else:
        #Conta o número aproximado de palavras no arquivo.
        words = contents.split()
        num_words = len(words)
        print("The file " + " has about " + str(num_words) + " words.")
        
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
