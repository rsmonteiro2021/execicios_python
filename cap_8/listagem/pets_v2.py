# Argumentos posicionais - contar a ordem dos argumentos fornecidos
# A função abaixo apresenta uma informação sobre animais de estimação, o tinpo de cada animal de estimação
# e o nome dele.

# sendo que agora iremos criar um valor argumento default no parâmetro 
def describe_pet(pet_name, animal_type = 'dog'):
    """Exibe informação sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# se chamarmos a função apenas com o pet_name teremos, o default para o animal_type;
describe_pet('wolverine')

# para atribuir um argumento para animal_type pode-se chamar a função do seguinte modo:
describe_pet(animal_type = 'Shitzu', pet_name = 'Bidu')

# outra forma que pode ser utilizada para alterar o argumento do parâmetro animal_type pode ser:
describe_pet('harry', 'hamster')

# describe_pet() se chamarmos a função sem os argumentos Python retorna uma mensagem de Error