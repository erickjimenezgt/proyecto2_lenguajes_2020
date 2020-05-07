#Menú Educación

#!/usr/bin/python3
import msvcrt
import os


global nombre_gramatica

#Funciones
if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

def ingresarNT():
    print("Ingresar NT")

def ingresarTerminales():
    print("Ingresar Terminales")

def ntInicial():
    print("NT inicial")

def producciones():
    print("Producciones")

def mostrarGramaticaTransformada():
    print("Mostrar gramática transformada")

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
    nombre_gramatica = nombre
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
    print ("1. Ingresar NT")
    print ("2. Ingresar Terminales")
    print ("3. NT Inicial")
    print ("4. Producciones")
    print ("5. Mostrar Gramática Transformada")
    print ("6. Ayuda")
    print ("7. Regresar a pantalla inicial")
    print ("Elige una opcion")
        
    while not salir:
        opcion = pedirNumeroEntero()
        if opcion == 1:
            ingresarNT()
        elif opcion == 2:
            ingresarTerminales()
        elif opcion == 3:
            ntInicial()
        elif opcion == 4:
            producciones()
        elif opcion == 5:
            mostrarGramaticaTransformada()
        elif opcion == 6:
            ayuda()
        elif opcion == 7:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            os.system("menu_principal.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
        else:
            print ("Introduce un numero entre 1 y 7")

print ("#######################  PROYECTO 1  #########################")
print ("####################### MENÚ GRAMÁTICA #########################")
print ("")
cadena = input("Introduce el nombre de la gramática: ")
asignar_nombre(cadena)
