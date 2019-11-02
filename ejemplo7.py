#Calcular el area lateral del tronco de cono de revolucion
area_lateral, pi, radio_mayor, radio_menor, generatriz=0.0, 0.0, 0, 0, 0.0

#Asignacion de valores
pi=3.14
radio_mayor=5
radio_menor=3
generatriz=6.1

#Calculo
area_lateral=(radio_mayor+radio_menor)*generatriz*pi

#Mostrar valores
print ("pi", pi)
print ("radio mayor", radio_mayor)
print ("radio menor", radio_menor)
print ("generatriz", generatriz)
print ("el area lateral del tronco de cono", area_lateral)
