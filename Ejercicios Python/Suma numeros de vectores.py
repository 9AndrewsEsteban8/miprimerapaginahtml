numeros1=[]
numeros2=[]
suma=[]
n=int(input("Ingrese la cantidad de números a ingresar: "))
for i in range(0,n):
  numeros1.append(int(input("Ingrese número "+ str(i +1 )+ " de la primera lista:")))
  numeros2.append(int(input("Ingrese número "+ str(i +1 )+ " de la segunda lista:")))
  suma.append(numeros1[i] + numeros2[i])
print("La primera lista es: "+ str(numeros1))
print("La segunda lista es: "+ str(numeros2))
print("La suma de los números es: "+str(suma))

