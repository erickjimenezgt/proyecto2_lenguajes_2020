#Menú Educación

#!/usr/bin/python3
import msvcrt
import os
import numpy as np


global nombre_afd

#Funciones
if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

class AFD:
    def ingresarEstados(parametro):
        os.system(var) #Limpiamos o cambiamos pantalla
        os.system("ingresar_estados.py "+parametro)

    def ingresarAlfabeto():
        print("Ingresar Alfabeto")

    def estadoInicial():
        print("Estado Inicial")

    def estadoAceptacion():
        print("Estado de aceptación")

    def transiciones():
        print("Transiciones")

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
    nombre_afd = nombre
    if buscarAFD(nombre_afd) == 't':
        print ("El nombre del AFD ya existe. Por favor, ingresa uno diferente.")
        pedir_nombre()
    else:
        f = open('datos_afd_manual.txt','a')
        f.write('\n'+nombre+';')
        f.close()
        mostrar_menu(nombre_afd)

def buscarAFD(nombre_afd):
        list = []
        list2 = []
        list3 = []
        respuesta = 'f'
        cadena_datos = ''
        archivo = open("datos_afd_manual.txt", "r")
        for linea in archivo.readlines():
            list = linea.split(";")
            if list[0] == nombre_afd:
                list2 = list[1].split(",")
                if list2[0] == 'estados':
                        respuesta = 't'
                else:
                    respuesta = 'f'
            else:
                respuesta = 'f'
        archivo.close()
        return respuesta

def pedir_nombre():
    cadena = input("Introduce el nombre del AFD: ")
    asignar_nombre(cadena)

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

def mostrar_menu(xxx):
    salir = False
    opcion = 0
    
    print ("")
    print ("1. Ingresar estados")
    print ("2. Ingresar alfabeto")
    print ("3. Estado inicial")
    print ("4. Estado de aceptación")
    print ("5. Transiciones")
    print ("6. Ayuda")
    print ("7. Regresar a pantalla inicial")
    print ("Elige una opcion")
        
    while not salir:
        opcion = pedirNumeroEntero()
        if opcion == 1:
            salir = True
            AFD.ingresarEstados(xxx)
        elif opcion == 2:
            AFD.ingresarAlfabeto()
        elif opcion == 3:
            AFD.estadoInicial()
        elif opcion == 4:
            AFD.estadoAceptacion()
        elif opcion == 5:
            AFD.transiciones()
        elif opcion == 6:
            AFD.ayuda()
        elif opcion == 7:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            os.system("menu_principal.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
        else:
            print ("Introduce un numero entre 1 y 7")

print ("#######################  PROYECTO 1  #########################")
print ("####################### MENÚ AFD #########################")
print ("")
pedir_nombre()


