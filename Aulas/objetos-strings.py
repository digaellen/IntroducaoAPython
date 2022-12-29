'''#a = "Ellen"
b = "Camila"

nome = a + " " + b

print (nome)
print (len(nome)) #o Len conta a quantidade de caracteres dentro de uma string

sequencia = "ABCD EFGH IJKL MNOP"
letra = sequencia[8] #entre chaves, está o único caractere que a variável letra vai buscar.
O número é sempre -1 pois a contagem inicia em 0, e espaços contam como caracteres
print (letra)

print(sequencia.lower())

print (nome.upper())
print (nome)
'''

frase = "O rato roeu a roupa do rei de Roma"
print(frase.split())
print(frase.find("rei"))
busca = frase.find("rei")
print(frase[busca:])
frase = frase.replace("o rei", "a rainha")
print(frase)