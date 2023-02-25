# programa para implementar operadores aritmeticos

print("-----------------------------")
print("---operadodres aritmeticos---")
print("-----------------------------")

#input

x = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y: "))


# precesing

s = x + y
r = x - y
m = x * y
d = x / y
mod = x % y
de = x // y
p = x ** y

# output 

print("-----------------------------")
print("---------RESULTADOS----------")
print("-----------------------------")
print("suma: " + str(s))
print("resta: " + str(r))
print("multiplicacion: " + str(m))
print("division: " + str(d))
print("modulo: " + str(mod))
print("division entera: " + str(de))
print("potencia: " + str(p))