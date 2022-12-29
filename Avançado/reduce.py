from functools import reduce

def soma(x,y):
    return x+y

lista = [2,5,8,7,1] ## resultado: 23

soma = reduce(soma, lista) 
#pra cada elemento da lista, ele vai obter o valor e vai somar.
# x vai receber o elemento da lista, e o y vai receber o montante da soma.

print(soma)
###    saída: 23