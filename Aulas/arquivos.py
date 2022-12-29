#-*- coding: utf-8 -*-

arquivo = open("arquivo.txt", "r") #vai me mostrar qual é o tipo de arquivo
print (arquivo)

texto = arquivo.read()
print(texto)

w = open("arquivo2.txt", "w") #criando um novo arquivo, ou substituindo um existente
w.write("esse eh o meu arquivo \n")
w.close()

arquivo2 = open("arquivo2.txt")
leitura = arquivo2.read()
print(leitura)

a = open("arquivo.txt", "a") #ler e adicionar uma nova linha ao texto
a.write("o A adiciona mais uma linha \n")
a.close()

arquivo3 = open("arquivo.txt")
leitura = arquivo3.read()
print(leitura)