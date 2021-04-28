#Fatias: usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que faça o seguinte:
#1 Exiba a mensagem: Os tres primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
#2 Exiba a mensagem: os três itens do meio da lista são: Use uma fatia para exibir os três itens do meio da lista.
#3 Exiba a mensagem: os três últimos itnes da lista são: Use uma fatia para exibir os três últimos itens da lista.

#Resposta:

cubos = []
for numero in range(1,11):
    cubo = numero ** 3
    cubos.append(cubo)

print("Os três primeiros itens da lista são:")
print(cubos[0:3])

print("Os três itens do meio da lista são:")
print(cubos[3:6])

print("Os três últimos itens da lista são:")
print(cubos[7:11])

print("Essa é a lista completa:")
print(cubos)
