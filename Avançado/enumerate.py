lista = ["abacate", "bola", "cachorro"]
for i in lista: #vai imprimir os itens da lista
    print(i) 
###  saida: abacate
###         bola
###         cachorro


for i in range(len(lista)): #range vai criar um vetor e o len vai medir o tamanho
    print(i, lista[i])
###  saida: 0 abacate
###         1 bola
###         2 cachorro



#MELHOR MANEIRA É COM O ENUMERATE

for i, nome in enumerate(lista): #imprime o item e o nome na frente
    print(i, nome),
###  saida: 0 abacate
###         1 bola
###         2 cachorro