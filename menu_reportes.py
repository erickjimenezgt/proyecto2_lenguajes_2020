#Menú Educación

#!/usr/bin/python3
import msvcrt
import os


global nombre_gramatica_afd_cadena

#Funciones
if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

def verDetalle():
    print("Ver detalle")

def generarReporte():
    print("Generar reporte")

def ayuda():
    print ("")
    print ("Curso: Lenguajes Formales y de Programación")
    print ("Sección: B-")
    print ("Carnet: 201603171")
    print ("Nombre estudiante: Erick Erasmo Jiménez Palacios")
    print ("Nombre auxiliar: Luis Yela")
    print ("Último dígito de carnet: 1")
    print ("")

def asignar_nombre(nombre):
    nombre_gramatica_afd_cadena = nombre
    mostrar_menu()

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
    print ("1. Ver detalle")
    print ("2. Generar reporte")
    print ("3. Ayuda")
    print ("4. Regresar a pantalla inicial")
    print ("Elige una opcion")
        
    while not salir:
        opcion = pedirNumeroEntero()
        if opcion == 1:
            verDetalle()
        elif opcion == 2:
            generarReporte()
        elif opcion == 3:
            ayuda()
        elif opcion == 4:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            os.system("menu_principal.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
        else:
            print ("Introduce un numero entre 1 y 4")

print ("#######################  PROYECTO 1  #########################")
print ("####################### MENÚ DE REPORTES #########################")
print ("")
cadena = input("Introduce el nombre de la gramática o AFD: ")
asignar_nombre(cadena)