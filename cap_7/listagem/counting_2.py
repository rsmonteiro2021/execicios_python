# O laço while a seguir conta de 1 a 10 utilizando a função continue.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)