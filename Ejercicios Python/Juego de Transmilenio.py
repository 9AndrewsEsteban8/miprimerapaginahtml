print("Acabas de ingresar a una travesia urbana 🏛️  inesperada; tu mision es llegar a clase 📖 temprano; debes tomar la mejor desición para cumplir tu objetivo, recuerda ser tolerante, respetar a los demás, no olvides la dirección de tu viaje. Pista ( es la superior de los puntos cardinales). ¡buena suerte! 🧭")
seleccion = int(input("Estas esperando el alimentador, pero en 20 minutos no ha pasado. \n¿Que vas a hacer? \n1. Esperar ⏳\n2. Coger un taxi hasta la estación más cercana 🚕 \n3. Coger el proximo el SITP lleno que pase y bajarse en una estación  más cercana 🚌\n"))
if (seleccion == 1):
  print("Que buena eleccion, la paciencia es virtud de sabios, el alimentador paso a los 30 segundos.")

  print("Una dama en condición de embarazo 🤰 te pide la silla💺. \n1. Te    haces el dormido😴 \n2. Le das la silla 💺 \n3. Le dices que pida la silla azul 😖")
  seleccion = int(input(""))
  if(seleccion == 1):
    print("Una viejita 👵 te dio un codazo porque sabe que estan fingiendo y te pide que le des la silla, generando una discución 🤼 que te hace llegar tarde.")
  elif (seleccion == 2):
    print("¡Que buena elección!, ser amable con los demás es la clave para restaurar la sociedad 🏙️")
    print("Llegate al Portal🅿️, debes pasar el  torniquete. \n1. Te colas para ahorar dinero 💵\n2. Intentas pasar con la tarjeta para que te preste un pasaje 💳 ")
    seleccion = int(input(""))
    if (seleccion == 1):
      print("Fuiste capturado por la policia 👮, llegando tarde y con un comparendo")
    else:
      print("Afortunadamente tu tarjeta de deja pasar 🤞.")
      print("¿Qué ruta vas a tomar. \n1. D20 (Occidente) ⬅️  \n2. H15 (Sur) ⬇️ \n3. B3 (Norte) ⬆️")
      seleccion = int(input(""))
      if(seleccion == 1):
        print("Esta ruta toma la Calle 80, tu estudiar al Norte de la Ciudad ¡Pendejo! 🤓")
      elif(seleccion == 2):
          print("Los H se dirigen al Sur, tu estudias hacia el Norte, Perdiste. ↪️") 
      else:
        print("Bien, ahora se sube un vendedor a ofrecer dulces 🍬.\n¿Le compras? \n1. Si \n2. No")
        seleccion = int(input(""))
        if (seleccion == 1):
          print("Bien, la cara de malandrin 🔪 no se la quitaba nadie, por comprarle te has salvado.")
          print("Te bajaste de la estación, pero alcanzas a visualizar al vendedor hablando con sus compañeros y mirandote extraño 🕵️. Debes tomar una desicion \n1. Correr 🏃 \n2. Avisarle a la policia 👮. \n3. Comprarle más dulces al vendedor🍬")
          seleccion = int(input(""))
          if (seleccion == 1):
            print("Te salvaste, fue la mejor desición que pudiste tomar.\nLlegaste a la universidad Sano y Salvo con 5 minutos de anticipo 🎖️.\nGracias por jugar")
          elif (seleccion == 2):
            print("La Policia 👮 no te ayudo, te robaron.")
          else:
             print("Te robaron 🔪.Perdiste")
            
        else:
          print("Te han pegado una puñalada 🔪 por no comprar.")  
  else:
    print("Un señor te pega por contestón, y llegas tarde con el ojo morado.🥵")
    
elif (seleccion == 2):
  print("Solo tienes dinero suficientes quisas para comprar unos dulces🍬, Perdiste.")
else :
  print("El SITP 🚌 va muy lleno y no puedes subirte, Perdiste.")

