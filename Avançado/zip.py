lista1 = [1,2,3,4,5]
lista2 = ["abacate", "bola", "cachorro", "dado", "escada"]
lista3 = ["R$ 3,50", "R$ 5,00", "R$ 0,00", "R$ 1,20", "R$ 80,00"]

#FUNCAO ZIP compacta 2 listas como se fossem uma única lista utilizando o laço for

for numero, nome, preco in zip(lista1, lista2, lista3):
    print(numero, nome, preco)
#ele vai pegar o primeiro item da lista 1 e jogar pra numero
#e em seguida, o primeiro item da lista 2 e jogar pra nome
#e em seguida, o primeiro item da lista 3 e jogar pra preco

###   saída:
#            1 abacate R$ 3,50
#            2 bola R$ 5,00
#            3 cachorro R$ 0,00
#            4 dado R$ 1,20
#            5 escada R$ 80,00