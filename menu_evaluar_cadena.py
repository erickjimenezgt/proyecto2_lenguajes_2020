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

def soloValidar():
    print("Solo validar")

def rutaAFD():
    print("Ruta AFD")

def expandirConGramatica():
    print("Expandir con gramática")

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
    nombre_gramatica_cadena = nombre
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
    print ("1. Sólo validar")
    print ("2. Ruta en AFD")
    print ("3. Expandir con gramática")
    print ("4. Ayuda")
    print ("5. Regresar a pantalla inicial")
    print ("Elige una opcion")
        
    while not salir:
        opcion = pedirNumeroEntero()
        if opcion == 1:
            soloValidar()
        elif opcion == 2:
            rutaAFD()
        elif opcion == 3:
            expandirConGramatica()
        elif opcion == 4:
            ayuda()
        elif opcion == 5:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            os.system("menu_principal.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
        else:
            print ("Introduce un numero entre 1 y 5")

print ("#######################  PROYECTO 1  #########################")
print ("####################### MENÚ EVALUAR CADENA #########################")
print ("")
cadena = input("Introduce el nombre de la gramática: ")
asignar_nombre(cadena)
