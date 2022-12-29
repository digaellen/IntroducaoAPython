print("\n ***CALCULO DE NOTAS*** \n")

nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("\nDigite sua nota 2: "))

media = (nota1+nota2)/2

if media >= 6:
    print("\nSua media e: ", media)
    print("APROVADO\n\n")
else:
    print("\nSua media e: ", media)
    print("REPROVADO\n\n")