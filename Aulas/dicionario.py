#a chave é o que está em primeira posição, antes do :
dicionario = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}

#chama a chave e imprime o conteúdo dentro dessa chave
print(dicionario["A"]) 

#navegação por cada item
for chave in dicionario:
    print(chave+"-"+dicionario[chave]) #imprime a chave separando o valor por um -
    print(dicionario[chave]) #imprime só o valor depois da chave


#separa chave+valor dentro do meu dicionario
#tupla: conjunto de dados imutáveis \ parecido com as listas
for chave in dicionario.items():
    print(chave)

#para retornar só os valores
for chave in dicionario.values():
    print(chave)

#para retornar só as chaves
for chave in dicionario.keys():
    print(chave)