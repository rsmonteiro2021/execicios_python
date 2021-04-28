#Trabalhando com parte de uma lista. Fatiando uma lista.
#Suponha que temos uma lista de nossos alimentos prediletos e queremos criar uma lista separada de comidas que um amigo gosta. Esse amigo gosta de tudo que
#está na nossa lista até agora, portanto, podemos criar uma lista copiando a nossa:

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#não funciona do mesmo jeito se fizermos fried_foods = my_foods, cada alimento acrescentado será acrescentado nas duas listas, portanto, não teríamos duas listas independentes.
