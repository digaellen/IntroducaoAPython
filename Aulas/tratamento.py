#Conceito de Tratamento de Exceções

a = 2
b = 0

'''print (a/b) vai dar erro, não dá pra dividir por 0'''


#Solução

try: #para ele testar uma funcionalidade
    print(a/b)

except: #se der erro, aparecer a mensagem de erro, e continua a execução do programa
    print("Nao e permitida a divisao por 0")

print(a/a)
