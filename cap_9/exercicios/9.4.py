"""
    Pessoas Atendidas: Comece com seu programa do Exercício 9.1[página 225]. Acrescente um atributo
    chamado number_served cujo valor default é  0. Crie uma instância chamada restaurant a partir dessa
    classe. Apresente o número de clientes atendidos pelo restaurante e, em seguida, mude esse valor
    e exiba-o novamente.
"""
"""
    Acrescente um método chamadao set_number_served() que permita definir o número de clientes atendidos.
    Chame esse método com um novo número e mostre o valor novamente.
    Acrescente um método chamado increment_number_served() que permita incrementar o número de clientes
    servidos. Chame este método com qualquero número que você quiser e que represente quantos clientes
    foram atendidos, por exemplo, em um dia de funcionamento.
"""

# Relembrando o Exercício 9.1[página 225]

"""
    Restaurante: crie uma classe chamada Restaurant. O método ___init___() de Restaurant
    deve armazenar dois atributos: restaurant_name e cuisine_type. Crie um método chamadao
    describe_restaurant() que mostre essas duas informações, e um método de nome open_restaurant()
    que exiba uma mensagem informando que o restaurante está aberto.
    Crie uma instancia chamada restaurant a partir de sua classe. Mostre os dois atributos
    individualmente e, em seguida, chame os dois métodos.
"""

class Restaurant():
    """Tentativa simples de simular um restaurante."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    # acrescentando o atributo number_served() com default = 0
        self.number_served = 0
    
    def describe_restaurant(self):
        """Retorna a descrição do restaurante - nome e culinária."""
        description = 'O restaurante ' + self.restaurant_name.title() + ' é espeicalista na culinária ' + self.cuisine_type.title() + ';'
        return description

    def open_served(self):
        """Retorna o horário de funcionamento do restaurante."""
        time_function = self.restaurant_name + ' está aberto das 11h30min às 22h00min.'
        return time_function
    
    # método que chama o novo atributo number_served
    def read_number(self):
        """Retorna o número de clientes atendidos."""
        parcial_number = 'Estão sendo atendidos ' + str(self.number_served) + ' clientes.'
        return parcial_number

    # cria um método para alterar o atributo number_served
    def update_number(self, clientes):
        """Define o valor do atributo number_served"""
        self.number_served = clientes

    # cria um método para incrementar o valor do atributo number-served
    def increment_number(self, clientes):
        """Define o valor atualizado do atributo number_served."""
        self.number_served += clientes

restaurant = Restaurant('Xian', 'Chinesa')
print('\n' + restaurant.describe_restaurant())
print(restaurant.open_served())

# cria uma instância restaurant e chama o método read.number()
print(restaurant.read_number())

# aterando o valor do atibuto number_serverd diretamente
restaurant = Restaurant('CheFranco', 'Japonesa')
print('\n' + restaurant.describe_restaurant())
print(restaurant.open_served())

restaurant.number_served = 25
print(restaurant.read_number())

# alterando o valor do atributo através de um método
restaurant = Restaurant('O Rei do Galeto', 'Grega')
print('\n' + restaurant.describe_restaurant())
print(restaurant.open_served())
restaurant.update_number(15)
print(restaurant.read_number())

# incrementando o valor de um atributo
restaurant = Restaurant('Parmegiano', 'Italiana')
print('\n' + restaurant.describe_restaurant())
print(restaurant.open_served())
restaurant.update_number(15)
restaurant.read_number()
restaurant.increment_number(20)
print(restaurant.read_number())