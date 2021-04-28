#Números Ímpares: Use o tereiro argumento da função range() para criar uma lista de números ímpares de 1 a 20. Utilize uma laço for para exibir os números.

#Opção 1:

#for impares in range(1,21,2):
    #print(impares)

#opção 2:

numeros_impares = []
x = 1
while True:
    if x <= 20:
        numeros_impares.append(x)
        x += 2
    else:
        print(numeros_impares)
        break
