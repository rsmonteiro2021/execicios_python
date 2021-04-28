#Crie uma lista de múltiplos de 3, de 3 a 30. Use o laço for para exibir os números de sua lista.

#Opção 1:

lista = []
for multiplo in range(1,11):
    multiplos = multiplo * 3
    lista.append(multiplos)
print(lista)

#opção 2:

#numeros_impares = []
#x = 1
#while True:
    #if x <= 20:
        #numeros_impares.append(x)
        #x += 2
    #else:
        #print(numeros_impares)
        #break
