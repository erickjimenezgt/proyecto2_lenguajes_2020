#Menú Educación

#!/usr/bin/python3
import msvcrt
import os

#Funciones
if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"
   
def pedirNumeroEntero(): #Función que revisa si es número entero o no
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

print ("####################### MENÚ EDUCACIÓN #########################")

salir = False
opcion = 0

print ("1. Cargar archivo con extensión .edu")
print ("1. Cargar archivo con extensión .almacen")
print ("3. Regresar a pantalla inicial")
print ("Elige una opcion")
    
while not salir:
    opcion = pedirNumeroEntero()
    if opcion == 1:
        print ("Opcion 1")
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        salir = True
        os.system(var) #Limpiamos o cambiamos pantalla
        os.system("prueba.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
    else:
        print ("Introduce un numero entre 1 y 3")
        
