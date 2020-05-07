#!/usr/bin/python3
import msvcrt
import os

#Funciones
var = ""
if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

def asignar_nombre(nombre):
    nombre_afd = nombre
    if buscarAFD(nombre_afd) == 't':
        print ("El nombre del AFD ya existe. Por favor, ingresa uno diferente.")
        pedir_nombre()
    else:
        f = open('datos_afd_manual.txt','a')
        f.write('\n'+nombre+';')
        f.close()
        mostrar_menu(nombre_afd)

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


print ("#######################  PROYECTO 1  #########################")
print ("####################### MENÚ PRINCIPAL #########################")

salir = False
opcion = 0

print ("1. Crear AFD")
print ("2. Crear gramática")
print ("3. Evaluar cadenas")
print ("4. Reportes")
print ("5. Cargar archivo de entrada")
print ("6. Guardar")
print ("7. Salir")
print ("Elige una opcion")
    
while not salir:

    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        salir = True
        os.system(var) #Limpiamos o cambiamos pantalla
        #os.system("menu_afd.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
        mostrar_menu("hola")
    elif opcion == 2:
        salir = True
        os.system(var) #Limpiamos o cambiamos pantalla
        os.system("menu_gramatica.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
    elif opcion == 3:
        salir = True
        os.system(var) #Limpiamos o cambiamos pantalla
        os.system("menu_evaluar_cadena.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
    elif opcion == 4:
        salir = True
        os.system(var) #Limpiamos o cambiamos pantalla
        os.system("menu_reportes.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
    elif opcion == 5:
        salir = True
        os.system(var) #Limpiamos o cambiamos pantalla
        os.system("menu_cargar_archivos.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
    elif opcion == 6:
        salir = True
        os.system(var) #Limpiamos o cambiamos pantalla
        os.system("menu_guardar.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
    elif opcion == 7:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 7")

print ("Fin")
