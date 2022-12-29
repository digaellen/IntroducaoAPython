lista = [1,2,3,4,5] 
lista_quadrado = [] #essa lista vai receber cada elemento da lista 1, ao quadrado

for numero in lista:
    lista_quadrado.append(numero**2)

print(lista)
print(lista_quadrado)

#saída: [1, 2, 3, 4, 5]
#       [1, 4, 9, 16, 25]

### forma mais simples de fazer essa mesma lista:

lista = [1,2,3,4,5] 
lista_quadrado = [numero**2 for numero in lista] #[valor / laço / condição]
print ("Usando LIST COMPREHENSION")
print(lista)
print(lista_quadrado)

#saída: Usando LIST COMPREHENSION
#       [1, 2, 3, 4, 5]
#       [1, 4, 9, 16, 25]


lista = [1,2,3,4,5] 
lista_quadrado = [numero**2 for numero in lista]
lista_impares = [impar for impar in lista    if impar%2==1] ##se o resto da divisão do número for 1, ele salva na lista de ímpares.

print (lista_impares)
# saída: [1, 3, 5]