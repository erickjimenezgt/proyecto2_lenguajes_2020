#Menú Educación

#!/usr/bin/python3
import msvcrt
import os
import numpy as np


#Funciones
if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

#print ("los parametros recibidos son :")
#for i in range(len(os.sys.argv)):
#    print ("valor %s : %s" % (i,os.sys.argv[i]))

class Estado:    
    C_ClfGtLabels = []
    lst = list(C_ClfGtLabels)
    def guardarEstado(estado, l):
        if estado:
            if estado.isdigit():
                print("Puedes ingresar solo letras mayúsculas, no números.")
            else:
                estado = estado[0:1] 
                estado = estado.upper()
                if estado in l: # Imprime lo de abajo
                    print ("El estado "+estado+ " ya existe en el AFD. Por favor, ingresa otro estado.")
                else:
                    if Estado.buscarAlfabeto(estado,os.sys.argv[1]) == 't':
                        print ("El estado ya existe como alfabeto del lenguaje de " + os.sys.argv[1] + ", por favor ingresa otro estado.")
                    else:      
                        l.append(estado)
                        C_ClfGtLabels = np.asarray(l)
                        print(C_ClfGtLabels)
        else:
            print("No puedes ingresar un estado vacio. Por ingresa un estado.")
        
    def buscarAlfabeto(estadoxx,nombre_afd):
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
                if list2[0] == 'alfabeto':
                    cadena_datos = list2[1]
                    if estadoxx in cadena_datos:
                        respuesta = 't'
                    else:
                        respuesta = 'f'
                else:
                    respuesta = 'f'
            else:
                respuesta = 'f'
        archivo.close()
        return respuesta




        #arr = np.array([1, 2, 3])
        #arr = np.append(arr,estado)
        #print(arr)

def mostrar_menu():
    salir = False
    opcion = 0

    print ("")
    print ("Escriba salir para regresar al menú anterior o ingrese el estado: ")

    while not salir:
        estado = input("Estado: ")
        if estado == "salir":
            f = open('datos_afd_manual.txt','a')
            f.write("estados,")
            f.write("".join(map(str, Estado.lst)))
            f.close()
            #with open(r'datos_afd_manual.txt', 'w') as f:
            #    f.write("".join(map(str, Estado.lst)))
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            os.system("menu_afd.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
        else:
            Estado.guardarEstado(estado, Estado.lst)
            
#import menu_afd as mafd

print ("#######################  PROYECTO 1  #########################")
print ("####################### MENÚ AFD >> Ingresar Estados de "+ os.sys.argv[1] +"  #########################")
print ("")
mostrar_menu()
#buscarAFD("hola")



