numero1 = int(input("Digite um numero: "))
sinal = input("Digite o sinal: ")
numero2 = int(input("Digite outro numero: "))

if sinal == "+":
    operacao = numero1 + numero2

elif sinal == "-":
    operacao = numero1 - numero2

elif sinal == "/":
    operacao = numero1 / numero2

elif sinal == "*":
    operacao = numero1 * numero2

else:
    print("Sinal Invalido")

print("Resultado: ", operacao)