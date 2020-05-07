#Menú Educación

#!/usr/bin/python3
import msvcrt
import os


global nombre_gramatica_cadena

#Funciones
if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

def cargarAFD():
    print("Cargar AFD")

def cargarGramatica():
    print("Cargar Gramática")

def pedirNumeroEntero(): #Función que revisa si es número entero o no
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("\nIntroduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

def mostrar_menu():
    salir = False
    opcion = 0

    print ("")
    print ("1. Cargar AFD")
    print ("2. Cargar Gramática")
    print ("3. Regresar a pantalla inicial")
    print ("Elige una opcion")
        
    while not salir:
        opcion = pedirNumeroEntero()
        if opcion == 1:
            cargarAFD()
        elif opcion == 2:
            cargarGramatica()
        elif opcion == 3:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            os.system("menu_principal.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
        else:
            print ("Introduce un numero entre 1 y 3")

print ("#######################  PROYECTO 1  #########################")
print ("####################### MENÚ CARGAR ARCHIVOS #########################")
print ("")
mostrar_menu()


