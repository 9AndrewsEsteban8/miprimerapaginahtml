Lista = [];
suma = int();
n = int(input("Ingrese la cantidad de números:"))
for i in range(0,n):
  num = int(input("Introduce el número: "))
  Lista.append(num)
  suma = suma + num
print("La suma de los numeros es: ")
print(suma)

