# Usando uma função com um laço 'while':

def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# Aqui teremos um loop infinito:
#while True:
#    print('\nPlease tell me your name:')
#    f_name = input('First name: ')
#    l_name = input('Last name: ')
#    formatted_name = get_formatted_name(f_name, l_name)
#    print('\nHello, ' + formatted_name + '.')

# Para corrigir o loop infinito acrescentaremos mais algumas linhas de código:

while True:
    print('\nPlease tell me your name:')
    print('\nEnter 'q' any time to quit.')     # informamos ao usuário que ele pode encerrar o programa quando
                                               # quiser digitando a tecla 'q'.
    
    f_name = input('First name: ')
    if f_name == 'q':                  # aplicamos a condição de parada
        break
    l_name = input('Last name: ')      # como é em qualquer momento, aqui também aplicamos a mesma condição
                                       # de parada.
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '.')