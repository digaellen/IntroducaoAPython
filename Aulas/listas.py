lista_frutas = ["abacaxi", "banana", "coco", "damasco"]
lista_numeros = [1,2,3,4,5]
lista_mista = ["amor", True, 0.1, 800]

print (lista_frutas)
print (lista_numeros)
print (lista_mista)

#printar elemento 2 da lista de frutas
print(lista_frutas[1])

#para imprimir item por item
for item in lista_frutas:
    print(item)

#para saber o tamanho da lista
tamanho = len(lista_frutas)
print(tamanho)

#para adicionar elementos à lista
lista_frutas.append("limao")
print(lista_frutas)

#verificar se o elemento pertence a minha lista
if 3 in lista_numeros:
    print("3 esta na linha")

#para remover itens na lista
del lista_numeros[2:] #remove da posição 2 até o final
print(lista_numeros)

lista_desordenada = [125,478,632,1,2,5,8,9,6,4,75,23,69]
lista_desordenada.sort() #só altera a lista que já existe
lista = sorted(lista_desordenada) #retorna uma lista ordenada
print(lista_desordenada)

#para ordenar decrescente
lista_desordenada.sort(reverse=True)
print (lista_desordenada)

#para reverter a lista, deixando o último elemento como primeiro
lista_desordenada.reverse()
print(lista_desordenada)

lista_aleatoria = ["bola", "abacate", "caneta", "dinheiro"]
lista_aleatoria.sort() #vai ordenar em ordem alfabetica
print(lista_aleatoria)

lista_aleatoria.sort(reverse = True) #vai ordenar do Z ao A
print(lista_aleatoria)