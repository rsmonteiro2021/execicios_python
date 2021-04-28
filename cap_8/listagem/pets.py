# Argumentos posicionais - contar a ordem dos argumentos fornecidos
# A função abaixo apresenta uma informação sobre animais de estimação, o tinpo de cada animal de estimação
# e o nome dele

def describe_pet(animal_type, pet_name):
    """Exibe informação sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'wolverine')

# Argumentos nomeados
describe_pet(animal_type = 'hamster', pet_name = 'harry')
# Nesse caso a ordem dos argumentos não importa, uma vez que foi informado a Python o parâmetro e qual argumento
# este corresponde:
describe_pet( pet_name = 'harry', animal_type = 'hamster')