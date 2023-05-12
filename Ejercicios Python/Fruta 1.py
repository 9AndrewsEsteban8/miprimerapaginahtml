serpList = ["Manzana", "Melón", "Uva", "Mango","Cereza"]
for i in range(0,5):
  print(serpList[i])
  fin = len(serpList[i])
  for j in range(0,fin+1):
    print(serpList[i][j-1:j])
