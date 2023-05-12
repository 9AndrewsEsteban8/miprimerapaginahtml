lista=[]
print("TABLA DE MULTIPLICAR")
for i in range(1,11):
  for j in range(1,11):
    lista.append(i*j) 
  print(lista)
  lista.clear()
