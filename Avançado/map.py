#função para calcular o dobro de um número
def dobro(x):
    return x*2

valor1 = 2
valor2 = [1,2,3,4,5]

print(dobro(valor1))
###   saida: 4


#Se for com vários valores, fica assim:
print (dobro(valor2)) #não funciona, ele imprime a lista 2 vezes
###   saida: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


#Pra resolver, utilizamos a função MAP da seguinte forma:
valor_dobrado = map(dobro, valor2) #(valor, lista)
valor_dobrado = list(valor_dobrado) #transformo essa variavel numa lista
print(valor_dobrado)
###   saida: [2, 4, 6, 8, 10]