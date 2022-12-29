import math

a = 1
b = -1
c = -12

print("A = ", a)
print("B = ", b)
print("C = ", c)

delta = (b**2) - 4 * (a*c)

if delta <0:
    print("Delta Negativo")

else:
    print("DELTA = ", delta)

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print("X1 = ", x1)
    print("X2 = ", x2)