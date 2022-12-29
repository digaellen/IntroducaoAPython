import random


#o random escolhe um número aleatório entre 0 e 10
numero_aleatorio = random.randint(0,10)
print(numero_aleatorio)

#para forçar a escolher o mesmo número
random.seed(1)
numero_forcado = random.randint(0,10)
print (numero_forcado)


#para escolher o número de uma lista
lista = [85,7,3]
numero_lista = random.choice(lista)
print (numero_lista)