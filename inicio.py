#Proyecto 1 - Lenguajes de Programación
#!/usr/bin/python3
import msvcrt
import os
import numpy as np
import string
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from graphviz import Digraph
import graphviz as gv
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image,Frame,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import A4
from datetime import date
from datetime import datetime
import random
from PIL import Image
import pathlib
import csv
import pandas as pd
from tabulate import tabulate
import pydot

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

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
            num = int(input("\nElige una opción. Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

def ayuda():
        print ("")
        print ("Curso: Lenguajes Formales y de Programación")
        print ("Sección: B-")
        print ("Carnet: 201603171")
        print ("Nombre estudiante: Erick Erasmo Jiménez Palacios")
        print ("Nombre auxiliar: Luis Yela")
        print ("Último dígito de carnet: 1")
        print ("")

def pedir_nombre_grm_tipo2():
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ Ingresar / Modificar Gramática #########################")
        print ("")
        cadena = input("Introduce el nombre de la gramática o escribe salir para regresar al menú de gramática: ")
        if cadena == 'salir':
            os.system(var) #Limpiamos o cambiamos pantalla
            menu_general_grm_tipo2()
        else:
            if(len(cadena)==0):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm_tipo2()
            elif (cadena.isspace()):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm_tipo2()
        return cadena

def pedir_nombre_grm_tipo2_visualizar_automata():
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ Visualizar Autómata y la sextupla de la misma #########################")
        print ("")
        cadena = input("Introduce el nombre de la gramática asociada al autómata a visualizar: ")
        if cadena == 'salir':
            os.system(var) #Limpiamos o cambiamos pantalla
            menu_general_grm_tipo2()
        else:
            if(len(cadena)==0):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm_tipo2_visualizar_automata()
            elif (cadena.isspace()):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm_tipo2_visualizar_automata()
        return cadena

def pedir_direccion_imagen_grm_tipo2_visualizar_automata():
        cadena = input("Introduce una dirección donde puede estar guardada la imagen: ")
        if cadena == 'salir':
            os.system(var) #Limpiamos o cambiamos pantalla
            menu_general_grm_tipo2()
        else:
            if(len(cadena)==0):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_direccion_imagen_grm_tipo2_visualizar_automata()
            elif (cadena.isspace()):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_direccion_imagen_grm_tipo2_visualizar_automata()
        return cadena

def pedir_nombre_grm_tipo2_generar_automata():
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ GENERAR AUTÓMATA #########################")
        print ("")
        cadena = input("Introduce el nombre de la gramática asociada al autómata a generar: ")
        if cadena == 'salir':
            os.system(var) #Limpiamos o cambiamos pantalla
            menu_general_grm_tipo2()
        else:
            if(len(cadena)==0):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm_tipo2_generar_automata()
            elif (cadena.isspace()):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm_tipo2_generar_automata()
        return cadena

def pedir_nombre_grm_tipo2_evaluar_cadena():
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ Evaluar Cadena #########################")
        print ("")
        cadena = input("Introduce el nombre de la gramática asociada asociada a la cadena a evaluar: ")
        if cadena == 'salir':
            os.system(var) #Limpiamos o cambiamos pantalla
            menu_general_grm_tipo2()
        else:
            if(len(cadena)==0):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm_tipo2_evaluar_cadena()
            elif (cadena.isspace()):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm_tipo2_evaluar_cadena()
        return cadena



def pedir_nombre_afd():
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ AFD #########################")
        print ("")
        cadena = input("Introduce el nombre del AFD o escribe salir para regresar al menú principal: ")
        if cadena == 'salir':
            os.system(var) #Limpiamos o cambiamos pantalla
            MenuPrincipal.inicio()
        else:
            if(len(cadena)==0):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_afd()
            elif (cadena.isspace()):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_afd()
        return cadena

def pedir_nombre_grm():
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ GRAMÁTICA #########################")
        print ("")
        cadena = input("Introduce el nombre de la gramática o escribe salir para regresar al menú principal: ")
        if cadena == 'salir':
            os.system(var) #Limpiamos o cambiamos pantalla
            MenuPrincipal.inicio()
        else:
            if(len(cadena)==0):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm()
            elif (cadena.isspace()):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm()
        return cadena

def pedir_nombre_grm_ecad():
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ EVALUAR CADENAS #########################")
        print ("")
        cadena = input("Introduce el nombre de la gramática o escribe salir para regresar al menú principal: ")
        if cadena == 'salir':
            os.system(var) #Limpiamos o cambiamos pantalla
            MenuPrincipal.inicio()
        else:
            if(len(cadena)==0):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm()
            elif (cadena.isspace()):
                print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
                pedir_nombre_grm()
        return cadena

def pedir_nombre_reporte_grm():
    print ("#######################  PROYECTO 1  #########################")
    print ("####################### MENÚ REPORTE #########################")
    print ("")
    cadena = input("Introduce el nombre de la gramática o escribe salir para regresar al menú de reportes principal: ")
    if cadena == 'salir':
        os.system(var) #Limpiamos o cambiamos pantalla
        pedir_nombre_reporte()
    else:
        if(len(cadena)==0):
            print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
            pedir_nombre_reporte_grm()
        elif (cadena.isspace()):
            print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
            pedir_nombre_reporte_grm()
        else:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            cad = cadena
            xy = REPORTES(cad,"grm")
            xy.inicio()
    return cadena

def pedir_nombre_cargar_archivos_grm():
    print ("#######################  PROYECTO 1  #########################")
    print ("####################### MENÚ CARGAR ARCHIVO de Gramática (.grm) #########################")
    print ("")
    cadena = input("Introduce la dirección donde está alojada el archivo .grm o escribe salir para regresar al menú de cargar archivos principal: ")
    if cadena == 'salir':
        os.system(var) #Limpiamos o cambiamos pantalla
        pedir_nombre_cargar_archivo()
    else:
        if(len(cadena)==0):
            print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
            pedir_nombre_cargar_archivos_grm()
        elif (cadena.isspace()):
            print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
            pedir_nombre_cargar_archivos_grm()
        else:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            cad = cadena
            dam = pedir_nombre_archivo()
            xy = CA(cad,"grm",dam)
            xy.inicio()
    return cadena


def pedir_nombre_archivo():
    os.system(var)
    cadena = input("Introduce el nombre del archivo alojado en la dirección antes ingresada: ")
    if cadena == 'salir':
        os.system(var) #Limpiamos o cambiamos pantalla
        pedir_nombre_archivo()
    else:
        cadena = cadena
    return cadena

def pedir_nombre_reporte_afd():
    print ("#######################  PROYECTO 1  #########################")
    print ("####################### MENÚ REPORTE #########################")
    print ("")
    cadena = input("Introduce el nombre del AFD o escribe salir para regresar al menú de reportes principal: ")
    if cadena == 'salir':
        os.system(var) #Limpiamos o cambiamos pantalla
        pedir_nombre_reporte()
    else:
        if(len(cadena)==0):
            print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
            pedir_nombre_reporte_afd()
        elif (cadena.isspace()):
            print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
            pedir_nombre_reporte_afd()
        else:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            cad = cadena
            xy = REPORTES(cad,"afd")
            xy.inicio()
    return cadena

def pedir_nombre_cargar_archivos_afd():
    print ("#######################  PROYECTO 1  #########################")
    print ("####################### MENÚ CARGAR ARCHIVOS de AFD (.afd) #########################")
    print ("")
    cadena = input("Introduce la dirección donde está alojada el archivo .afd o escribe salir para regresar al menú de cargar archivos principal: ")
    if cadena == 'salir':
        os.system(var) #Limpiamos o cambiamos pantalla
        pedir_nombre_cargar_archivo()
    else:
        if(len(cadena)==0):
            print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
            pedir_nombre_cargar_archivos_afd()
        elif (cadena.isspace()):
            print ("El nombre no puede estar vacío. Por favor, ingresa un nombre.")
            pedir_nombre_cargar_archivos_afd()
        else:
             #Limpiamos o cambiamos pantalla
            cad = cadena
            dam = pedir_nombre_archivo()
            salir = True
            os.system(var)
            xy = CA(dam,"afd",cad)
            xy.inicio()
    return cadena

def pedir_nombre_reporte():
    print ("#######################  PROYECTO 1  #########################")
    print ("####################### MENÚ REPORTE #########################")
    print ("")
    print ("    1. Gramática")
    print ("    2. AFD")
    print ("    3. Regresar a pantalla inicial")

    salir = False
    opcion = 0
 
    while not salir:
        opcion = pedirNumeroEntero()
        if opcion == 1:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            pedir_nombre_reporte_grm()
        elif opcion == 2:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            pedir_nombre_reporte_afd()
        elif opcion == 3:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            MenuPrincipal.inicio()
        else:
            print ("Introduce un numero entre 1 y 3")

def pedir_nombre_cargar_archivo():
    print ("#######################  PROYECTO 1  #########################")
    print ("####################### MENÚ CARGAR ARCHIVO #########################")
    print ("")
    print ("    1. Gramática")
    print ("    2. AFD")
    print ("    3. Regresar a pantalla inicial")

    salir = False
    opcion = 0
 
    while not salir:
        opcion = pedirNumeroEntero()
        if opcion == 1:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            pedir_nombre_cargar_archivos_grm()
        elif opcion == 2:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            pedir_nombre_cargar_archivos_afd()
        elif opcion == 3:
            salir = True
            os.system(var) #Limpiamos o cambiamos pantalla
            MenuPrincipal.inicio()
        else:
            print ("Introduce un numero entre 1 y 3")

#
# **********************************  MENÚ AFD ******************************
#
class AFD:
    nombre = ''

    diccionario_afd_estados = dict() #Declaramos diccionario que contiene los nombres de AFDs y su conjunto de estados pertenecientes a cada uno
    diccionario_afd_alfabeto = dict() #Declaramos diccionario que contiene los nombres de AFDs y su conjunto de alfabeto pertenecientes a cada uno
    diccionario_afd_estado_inicial = dict() #Declaramos diccionario que contiene los estados iniciales del AFD
    diccionario_afd_estados_aceptacion = dict() #Declaramos diccionario que contiene los estados de aceptacion del AFD
    diccionario_afd_transiciones = dict() #Declaramos diccionario que contiene los estados de aceptacion del AFD
    diccionario_afd_transiciones_metodo2 = dict() #Declaramos diccionario el metodo 2 para reportes
    diccionario_afd_transiciones_metodo2_original = dict() #Declaramos diccionario el metodo 2 transformado a metodo 1 para usarlos en las validación de cadenas


    """diccionario_afd_alfabeto = {
        "erick" : "abcd52.#", "dam" : "RadDSp"
    }"""
    """diccionario_afd_estados = {
        "erick" : "abcd52.#", "dam" : "RadDSp"
    }"""

    listaEstadosAFD = []
    listaAlfabetoAFD = []
    listaEstadoInicialAFD = []
    listaEstadosAceptacionAFD = []
    listaTransicionesAFD = []
    listaTransicionesAFDmetodo2 = []


    def __init__(self, nombre): 
        self.nombre = nombre 

    def inicio(self):
        xy = AFD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ AFD #########################")
        xy.mostrar_menu(self.listaEstadosAFD, self.listaAlfabetoAFD, self.listaEstadoInicialAFD, self.listaEstadosAceptacionAFD, self.listaTransicionesAFD, self.listaTransicionesAFDmetodo2) #Pasamos los estados al menú con el propósito de borrarlos despúes

    def ingresarEstado(self):
        xy = AFD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ AFD >> Ingresar Estados de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_estado()

    def ingresarAlfabeto(self):
        xy = AFD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ AFD >> Ingresar símbolos del Alfabeto de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_alfabeto()

    def estadoInicial(self):
        xy = AFD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ AFD >> Ingresar Estado Inicial de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_estado_inicial()

    def estadoAceptacion(self):
        xy = AFD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ AFD >> Ingresar estados de aceptación de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_estados_aceptacion()

    def transiciones(self):
        xy = AFD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ AFD >> Menú Ingreso de Transiciones del AFD "+ self.nombre +"  #########################")
        print ("")
        xy.mostrar_menu_transiciones_afd()

    def metodo1_ingreso_transiciones(self):
        xy = AFD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ AFD >> Método 1 - Ingreso de Transiciones del AFD "+ self.nombre +"  #########################")
        print ("")
        xy.mostrar_menu_transiciones_afd_metodo1()

    def metodo2_ingreso_transiciones(self):
        xy = AFD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ AFD >> Método 2 - Ingreso de Transiciones del AFD "+ self.nombre +"  #########################")
        print ("")
        xy.mostrar_menu_transiciones_afd_metodo2()

    def recorrer_lista_estados(self):
        x = ''
        for i in self.listaEstadosAFD:
            x = x + i
        return x

    def recorrer_lista_alfabeto(self):
        x = ''
        for i in self.listaAlfabetoAFD:
            x = x + i
        return x

    def recorrer_lista_estados_aceptacion(self):
        x = ''
        for i in self.listaEstadosAceptacionAFD:
            x = x + i
        return x

    def recorrer_lista_transiciones_metodo1_afd(self):
        x = ''
        for i in self.listaTransicionesAFD:
            x = x + i
        return x

    def mostrar_menu(self, pendejo, pendejo_alfabeto, pendejo_estado_inicial, pendejo_estados_aceptacion, pendejo_lista_transiciones_afd, pendejo_lista_transiciones_afd_m2):
        xy = AFD(self.nombre)
        salir = False
        opcion = 0
        
        print ("")
        print ("    1. Ingresar estados")
        print ("    2. Ingresar alfabeto")
        print ("    3. Estado inicial")
        print ("    4. Estado de aceptación")
        print ("    5. Transiciones")
        print ("    6. Ayuda")
        print ("    7. Regresar a pantalla inicial")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.ingresarEstado()
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.ingresarAlfabeto()
            elif opcion == 3:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.estadoInicial()
            elif opcion == 4:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.estadoAceptacion()
            elif opcion == 5:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.transiciones()
            elif opcion == 6:
                ayuda()
            elif opcion == 7:
                pendejo.clear() #Borramos lista de estados
                pendejo_alfabeto.clear() #Borramos lista de alfabeto
                pendejo_estado_inicial.clear() # Borramos el estado inicial
                pendejo_estados_aceptacion.clear() #Borramos estados de aceptacion
                pendejo_lista_transiciones_afd.clear()
                pendejo_lista_transiciones_afd_m2.clear()
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                MenuPrincipal.inicio()
            else:
                print ("Introduce un numero entre 1 y 7")

    def guardar_estado(self,estado):
        xy = AFD(self.nombre)
        if estado:
            estado = estado[0:1] 
            estado = estado.upper()
            if estado.isdigit():
                print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
            else:
                if estado in self.listaEstadosAFD: # Imprime lo de abajo
                    print ("El estado "+estado+ " ya existe en el AFD "+ self.nombre +". Por favor, ingresa otro estado.")
                elif estado in string.ascii_uppercase:
                    if xy.diccionario_afd_alfabeto: #Verificamos que no esté vacio el diccionario del alfabeto
                        if self.nombre in xy.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                            if estado in xy.diccionario_afd_alfabeto[self.nombre]:
                                print ("El estado ya existe como alfabeto del lenguaje de " + self.nombre + ", por favor ingresa otro estado.")
                            else:
                                self.listaEstadosAFD.append(estado)
                                xy.diccionario_afd_estados.update({self.nombre:xy.recorrer_lista_estados()})
                                print ("Estados guardados: "+xy.diccionario_afd_estados[self.nombre])
                        else: 
                            self.listaEstadosAFD.append(estado)
                            xy.diccionario_afd_estados.update({self.nombre:xy.recorrer_lista_estados()})
                            print ("Estados guardados: "+xy.diccionario_afd_estados[self.nombre])
                    else:  
                        self.listaEstadosAFD.append(estado)
                        xy.diccionario_afd_estados.update({self.nombre:xy.recorrer_lista_estados()})
                        print ("Estados guardados: "+xy.diccionario_afd_estados[self.nombre])
                else:
                    print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
        else:
            print("No puedes ingresar un estado vacio. Por ingresa un estado.")

    def guardar_alfabeto(self,estado):
        xy = AFD(self.nombre)
        if estado:
            estado = estado[0:1] 
            estado = estado.lower()
            if (estado.isspace()):
                print ("No puedes ingresar simbolos vacios.")
            else:
                if estado in self.listaAlfabetoAFD: # Imprime lo de abajo
                    print ("El símbolo del alfabeto "+estado+ " ya existe en el AFD "+ self.nombre +". Por favor, ingrese otro símbolo del alfabeto.")
                elif xy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario del alfabeto
                    if self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                        if estado in xy.diccionario_afd_estados[self.nombre]:
                            print ("El símbolo del alfabeto ya existe como estado de " + self.nombre + ", por favor ingrese otro símbolo del alfabeto.")
                        else:
                            self.listaAlfabetoAFD.append(estado)
                            xy.diccionario_afd_alfabeto.update({self.nombre:xy.recorrer_lista_alfabeto()})
                            print ("Símbolos del alfabeto guardados: "+xy.diccionario_afd_alfabeto[self.nombre])
                    else: 
                        self.listaAlfabetoAFD.append(estado)
                        xy.diccionario_afd_alfabeto.update({self.nombre:xy.recorrer_lista_alfabeto()})
                        print ("Símbolos del alfabeto guardados: "+xy.diccionario_afd_alfabeto[self.nombre])
                else:  
                    self.listaAlfabetoAFD.append(estado)
                    xy.diccionario_afd_alfabeto.update({self.nombre:xy.recorrer_lista_alfabeto()})
                    print ("Símbolos del alfabeto guardados: "+xy.diccionario_afd_alfabeto[self.nombre])
        else:
            print("No puedes ingresar un estado vacio. Por ingresa un estado.")

    def guardar_estado_inicial(self,estado):
        xy = AFD(self.nombre)
        if estado:
            estado = estado[0:1] 
            estado = estado.upper()
            if estado.isdigit():
                print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
            else:
                if xy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario de estados de aceptacion
                    if self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                        if not estado in xy.diccionario_afd_estados[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                            print ("El estado ingresado no existe en los estados declarados del AFD: " + self.nombre)
                        else:
                            if estado in string.ascii_uppercase:
                                self.listaEstadoInicialAFD.clear()
                                self.listaEstadoInicialAFD.append(estado)
                                xy.diccionario_afd_estado_inicial.update({self.nombre:estado})
                                print ("Estado guardado exitosamente: "+xy.diccionario_afd_estado_inicial[self.nombre])
                    else:
                        print ("El estado ingresado no existe en los estados declarados del AFD: " + self.nombre)
                else:
                    print ("El estado ingresado no existe en los estados declarados del AFD: " + self.nombre)
        else:
            print("No puedes ingresar un estado vacio. Por ingresa un estado.")

    def guardar_estados_aceptacion(self,estado):
        xy = AFD(self.nombre)
        if estado:
            estado = estado[0:1] 
            estado = estado.upper()
            if estado.isdigit():
                print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
            else:
                if xy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario de estados de aceptacion
                    if self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                        if not estado in xy.diccionario_afd_estados[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                            print ("El estado ingresado no existe en los estados declarados del AFD: " + self.nombre)
                        else:
                            if estado in self.listaEstadosAceptacionAFD: # Imprime lo de abajo
                                print ("El estado de aceptación ingresado ya se encuentra registrado como estado aceptación de "+self.nombre+", por favor ingresa otro estado")
                            elif estado in string.ascii_uppercase:
                                self.listaEstadosAceptacionAFD.append(estado)
                                xy.diccionario_afd_estados_aceptacion.update({self.nombre:xy.recorrer_lista_estados_aceptacion()})
                                print ("Estados de aceptación guardados: "+xy.diccionario_afd_estados_aceptacion[self.nombre])
                            else:
                                print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
                    else:
                        print ("El estado ingresado no existe en los estados declarados del AFD: " + self.nombre)
                else:
                    print ("El estado ingresado no existe en los estados declarados del AFD: " + self.nombre)
        else:
            print("No puedes ingresar un estado de aceptación vacio. Por favor, ingresa un estado.")

    def revisar_doble_estado_transicion_metodo1(self,e1,s):
        estado1 = ""
        estado2 = ""
        simbolo = ""
        cadena1 = []
        cadena2 = []
        y = 'f'
        if self.listaTransicionesAFD:
            for x in self.listaTransicionesAFD:
                cadena1 = x.split(";")
                cadena2 = cadena1[0].split(",")
                simbolo = cadena1[1][0:1]
                estado1 = cadena2[0]
                estado2 = cadena2[1]
                if e1 == estado1 and s == simbolo:
                    y = 't'
        return y

    def guardar_transicion_metodo1(self,estado):
        xy = AFD(self.nombre)
        estado1 = ""
        estado2 = ""
        simbolo = ""
        cadena1 = []
        cadena2 = []

        lista1 = []
        pos_inicial1 = -1
        lista2 = []
        pos_inicial2 = -1
        posicion_coma = 0
        posicion_pc = 0

        if estado:
            if(len(estado)!=5):
                print ("Debes ingresar una notación a la vez, o puede que no ingresaste una transición completa. Por favor ingresa una sóla transición.")
            elif not ";" in estado:
                print ("No existe el caracter especial ';'en la cadena de texto. Por favor, ingresa una cadena de texto correta.")
            elif not "," in estado:
                print ("No existe el caracter especial ',' en la cadena de texto. Por favor, ingresa una cadena de texto correta.")
            elif ";" in estado and "," in estado:
                try:
                    while True:
                        pos_inicial1 = estado.index(',', pos_inicial1+1)
                        lista1.append(pos_inicial1)
                except ValueError: # cuando ya no se encuentre la letra
                    posicion_coma = lista1[0]
                try:
                    while True:
                        pos_inicial2 = estado.index(';', pos_inicial2+1)
                        lista2.append(pos_inicial2)
                except ValueError: # cuando ya no se encuentre la letra
                    posicion_pc = lista2[0]
                if posicion_coma!=1 or posicion_pc!=3:
                    print ("El orden ingresado de los caracteres es incorrecto, por favor ingresa una transición con el orden siguiente: Estado1,Estado2;simbolo")
                else:
                    cadena1 = estado.split(";")
                    cadena2 = cadena1[0].split(",")
                    simbolo = cadena1[1]
                    estado1 = cadena2[0]
                    estado2 = cadena2[1]
                    
                    estado1 = estado1.upper()
                    estado2 = estado2.upper()
                    simbolo = simbolo.lower()

                    if (simbolo.isspace()):
                        print("No puede haber una transición con epsilon, por favor intentalo de nuevo.")
                    elif estado1.isdigit():
                        print("El estado 1 sólo puede ser letras mayúsculas, no números ni caracteres extraños")
                    elif estado2.isdigit():
                        print("El estado 2 sólo puede ser letras mayúsculas, no números ni caracteres extraños")
                    elif not estado1 in string.ascii_uppercase:
                        print("El estado 1 sólo puede ser letras mayúsculas, no números ni caracteres extraños")
                    elif not estado2 in string.ascii_uppercase:
                        print("El estado 2 sólo puede ser letras mayúsculas, no números ni caracteres extraños")
                    elif self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                        if not estado1 in xy.diccionario_afd_estados[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                            print ("El estado 1 ingresado no existe en los estados declarados del AFD: " + self.nombre)
                        elif not estado2 in xy.diccionario_afd_estados[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                            print ("El estado 2 ingresado no existe en los estados declarados del AFD: " + self.nombre)
                        elif self.nombre in xy.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                            if not simbolo in xy.diccionario_afd_alfabeto[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                                print ("El simbolo ingresado no existe en el alfabeto declarado del AFD: " + self.nombre)  
                            elif xy.revisar_doble_estado_transicion_metodo1(estado1,simbolo)=='t':
                                print ("Intenta ingresar dos transiciones desde el mismo estado. Esto no es posible en los AFD. Por favor, ingresa una transición diferente.")
                            else:
                                self.listaTransicionesAFD.append(estado1+","+estado2+";"+simbolo+"*")
                                xy.diccionario_afd_transiciones.update({self.nombre:xy.recorrer_lista_transiciones_metodo1_afd()})
                                print ("Transiciones guardadas exitosamente separadas por *: "+xy.diccionario_afd_transiciones[self.nombre])
                        else:
                            print ("Los estados ingresados no existen en los estados declarados del AFD: " + self.nombre) 
                    else:
                        print ("Los estados ingresados no existen en los estados declarados del AFD: " + self.nombre) 
        else:
            print("No puedes ingresar transiciones vacías. Por favor, ingresa una transición.")

    def menu_ingresar_estado(self):
        xy = AFD(self.nombre)
        if xy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                print ("Los estados guardados de "+self.nombre+" son: "+xy.diccionario_afd_estados[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese el estado de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar estado: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_estado(estado)

    def menu_ingresar_alfabeto(self):
        xy = AFD(self.nombre)
        if xy.diccionario_afd_alfabeto: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                print ("Los símbolos del alfabeto guardado de "+self.nombre+" son: "+xy.diccionario_afd_alfabeto[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese un símbolo del alfabeto de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar símbolo del alfabeto: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_alfabeto(estado)

    def menu_ingresar_estado_inicial(self):
        xy = AFD(self.nombre)
        if xy.diccionario_afd_estado_inicial: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_afd_estado_inicial: #Verificamos que la clave (nombre de AFD) exista
                print ("El estado inicial guardado de "+self.nombre+" es: "+xy.diccionario_afd_estado_inicial[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese un estado inicial de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar estado inicial: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_estado_inicial(estado)


    def menu_ingresar_estados_aceptacion(self):
        xy = AFD(self.nombre)
        if xy.diccionario_afd_estados_aceptacion: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_afd_estados_aceptacion: #Verificamos que la clave (nombre de AFD) exista
                print ("Los estados de aceptacion guardados de "+self.nombre+" son: "+xy.diccionario_afd_estados_aceptacion[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese los estados de aceptación de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar estado de aceptación: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_estados_aceptacion(estado)

    def mostrar_menu_transiciones_afd(self):
        xy = AFD(self.nombre)
        salir = False
        opcion = 0
        
        print ("    1. Método 1")
        print ("    2. Método 2")
        print ("    3. Regresar a menú de AFD")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.metodo1_ingreso_transiciones()
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.metodo2_ingreso_transiciones()
            elif opcion == 3:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.inicio()
            else:
                print ("Introduce un numero entre 1 y 3")

    def mostrar_menu_transiciones_afd_metodo1(self):
        xy = AFD(self.nombre)
        if xy.diccionario_afd_transiciones: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_afd_transiciones: #Verificamos que la clave (nombre de AFD) exista
                print ("Las transiciones guardados de "+self.nombre+" son: "+xy.diccionario_afd_transiciones[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese las transiciones de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar transición: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.transiciones()
            else:
                xy.guardar_transicion_metodo1(estado)

    def mostrar_menu_transiciones_afd_metodo2(self):
        xy = AFD(self.nombre)
        if xy.diccionario_afd_transiciones_metodo2: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_afd_transiciones_metodo2: #Verificamos que la clave (nombre de AFD) exista
                print ("Las transiciones guardados de "+self.nombre+" son: "+xy.diccionario_afd_transiciones_metodo2[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese las transiciones de: "+ self.nombre)
        print ("")

        contador = 0
        list_temp_trans = []
        el_mero_mero1 = "" #Este irá guardando la información original en la lista original para reportes
        el_mero_mero2 = "" #Este irá guardando la información original en la lista original para reportes
        el_mero_mero3 = "" #Este irá guardando la información original en la lista original para reportes
        el_mero_mero_total = "" #Este irá guardando la información original en la lista original para reportes

        cantidad_estados_declarados = 0

        aux_lista_transiciones_real1 = []
        aux_lista_transiciones_real2 = []
        aux_lista_transiciones_real3 = []

        while not salir:
            print ("")
            if contador == 0:
                estado = input("Ingresar terminales separados por comas (Columnas... alfabeto): ")
            elif contador == 1:
                estado = input("Ingresar NO terminales separados por comas (Filas... estados): ")
            elif contador == 2:
                estado = input("Ingresar símbolos destino (Filas con coma y columnas por punto y coma... transiciones): ")
            elif contador == 3:
                contador = 3
            if estado == "salir":
                salir = True
                os.system(var)
                xy.transiciones()
            else:
                if contador == 0:
                    xy = AFD(self.nombre)
                    estado = estado.lower()
                    el_mero_mero1 = estado
                    if estado:
                        estado = estado.replace("[", "") # reemplazamos las cadenas
                        estado = estado.replace("]", "") # reemplazamos las cadenas
                        estado = estado.replace(",", "") # reemplazamos las cadenas
                        estado = estado.lower()
                        ltemp = []
                        ltemp = estado
                        print (ltemp)
                        ltemp = []
                        ltemp = estado
                        lotro = []
                        for x in range(0,len(ltemp)):
                            if xy.diccionario_afd_alfabeto: #Verificamos que no esté vacio el diccionario
                                if self.nombre in xy.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                                    if not ltemp[x] in xy.diccionario_afd_alfabeto[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                                        print ("El simbolo ingresado << "+ltemp[x]+" >> no existe en el alfabeto declarado del AFD: " + self.nombre)
                                        el_mero_mero1 = ""
                                        lotro.clear()
                                        contador = 0
                                    elif ltemp[x] in lotro:
                                        print ("No pueden haber dos o más simbolos terminales iguales: << "+ltemp[x]+" >>")
                                        el_mero_mero1 = ""
                                        lotro.clear()
                                        contador = 0
                                    else:
                                        lotro.append(ltemp[x])
                                        aux_lista_transiciones_real1.append(ltemp[x])
                                        contador = 1
                                else:
                                    print ("El simbolo ingresado << "+ltemp[x]+" >> no existe en el alfabeto declarado del AFD: " + self.nombre)
                                    el_mero_mero1 = ""
                                    lotro.clear()
                                    contador = 0
                            else:
                                print ("El simbolo ingresado << "+ltemp[x]+" >> no existe en el alfabeto declarado del AFD: " + self.nombre)
                                el_mero_mero1 = ""
                                lotro.clear()
                                contador = 0
                    else:
                        print ("No puedes ingresar vacio.")
                        el_mero_mero1 = ""
                        contador = 0
                elif contador == 1:
                    xy = AFD(self.nombre)
                    estado = estado.upper()
                    el_mero_mero2 = estado
                    if estado:
                        estado = estado.replace("[", "") # reemplazamos las cadenas
                        estado = estado.replace("]", "") # reemplazamos las cadenas
                        estado = estado.replace(",", "") # reemplazamos las cadenas
                        estado = estado.upper()

                        cantidad_estados_declarados = len(estado)

                        ltemp = []
                        ltemp = estado
                        print (ltemp)
                       
                        ltemp = []
                        ltemp = estado
                        lotro = []
                        for x in range(0,len(ltemp)):
                            if xy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario
                                if self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                                    if not ltemp[x] in xy.diccionario_afd_estados[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                                        print ("El estado ingresado << "+ltemp[x]+" >> no existe en los estados declarados del AFD: " + self.nombre)
                                        el_mero_mero2 = ""
                                        lotro.clear()
                                        cantidad_estados_declarados = 0
                                        contador = 1
                                    elif ltemp[x] in lotro:
                                        print ("No pueden haber dos o más simbolos NO terminales iguales: << "+ltemp[x]+" >>")
                                        el_mero_mero2 = ""
                                        lotro.clear()
                                        cantidad_estados_declarados = 0
                                        contador = 1
                                    else:
                                        lotro.append(ltemp[x])
                                        aux_lista_transiciones_real2.append(ltemp[x])
                                        contador = 2
                                else:
                                    print ("El estado ingresado << "+ltemp[x]+" >> no existe en los estados declarados del AFD: " + self.nombre)
                                    el_mero_mero2 = ""
                                    lotro.clear()
                                    cantidad_estados_declarados = 0
                                    contador = 1
                            else:
                                print ("El estado ingresado << "+ltemp[x]+" >> no existe en los estados declarados del AFD: " + self.nombre)
                                el_mero_mero2 = ""
                                lotro.clear()
                                cantidad_estados_declarados = 0
                                contador = 1
                    else:
                        print ("No puedes ingresar vacio.")
                        el_mero_mero2 = ""
                        cantidad_estados_declarados = 0
                        contador = 1
                elif contador == 2:
                    xy = AFD(self.nombre)
                    estado = estado.upper()
                    el_mero_mero3 = estado
                    if estado:
                        estado = estado.replace("[", "") # reemplazamos las cadenas
                        estado = estado.replace("]", "") # reemplazamos las cadenas
                        estado = estado.replace(",", "") # reemplazamos las cadenas
                        estado = estado.replace(";", "") # reemplazamos las cadenas
                        estado = estado.upper()
                        ltemp = []
                        ltemp = estado
                        #print (ltemp)
                       
                        ltemp = []
                        ltemp = estado
                        lotro = []
                        for x in range(0,len(ltemp)):
                            if cantidad_estados_declarados*4 == len(estado):
                                if xy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario
                                    if self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                                        if not ltemp[x] in el_mero_mero2: #Si no existe el estado ingresado en los estados declarados, hacer:
                                            if ltemp[x]!='-':
                                                print ("El estado ingresado << "+ltemp[x]+" >> no existe en los estados declarados anteriormente: " + self.nombre)
                                                el_mero_mero3 = ""
                                                lotro.clear()
                                                contador = 2
                                            else:
                                                aux_lista_transiciones_real3.append(ltemp[x])
                                                lotro.append(ltemp[x])
                                                #if len(lotro) == cantidad_estados_declarados*4:
                                                contador = 3
                                                #else:
                                                #contador = 2
                                        else:
                                            aux_lista_transiciones_real3.append(ltemp[x])
                                            lotro.append(ltemp[x])
                                            #if len(lotro) == cantidad_estados_declarados*4:
                                            contador = 3
                                            #else:
                                            #contador = 2
                                    else:
                                        print ("El estado ingresado << "+ltemp[x]+" >> no existe en los estados declarados del AFD: " + self.nombre)
                                        el_mero_mero2 = ""
                                        lotro.clear()
                                        contador = 2
                                else:
                                    print ("El estado ingresado << "+ltemp[x]+" >> no existe en los estados declarados del AFD: " + self.nombre)
                                    el_mero_mero2 = ""
                                    lotro.clear()
                                    contador = 2
                            else:
                                print ("Existe una diferencia en la cantidad de estados ingresados")
                    else:
                        print ("No puedes ingresar vacio.")
                        el_mero_mero2 = ""
                        contador = 2
                elif contador == 3:




                    el_mero_mero_total = el_mero_mero1+el_mero_mero2+el_mero_mero3
                    xy.diccionario_afd_transiciones_metodo2.update({self.nombre:el_mero_mero_total})
                    print ("Se ha guardado exitosamente:" + xy.diccionario_afd_transiciones_metodo2[self.nombre])

                    


                    contador = 0




                """contador = contador + 1
                list_temp_trans.append(estado)
                if contador == 3:
                    xy.guardar_transicion_metodo2(list_temp_trans)
                    list_temp_trans.clear()
                    contador = 0"""

#
# **********************************  MENÚ GRAMÁTICA ******************************
#
class GRM:
    nombre = ''

    diccionario_afd_estados = dict() #Declaramos diccionario que contiene los nombres de AFDs y su conjunto de estados pertenecientes a cada uno
    diccionario_afd_alfabeto = dict() #Declaramos diccionario que contiene los nombres de AFDs y su conjunto de alfabeto pertenecientes a cada uno
    diccionario_afd_estado_inicial = dict() #Declaramos diccionario que contiene los estados iniciales del AFD
    diccionario_afd_estados_aceptacion = dict() #Declaramos diccionario que contiene los estados de aceptacion del AFD
    diccionario_afd_transiciones = dict() #Declaramos diccionario que contiene los estados de aceptacion del AFD
    diccionario_afd_transiciones_metodo2 = dict() #Declaramos diccionario el metodo 2 para reportes
    diccionario_afd_transiciones_metodo2_original = dict() #Declaramos diccionario el metodo 2 transformado a metodo 1 para usarlos en las validación de cadenas

    listaEstadosAFD = []
    listaAlfabetoAFD = []
    listaEstadoInicialAFD = []
    listaEstadosAceptacionAFD = []
    listaTransicionesAFD = []
    listaTransicionesAFDmetodo2 = []

    def __init__(self, nombre): 
        self.nombre = nombre 

    def inicio(self):
        xy = GRM (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ GRAMÁTICA #########################")
        xy.mostrar_menu(self.listaEstadosAFD, self.listaAlfabetoAFD, self.listaEstadoInicialAFD, self.listaEstadosAceptacionAFD, self.listaTransicionesAFD, self.listaTransicionesAFDmetodo2) #Pasamos los estados al menú con el propósito de borrarlos despúes

    def ingresarEstado(self):
        xy = GRM (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ GRAMÁTICA >> Ingresar NT (Estados) de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_estado()

    def ingresarAlfabeto(self):
        xy = GRM (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ GRAMÁTICA >> Ingresar Terminales (Alfabeto) de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_alfabeto()

    def estadoInicial(self):
        xy = GRM (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ GRAMÁTICA >> NT Inicial (Estado inicial) de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_estado_inicial()

    def estadoAceptacion(self):
        xy = GRM (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ GRAMÁTICA >> Estados de aceptación de "+ self.nombre +"  #########################")
        print ("")
        #xy.menu_ingresar_estados_aceptacion()

    """def transiciones(self): #Producciones
        xy = GRM (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ GRAMÁTICA >> Producciones de "+ self.nombre +"  #########################")
        print ("")
        xy.mostrar_menu_transiciones_afd()"""

    def metodo1_ingreso_transiciones(self): #Producciones
        xy = GRM (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ GRAMÁTICA >> Ingreso de Producciones de la Gramática "+ self.nombre +"  #########################")
        print ("")
        xy.mostrar_menu_transiciones_afd_metodo1()

    def mostrar_gramatica_transformada(self): #Producciones
        xy = GRM (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ GRAMÁTICA >> Mostrar Gramática Transformada "+ self.nombre +"  #########################")
        print ("")
        #xy.mostrar_gramatica_trans()

    def recorrer_lista_estados(self):
        x = ''
        for i in self.listaEstadosAFD:
            x = x + i
        return x

    def recorrer_lista_alfabeto(self):
        x = ''
        for i in self.listaAlfabetoAFD:
            x = x + i
        return x

    def recorrer_lista_estados_aceptacion(self):
        x = ''
        for i in self.listaEstadosAceptacionAFD:
            x = x + i
        return x

    def recorrer_lista_transiciones_metodo1_afd(self):
        x = ''
        for i in self.listaTransicionesAFD:
            x = x + i
        return x

    def mostrar_menu(self, pendejo, pendejo_alfabeto, pendejo_estado_inicial, pendejo_estados_aceptacion, pendejo_lista_transiciones_afd, pendejo_lista_transiciones_afd_m2):
        xy = GRM(self.nombre)
        salir = False
        opcion = 0
        
        print ("")
        print ("    1. Ingresar NT")
        print ("    2. Ingresar Terminales")
        print ("    3. NT Inicial")
        print ("    4. Producciones")
        print ("    5. Mostrar Gramática Transformada")
        print ("    6. Ayuda")
        print ("    7. Regresar a pantalla inicial")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.ingresarEstado() #Ingresar NT
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.ingresarAlfabeto() #Ingresar Terminales
            elif opcion == 3:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.estadoInicial() #NT inicial
            elif opcion == 4:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.metodo1_ingreso_transiciones() #Producciones
            elif opcion == 5:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.mostrar_gramatica_transformada() #Mostrar gramática transformada
            elif opcion == 6:
                ayuda()
            elif opcion == 7:
                pendejo.clear() #Borramos lista de estados
                pendejo_alfabeto.clear() #Borramos lista de alfabeto
                pendejo_estado_inicial.clear() # Borramos el estado inicial
                pendejo_estados_aceptacion.clear() #Borramos estados de aceptacion
                pendejo_lista_transiciones_afd.clear()
                pendejo_lista_transiciones_afd_m2.clear()
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                MenuPrincipal.inicio()
            else:
                print ("Introduce un numero entre 1 y 7")

    def guardar_estado(self,estado):
        xy = GRM(self.nombre)
        if estado:
            estado = estado[0:1] 
            estado = estado.upper()
            if estado.isdigit():
                print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
            else:
                if estado in self.listaEstadosAFD: # Imprime lo de abajo
                    print ("El estado o No Terminal "+estado+ " ya existe en la Gramática "+ self.nombre +". Por favor, ingresa otro estado o No Terminal.")
                elif estado in string.ascii_uppercase:
                    if xy.diccionario_afd_alfabeto: #Verificamos que no esté vacio el diccionario del alfabeto
                        if self.nombre in xy.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                            if estado in xy.diccionario_afd_alfabeto[self.nombre]:
                                print ("El estado o No Terminal ya existe como alfabeto o terminal del lenguaje de " + self.nombre + ", por favor ingresa otro estado o No Terminal.")
                            else:
                                self.listaEstadosAFD.append(estado)
                                xy.diccionario_afd_estados.update({self.nombre:xy.recorrer_lista_estados()})
                                print ("Estados o No Terminales guardados: "+xy.diccionario_afd_estados[self.nombre])
                        else: 
                            self.listaEstadosAFD.append(estado)
                            xy.diccionario_afd_estados.update({self.nombre:xy.recorrer_lista_estados()})
                            print ("Estados guardados o No Terminales: "+xy.diccionario_afd_estados[self.nombre])
                    else:  
                        self.listaEstadosAFD.append(estado)
                        xy.diccionario_afd_estados.update({self.nombre:xy.recorrer_lista_estados()})
                        print ("Estados guardados o No Terminales: "+xy.diccionario_afd_estados[self.nombre])
                else:
                    print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
        else:
            print("No puedes ingresar un estado vacio. Por ingresa un estado.")

    def guardar_alfabeto(self,estado):
        xy = GRM(self.nombre)
        if estado:
            estado = estado[0:1] 
            estado = estado.lower()
            if (estado.isspace()):
                print ("No puedes ingresar simbolos vacios.")
            else:
                if estado in self.listaAlfabetoAFD: # Imprime lo de abajo
                    print ("El símbolo o terminal "+estado+ " ya existe en la Gramática "+ self.nombre +". Por favor, ingrese otro símbolo del alfabeto o terminal.")
                elif xy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario del alfabeto
                    if self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                        if estado in xy.diccionario_afd_estados[self.nombre]:
                            print ("El símbolo o terminal ya existe como estado o No Terminal de " + self.nombre + ", por favor ingrese otro símbolo del alfabeto o terminal.")
                        else:
                            self.listaAlfabetoAFD.append(estado)
                            xy.diccionario_afd_alfabeto.update({self.nombre:xy.recorrer_lista_alfabeto()})
                            print ("Símbolos del alfabeto o terminales guardados: "+xy.diccionario_afd_alfabeto[self.nombre])
                    else: 
                        self.listaAlfabetoAFD.append(estado)
                        xy.diccionario_afd_alfabeto.update({self.nombre:xy.recorrer_lista_alfabeto()})
                        print ("Símbolos del alfabeto o terminales guardados: "+xy.diccionario_afd_alfabeto[self.nombre])
                else:  
                    self.listaAlfabetoAFD.append(estado)
                    xy.diccionario_afd_alfabeto.update({self.nombre:xy.recorrer_lista_alfabeto()})
                    print ("Símbolos del alfabeto o terminales guardados: "+xy.diccionario_afd_alfabeto[self.nombre])
        else:
            print("No puedes ingresar un símbolo vacio. Por ingresa un símbolo o terminal.")

    def guardar_estado_inicial(self,estado):
        xy = GRM(self.nombre)
        if estado:
            estado = estado[0:1] 
            estado = estado.upper()
            if estado.isdigit():
                print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
            else:
                if xy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario de estados de aceptacion
                    if self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                        if not estado in xy.diccionario_afd_estados[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                            print ("El estado ingresado o no terminal inicial no existe en los estados declarados de la Gramática: " + self.nombre)
                        else:
                            if estado in string.ascii_uppercase:
                                self.listaEstadoInicialAFD.clear()
                                self.listaEstadoInicialAFD.append(estado)
                                xy.diccionario_afd_estado_inicial.update({self.nombre:estado})
                                print ("Estado o no terminal inicial guardado exitosamente: "+xy.diccionario_afd_estado_inicial[self.nombre])
                    else:
                        print ("El estado ingresado o no terminal inicial no existe en los estados o No Terminales declarados de la Gramática: " + self.nombre)
                else:
                    print ("El estado o no terminal inicial ingresado no existe en los estados o No Terminales declarados de la Gramática: " + self.nombre)
        else:
            print("No puedes ingresar un estado o no terminal inicial vacio. Por ingresa un estado o no terminal inicial.")

    def guardar_estados_aceptacion(self,estado):
        xy = GRM(self.nombre)
        if estado:
            estado = estado[0:1] 
            estado = estado.upper()
            if estado.isdigit():
                print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
            else:
                if xy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario de estados de aceptacion
                    if self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                        if not estado in xy.diccionario_afd_estados[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                            print ("El estado ingresado no existe en los estados declarados del AFD: " + self.nombre)
                        else:
                            if estado in self.listaEstadosAceptacionAFD: # Imprime lo de abajo
                                print ("El estado de aceptación ingresado ya se encuentra registrado como estado aceptación de "+self.nombre+", por favor ingresa otro estado")
                            elif estado in string.ascii_uppercase:
                                self.listaEstadosAceptacionAFD.append(estado)
                                xy.diccionario_afd_estados_aceptacion.update({self.nombre:xy.recorrer_lista_estados_aceptacion()})
                                print ("Estados de aceptación guardados: "+xy.diccionario_afd_estados_aceptacion[self.nombre])
                            else:
                                print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
                    else:
                        print ("El estado ingresado no existe en los estados declarados del AFD: " + self.nombre)
                else:
                    print ("El estado ingresado no existe en los estados declarados del AFD: " + self.nombre)
        else:
            print("No puedes ingresar un estado de aceptación vacio. Por favor, ingresa un estado.")

    def revisar_doble_estado_transicion_metodo1(self,e1,s):
        estado1 = ""
        estado2 = ""
        simbolo = ""
        cadena1 = []
        cadena2 = []
        y = 'f'
        if self.listaTransicionesAFD:
            for x in self.listaTransicionesAFD:
                cadena1 = x.split(">")
                if cadena1[1] == "epsilon":
                    simbolo = "epsilon"
                else:
                    simbolo = cadena1[1][0]
                estado1 = cadena1[0]
                estado2 = cadena1[1][1]
                if e1 == estado1 and s == simbolo:
                    y = 't'
        return y

    def guardar_transicion_metodo1(self,estado):
        xy = GRM(self.nombre)
        estado1 = ""
        estado2 = ""
        simbolo = ""
        cadena1 = []
        cadena2 = []

        lista1 = []
        pos_inicial1 = -1
        lista2 = []
        pos_inicial2 = -1
        posicion_coma = 0
        posicion_pc = 0

        estado = estado.replace(" ","")

        if estado:
            if not ">" in estado:
                print ("No existe el caracter especial '>'en la cadena de texto. Por favor, ingresa una cadena de texto correta.")
            elif ">" in estado:
                    

                    cadena1 = estado.split(">")
                    estado1 = cadena1[0]
                    estado2 = cadena1[1][1]
                    
                    estado1 = estado1.upper()
                    estado2 = estado2.upper()

                    simbolo = cadena1[1][0]

                    if "epsilon" in cadena1[1]:
                        simbolo = "epsilon"
                        estado2 = ""
                    else:
                        simbolo = cadena1[1][0]
                        estado2 = cadena1[1][1]

                    if estado1.isdigit():
                        print("El estado 1 sólo puede ser letras mayúsculas, no números ni caracteres extraños")
                    elif estado2.isdigit():
                        print("El estado 2 sólo puede ser letras mayúsculas, no números ni caracteres extraños")
                    elif not estado1 in string.ascii_uppercase:
                        print("El estado 1 sólo puede ser letras mayúsculas, no números ni caracteres extraños")
                    elif not estado2 in string.ascii_uppercase:
                        print("El estado 2 sólo puede ser letras mayúsculas, no números ni caracteres extraños")
                    elif self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                        if not estado1 in xy.diccionario_afd_estados[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                            print ("El estado 1 ingresado no existe en los estados declarados del AFD: " + self.nombre)
                        elif not estado2 in xy.diccionario_afd_estados[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                            print ("El estado 2 ingresado no existe en los estados declarados del AFD: " + self.nombre)
                        elif xy.revisar_doble_estado_transicion_metodo1(estado1,simbolo)=='t':
                            print ("Intenta ingresar dos transiciones desde el mismo estado. Esto no es posible en las gramaticas tipo 3. Por favor, ingresa una transición diferente.")
                        else:
                            self.listaTransicionesAFD.append(estado1+">"+simbolo+estado2+"*")
                            xy.diccionario_afd_transiciones.update({self.nombre:xy.recorrer_lista_transiciones_metodo1_afd()})
                            print ("Transiciones guardadas exitosamente separadas por *: "+xy.diccionario_afd_transiciones[self.nombre])
                    else:
                        print ("Los estados ingresados no existen en los estados declarados de la gramática: " + self.nombre) 
        else:
            print("No puedes ingresar transiciones vacías. Por favor, ingresa una transición.")

    def menu_ingresar_estado(self): #No Terminales
        xy = GRM(self.nombre)
        if xy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                print ("Los No Terminales guardados de "+self.nombre+" son: "+xy.diccionario_afd_estados[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese el No Terminal de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar No Terminal: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_estado(estado)

    def menu_ingresar_alfabeto(self):
        xy = GRM(self.nombre)
        if xy.diccionario_afd_alfabeto: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                print ("Los símbolos (alfabeto) o terminales guardado de "+self.nombre+" son: "+xy.diccionario_afd_alfabeto[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese un símbolo o terminal de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar símbolo o terminal: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_alfabeto(estado)

    def menu_ingresar_estado_inicial(self):
        xy = GRM(self.nombre)
        if xy.diccionario_afd_estado_inicial: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_afd_estado_inicial: #Verificamos que la clave (nombre de AFD) exista
                print ("El estado inicial o no terminal inicial guardado de "+self.nombre+" es: "+xy.diccionario_afd_estado_inicial[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese un estado inicial o no terminal inicial de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar No terminal inicial: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_estado_inicial(estado)

    def mostrar_menu_transiciones_afd(self):
        xy = GRM(self.nombre)
        salir = False
        opcion = 0
        
        print ("    1. Método 1")
        print ("    2. Método 2")
        print ("    3. Regresar a menú de AFD")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.metodo1_ingreso_transiciones()
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.metodo2_ingreso_transiciones()
            elif opcion == 3:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.inicio()
            else:
                print ("Introduce un numero entre 1 y 3")

    def mostrar_menu_transiciones_afd_metodo1(self):
        xy = GRM(self.nombre)
        if xy.diccionario_afd_transiciones: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_afd_transiciones: #Verificamos que la clave (nombre de AFD) exista
                print ("Las producciones guardados de "+self.nombre+" son: "+xy.diccionario_afd_transiciones[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese las producciones de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar producción: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_transicion_metodo1(estado)

#
# **********************************  MENÚ REPORTES ******************************
#
class REPORTES:
    nombre = ''
    tipo = ''

    def __init__(self, nombre, tipo): 
        self.nombre = nombre
        self.tipo = tipo 

    def inicio(self):
        xy = REPORTES (self.nombre, self.tipo)
        print ("#######################  PROYECTO 1  #########################")
        if self.tipo == 'grm':
            print ("####################### MENÚ REPORTES >> Gramática "+ self.nombre +"  #########################")
        elif self.tipo == 'afd':
            print ("####################### MENÚ REPORTES >> AFD "+ self.nombre +"  #########################")
        xy.mostrar_menu() #Pasamos los estados al menú con el propósito de borrarlos despúes

    def verDetalle(self):
        xy = REPORTES (self.nombre, self.tipo)
        xxx = AFD(self.nombre)
        yyy = GRM(self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        if self.tipo == 'grm':
            print ("####################### MENÚ REPORTE >> Ver detalle Gramática "+ self.nombre +"  #########################")
        elif self.tipo == 'afd':
            print ("####################### MENÚ REPORTES >> Ve detalle AFD "+ self.nombre +"  #########################")
        print ("")
        
        if self.tipo == 'afd':
            if xxx.diccionario_afd_alfabeto: #Verificamos que no esté vacio el diccionario
                if self.nombre in xxx.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                    print ("Alfabeto correcto: "+xy.concatenar_letras_comas(xxx.diccionario_afd_alfabeto[self.nombre]))
                else:
                    print ("No hay alfabeto registrado con ese nombre de AFD: "+ self.nombre)
            else:
                print ("No hay alfabeto registrado con ese nombre de AFD: "+ self.nombre)
            if xxx.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario
                if self.nombre in xxx.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                    print ("Estados correctos: "+xy.concatenar_letras_comas(xxx.diccionario_afd_estados[self.nombre]))
                else:
                    print ("No hay estados registrado con ese nombre de AFD: "+ self.nombre)
            else:
                print ("No hay estados registrado con ese nombre de AFD: "+ self.nombre)
            if xxx.diccionario_afd_estados_aceptacion: #Verificamos que no esté vacio el diccionario
                if self.nombre in xxx.diccionario_afd_estados_aceptacion: #Verificamos que la clave (nombre de AFD) exista
                    print ("Estados de aceptación correctos: "+xy.concatenar_letras_comas(xxx.diccionario_afd_estados_aceptacion[self.nombre]))
                else:
                    print ("No hay estados de aceptación registrados con ese nombre de AFD: "+ self.nombre)
            else:
                print ("No hay estados de aceptación registrados con ese nombre de AFD: "+ self.nombre)
            if xxx.diccionario_afd_transiciones: #Verificamos que no esté vacio el diccionario
                if self.nombre in xxx.diccionario_afd_transiciones: #Verificamos que la clave (nombre de AFD) exista
                    print ("Transiciones correctas Método 1: "+xxx.diccionario_afd_transiciones[self.nombre].replace("*","   |    "))
                else:
                    print ("No hay transiciones registradas con el Método 1 con ese nombre de AFD: "+ self.nombre)
            else:
                print ("No hay transiciones registradas con el Método 1 con ese nombre de AFD: "+ self.nombre)
            if xxx.diccionario_afd_transiciones_metodo2: #Verificamos que no esté vacio el diccionario
                if self.nombre in xxx.diccionario_afd_transiciones_metodo2: #Verificamos que la clave (nombre de AFD) exista
                    print ("Transiciones correctas Método 2: "+xxx.diccionario_afd_transiciones_metodo2[self.nombre])
                else:
                    print ("No hay transiciones registradas con el Método 2 con ese nombre de AFD: "+ self.nombre)
            else:
                print ("No hay transiciones registradas con el Método 2 con ese nombre de AFD: "+ self.nombre)
            if xxx.diccionario_afd_estado_inicial: #Verificamos que no esté vacio el diccionario
                if self.nombre in xxx.diccionario_afd_estado_inicial: #Verificamos que la clave (nombre de AFD) exista
                    print ("Estado inicial correcto: "+xxx.diccionario_afd_estado_inicial[self.nombre])
                else:
                    print ("No hay estado inicial registrado con ese nombre de AFD: "+ self.nombre)
            else:
                print ("No hay estado inicial registrado con ese nombre de AFD: "+ self.nombre)

        if self.tipo == 'grm':
            if yyy.diccionario_afd_estado_inicial: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_estado_inicial: #Verificamos que la clave (nombre de AFD) exista
                    print ("No terminal inicial correcto: "+yyy.diccionario_afd_estado_inicial[self.nombre])
                else:
                    print ("No hay No terminal inicial registrado con ese nombre de Gramática: "+ self.nombre)
            else:
                print ("No hay No terminal inicial registrado con ese nombre de Gramática: "+ self.nombre)
            if yyy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                    print ("No terminales correctos: "+xy.concatenar_letras_comas(yyy.diccionario_afd_estados[self.nombre]))
                else:
                    print ("No hay No terminales registrados con ese nombre de Gramática: "+ self.nombre)
            else:
                print ("No hay No terminales registrados con ese nombre de Gramática: "+ self.nombre)
            if yyy.diccionario_afd_alfabeto: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                    print ("Terminales correcto: "+xy.concatenar_letras_comas(yyy.diccionario_afd_alfabeto[self.nombre]))
                else:
                    print ("No hay terminales registrados con ese nombre de Gramática: "+ self.nombre)
            else:
                print ("No hay terminales registrados con ese nombre de Gramática: "+ self.nombre)
            if yyy.diccionario_afd_transiciones: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_transiciones: #Verificamos que la clave (nombre de AFD) exista
                    print ("Producciones correctas: "+yyy.diccionario_afd_transiciones[self.nombre])
                else:
                    print ("No hay producciones registradas con ese nombre de Gramática: "+ self.nombre)
            else:
                print ("No hay producciones registradas con ese nombre de Gramática: "+ self.nombre)
        
        xy.salir_menu()

    def generarReporte(self):
        xy = REPORTES (self.nombre, self.tipo)
        xxx = AFD(self.nombre)
        yyy = GRM(self.nombre)
        if self.tipo == 'afd':

            estados = []
            #trans = [("A","B", 1),("A","E",0),("A","E",1),("A","A",1),("A","D",1),("F","F",1),("D","C",1),("B","A",0), ("E","C",0),("F","D",0), ("C","A",0), ("B","B", 1)]
            trans = []
            inicial = []
            alf = []
            terminal = ()

            nombre = self.nombre+random.choice(string.ascii_letters)+".pdf"
            c = canvas.Canvas(nombre)

            c.setFont('Helvetica', 15)
            c.drawString(25,800,"**** AFD ****")
            c.setFont('Helvetica', 12)

            if xxx.diccionario_afd_alfabeto: #Verificamos que no esté vacio el diccionario
                if self.nombre in xxx.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,780,"Alfabeto: "+xy.concatenar_letras_comas(xxx.diccionario_afd_alfabeto[self.nombre]))
                    for x in xxx.diccionario_afd_alfabeto[self.nombre]:
                        alf.append(x)
                else:
                    c.drawString(25,780,"")
            else:
                c.drawString(25,700,"")
            if xxx.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario
                if self.nombre in xxx.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,760,"Estados: "+xy.concatenar_letras_comas(xxx.diccionario_afd_estados[self.nombre]))
                    for x in xxx.diccionario_afd_estados[self.nombre]:
                        estados.append(x)
                else:
                    c.drawString(25,760,"")
            else:
                c.drawString(25,760,"")
            if xxx.diccionario_afd_estados_aceptacion: #Verificamos que no esté vacio el diccionario
                if self.nombre in xxx.diccionario_afd_estados_aceptacion: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,740,"Estados de aceptación: "+xy.concatenar_letras_comas(xxx.diccionario_afd_estados_aceptacion[self.nombre]))
                    l = list(terminal)
                    for x in xxx.diccionario_afd_estados_aceptacion[self.nombre]:
                        #terminal.append(x)
                        l.append(x)
                    terminal = tuple(l)
                else:
                    c.drawString(25,740,"")
            else:
                c.drawString(25,740,"")
            if xxx.diccionario_afd_transiciones: #Verificamos que no esté vacio el diccionario    
                if self.nombre in xxx.diccionario_afd_transiciones: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,720,"Transiciones: "+xxx.diccionario_afd_transiciones[self.nombre].replace("*","   |    "))
                    
                    xxxx = []
                    my_list = []
                    transiciones = xxx.diccionario_afd_transiciones[self.nombre].replace(";",",")
                    my_list = transiciones.split(",")

                    #transiciones = xxx.diccionario_afd_transiciones[self.nombre].replace(",","")
                    for x in transiciones:
                        if x!='*':
                            if x!=',':
                                xxxx.append(x)
                        else: 
                            trans.append(tuple(xxxx))
                            xxxx.clear()
                else:
                    c.drawString(25,720,"")
            else:
                c.drawString(25,720,"")
            if xxx.diccionario_afd_estado_inicial: #Verificamos que no esté vacio el diccionario    
                if self.nombre in xxx.diccionario_afd_estado_inicial: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,700,"Estado inicial: "+xxx.diccionario_afd_estado_inicial[self.nombre])
                    for x in xxx.diccionario_afd_estado_inicial[self.nombre]:
                        inicial.append(x)
                else:
                    c.drawString(25,700,"")
            else:
                c.drawString(25,700,"")


            c.setFont('Helvetica', 15)
            c.drawString(25,680,"**** Gramática ****")
            c.setFont('Helvetica', 12)

            if yyy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,660,"No Terminales: "+xy.concatenar_letras_comas(yyy.diccionario_afd_estados[self.nombre]))
                else:
                    c.drawString(25,660,"")
            else:
                c.drawString(25,660,"")
            if yyy.diccionario_afd_estado_inicial: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_estado_inicial: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,640,"No Terminal inicial: "+yyy.diccionario_afd_estado_inicial[self.nombre])
                else:
                    c.drawString(25,640,"")
            else:
                c.drawString(25,640,"")
            if yyy.diccionario_afd_alfabeto: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,620,"Alfabeto: "+xy.concatenar_letras_comas(yyy.diccionario_afd_alfabeto[self.nombre]))
                else:
                    c.drawString(25,620,"")
            else:
                c.drawString(25,620,"")
            if yyy.diccionario_afd_transiciones: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_transiciones: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,600,"Producciones: "+yyy.diccionario_afd_transiciones[self.nombre])
                else:
                    c.drawString(25,600,"")
            else:
                c.drawString(25,600,"")


            #xy.draw(alf, estados, inicial, trans, terminal)
            print (trans)
            print (estados)
            print (inicial)
            print (terminal)
            print (alf)

            xy.draw(alf, estados, inicial, trans, terminal)

            # Dibujamos una imagen (IMAGEN, X,Y, WIDTH, HEIGH)
            c.drawImage('Digraph.gv.png', 25, 250, 500, 200)




            c.save()


        if self.tipo == 'grm':
            nombre = self.nombre+random.choice(string.ascii_letters)+".pdf"
            c = canvas.Canvas(nombre)
            c.setFont('Helvetica', 15)
            c.drawString(25,680,"**** Gramática ****")
            c.setFont('Helvetica', 12)

            if yyy.diccionario_afd_estados: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_estados: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,660,"No Terminales: "+xy.concatenar_letras_comas(yyy.diccionario_afd_estados[self.nombre]))
                else:
                    c.drawString(25,660,"")
            else:
                c.drawString(25,660,"")
            if yyy.diccionario_afd_estado_inicial: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_estado_inicial: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,640,"No Terminal inicial: "+yyy.diccionario_afd_estado_inicial[self.nombre])
                else:
                    c.drawString(25,640,"")
            else:
                c.drawString(25,640,"")
            if yyy.diccionario_afd_alfabeto: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_alfabeto: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,620,"Alfabeto: "+xy.concatenar_letras_comas(yyy.diccionario_afd_alfabeto[self.nombre]))
                else:
                    c.drawString(25,620,"")
            else:
                c.drawString(25,620,"")
            if yyy.diccionario_afd_transiciones: #Verificamos que no esté vacio el diccionario
                if self.nombre in yyy.diccionario_afd_transiciones: #Verificamos que la clave (nombre de AFD) exista
                    c.drawString(25,600,"Producciones: "+yyy.diccionario_afd_transiciones[self.nombre])
                else:
                    c.drawString(25,600,"")
            else:
                c.drawString(25,600,"")

            c.save()

            # Dibujamos una imagen (IMAGEN, X,Y, WIDTH, HEIGH)
            #c.drawImage('image.jpg', 25, 480, 480, 270)

        xy.salir_menu()

    def concatenar_letras_comas(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        can = "{"+can+"}"
        return can

    def concatenar_letras_comas_sin_llaves(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        return can

    def generarAFDGraphics_fromAFD(self, nombre_generado):
        f = Digraph('finite_state_machine')
        f.attr(rankdir='LR', size='8,5')

        f.attr('node', shape='doublecircle')
        f.node('LR_0')
        f.node('LR_3')
        f.node('LR_4')
        f.node('LR_8')

        f.attr('node', shape='circle')
        f.edge('LR_0', 'LR_2', label='SS(B)')
        f.edge('LR_0', 'LR_1', label='SS(S)')
        f.edge('LR_1', 'LR_3', label='S($end)')
        f.edge('LR_2', 'LR_6', label='SS(b)')
        f.edge('LR_2', 'LR_5', label='SS(a)')
        f.edge('LR_2', 'LR_4', label='S(A)')
        f.edge('LR_5', 'LR_7', label='S(b)')
        f.edge('LR_5', 'LR_5', label='S(a)')
        f.edge('LR_6', 'LR_6', label='S(b)')
        f.edge('LR_6', 'LR_5', label='S(a)')
        f.edge('LR_7', 'LR_8', label='S(b)')
        f.edge('LR_7', 'LR_5', label='S(a)')
        f.edge('LR_8', 'LR_6', label='S(b)')
        f.edge('LR_8', 'LR_5', label='S(a)')

        #f.view()
        f.render('round-table.gv', view=True)

    def draw(self,alfabeto, estados, inicio, trans, final):
        print("inicio:", str(inicio))
        g = gv.Digraph(format='png')
        g.graph_attr['rankdir'] = 'LR'
        g.node('ini', shape="point")
        for e in estados:
            if e in final:
                g.node(e, shape="doublecircle")
            else:
                g.node(e)
            if e in inicio:
                g.edge('ini',e)

        for t in trans:
            if t[2] not in alfabeto:
                return 0
            g.edge(t[0], t[1], label=str(t[2]))
        g.render(view=True)

    def salir_menu(self):
        xy = REPORTES(self.nombre, self.tipo)
        salir = False
        opcion = 0
        
        print ("")
        print ("Ingrese << 0 >> para regresar al menú de reportes")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 0:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                pedir_nombre_reporte() #Ingresar NT
            else:
                print ("Introduce 0 para regresar al menú de reportes")

    def salir_menu_other(self):
        xy = REPORTES(self.nombre, self.tipo)

        salir = False
        opcion = 0
        
        print ("")
        print ("Ingrese << 0 >> para regresar al menú de reportes")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 0:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.mostrar_menu() #Ingresar NT
            else:
                print ("Introduce 0 para regresar al menú de reportes")

    def mostrar_menu(self):
        xy = REPORTES(self.nombre, self.tipo)
        salir = False
        opcion = 0
        
        print ("")
        print ("    1. Ver detalle")
        print ("    2. Generar Reporte")
        print ("    3. Ayuda")
        print ("    4. Regresar a pantalla inicial de reporte")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.verDetalle() #Ingresar NT
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.generarReporte() #Ingresar Terminales
            elif opcion == 3:
                #estados = ["A","B","C","E","F"]
                #trans = [("A","B", 1),("A","E",0),("A","E",1),("A","A",1),("A","D",1),("F","F",1),("D","C",1),("B","A",0), ("E","C",0),("F","D",0), ("C","A",0), ("B","B", 1)]
                #inicial = ["A"]
                #alf = [0,1]
                #terminal = ("C",)
                #xy.generarAFDGraphics_fromAFD("erick.gv")
                #xy.draw(alf, estados, inicial, trans, terminal)
                ayuda()
            elif opcion == 4:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                pedir_nombre_reporte()
            else:
                print ("Introduce un numero entre 1 y 4")


#
# **********************************  MENÚ CARGAR ARCHIVOS ******************************
#
class CA:
    nombre = ''
    tipo = ''
    direccion = ''

    def __init__(self, nombre, tipo, direccion): 
        self.nombre = nombre
        self.tipo = tipo
        self.direccion = direccion 

    def inicio(self):
        xy = CA (self.nombre, self.tipo, self.direccion)
        print ("#######################  PROYECTO 1  #########################")
        if self.tipo == 'grm':
            print ("####################### MENÚ CARGAR ARCHIVOS >> Gramática "+ self.nombre +"  #########################")
        elif self.tipo == 'afd':
            print ("####################### CARGAR ARCHIVOS >> AFD "+ self.nombre +"  #########################")
        xy.verDetalle() #Pasamos los estados al menú con el propósito de borrarlos despúes

    def verDetalle(self):
        xy = CA (self.nombre, self.tipo, self.direccion)
        xxx = AFD(self.nombre)
        yyy = GRM(self.nombre)
        if self.tipo == 'afd':
            #data_file = 'C:\\Users\\vuyisile\\Desktop\\Test\\data.txt'
            #C:\Users\USUARIO\Desktop\
            #binariasConAlmenosDos0
            

            #f = open('archivo.mascotas_result','a')
            #f.write('\n' + '[' + time.strftime("%d/%m/%y") + ' ' + time.strftime("%H:%M") + ']' + ' ' + 'Se creó el pájaro' + ' ' + nombre)
            #f.close()

            #f = open(self.direccion+self.nombre+'.afd', "r")
            #contents = f.read()
            #print (contents)

            xxx.listaEstadosAFD.clear()
            xxx.listaAlfabetoAFD.clear()
            xxx.listaEstadoInicialAFD.clear()
            xxx.listaEstadosAceptacionAFD.clear()
            xxx.listaTransicionesAFD.clear()

            list = []
            list2 = []
            list3 = []
            respuesta = 'f'
            cadena_datos = ''

            estados = []
            alfabeto = []
            estados_aceptacion = []
            estado_inicial = []
            transiciones = []
            contador = 0

            try:
                archivo = open(self.direccion+self.nombre+'.afd', "r")
                for linea in archivo.readlines():
                    list = linea.split(";")
                    list2 = list[0].split(",")
                    list3 = list[1].split(",")
                    if contador == 0:
                        xxx.listaEstadoInicialAFD.append(list2[0])
                        estado_inicial.append(list2[0])
                    contador = 1
                    if not list2[0] in xxx.listaEstadosAFD:
                        xxx.listaEstadosAFD.append(list2[0])
                    if not list2[1] in xxx.listaEstadosAFD:
                        xxx.listaEstadosAFD.append(list2[1])
                    if not list2[2] in xxx.listaAlfabetoAFD:
                        xxx.listaAlfabetoAFD.append(list2[2])
                    if list3[0] == 'true':
                        if not list2[0] in xxx.listaEstadosAceptacionAFD:
                            xxx.listaEstadosAceptacionAFD.append(list2[0])
                    if list3[0] == 'false':
                        if list2[0] in xxx.listaEstadosAceptacionAFD:
                            xxx.listaEstadosAceptacionAFD.remove(list2[0])
                    if list3[1] == 'true':
                        if not list2[1] in xxx.listaEstadosAceptacionAFD:
                            xxx.listaEstadosAceptacionAFD.append(list2[1])
                    if list3[1] == 'false':
                        if list2[1] in xxx.listaEstadosAceptacionAFD:
                            xxx.listaEstadosAceptacionAFD.remove(list2[1])

                    xxx.listaTransicionesAFD.append(list2[0]+","+list2[1]+";"+list2[2]+"*")
                    xxx.diccionario_afd_transiciones.update({self.nombre:xxx.recorrer_lista_transiciones_metodo1_afd()})
                    xxx.diccionario_afd_estados.update({self.nombre:xxx.recorrer_lista_estados()})
                    xxx.diccionario_afd_alfabeto.update({self.nombre:xxx.recorrer_lista_alfabeto()})
                    xxx.diccionario_afd_estado_inicial.update({self.nombre:estado_inicial[0]})
                    xxx.diccionario_afd_estados_aceptacion.update({self.nombre:xxx.recorrer_lista_estados_aceptacion()})

                print ("Se ha ingresado el archivo exitosamente")
            except IOError:
                print("No se puede acceder al archivo o no existe.")
            finally:
                archivo.close()


        xy.salir_menu()
        

    def concatenar_letras_comas(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        can = "{"+can+"}"
        return can

    def concatenar_letras_comas_sin_llaves(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        return can

    def salir_menu(self):
        xy = CA(self.nombre, self.tipo, self.direccion)
        salir = False
        opcion = 0
        
        print ("")
        print ("Ingrese << 0 >> para regresar al menú de cargar archivo")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 0:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                pedir_nombre_cargar_archivo() #Ingresar NT
            else:
                print ("Introduce 0 para regresar al menú de cargar archivo")

    def salir_menu_other(self):
        xy = REPORTES(self.nombre, self.tipo)

        salir = False
        opcion = 0
        
        print ("")
        print ("Ingrese << 0 >> para regresar al menú de reportes")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 0:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.mostrar_menu() #Ingresar NT
            else:
                print ("Introduce 0 para regresar al menú de reportes")

    def mostrar_menu(self):
        xy = REPORTES(self.nombre, self.tipo)
        salir = False
        opcion = 0
        
        print ("")
        print ("    1. Ver detalle")
        print ("    2. Generar Reporte")
        print ("    3. Ayuda")
        print ("    4. Regresar a pantalla inicial de reporte")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.verDetalle() #Ingresar NT
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.generarReporte() #Ingresar Terminales
            elif opcion == 3:
                #estados = ["A","B","C","E","F"]
                #trans = [("A","B", 1),("A","E",0),("A","E",1),("A","A",1),("A","D",1),("F","F",1),("D","C",1),("B","A",0), ("E","C",0),("F","D",0), ("C","A",0), ("B","B", 1)]
                #inicial = ["A"]
                #alf = [0,1]
                #terminal = ("C",)
                #xy.generarAFDGraphics_fromAFD("erick.gv")
                #xy.draw(alf, estados, inicial, trans, terminal)
                ayuda()
            elif opcion == 4:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                pedir_nombre_reporte()
            else:
                print ("Introduce un numero entre 1 y 4")

#
# **********************************  MENÚ EVALUAR CADENAS ******************************
#
class ECAD:
    nombre = ''

    def __init__(self, nombre): 
        self.nombre = nombre

    def inicio(self):
        xy = ECAD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ EVALUAR CADENAS #########################")
        xy.mostrar_menu() #Pasamos los estados al menú con el propósito de borrarlos despúes

    def soloValidar(self):
        xy = ECAD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ EVALUAR CADENAS >> Sólo validar gramática "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_cadena_validacion()

    def rutaEnAFD(self):
        xy = ECAD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ EVALUAR CADENAS >> Ruta en AFD de la gramática "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_cadena_ruta_afd()

    def expandirGramatica(self):
        xy = ECAD (self.nombre)
        print ("#######################  PROYECTO 1  #########################")
        print ("####################### MENÚ EVALUAR CADENAS >> Expandir con gramáica "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_cadena_expandir_gramatica()

    def menu_ingresar_cadena_validacion(self): #No Terminales
        xy = ECAD(self.nombre)
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese la cadena a evaluar para la gramática: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar cadena a evaluar: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.evaluar_cadena(estado)

    def menu_ingresar_cadena_ruta_afd(self): #No Terminales
        xy = ECAD(self.nombre)
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese la cadena a evaluar en Ruta AFD para la gramática: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar cadena a evaluar en Ruta AFD: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.evaluar_cadena_ruta_afd(estado)

    def menu_ingresar_cadena_expandir_gramatica(self): #No Terminales
        xy = ECAD(self.nombre)
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese la cadena a evaluar para Expandir Gramática de la gramática: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar cadena a evaluar para Expandir Gramática: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.evaluar_cadena_expandir_gramatica(estado)

    def evaluar_cadena(self,estado):
        print ("evaluar cadena")
        #evaluamos

    def evaluar_cadena_ruta_afd(self,estado):
        print ("evaluar cadena")

    def evaluar_cadena_expandir_gramatica(self,estado):
        print ("evaluar cadena")


    def mostrar_menu(self):
        xy = ECAD(self.nombre)
        salir = False
        opcion = 0
        
        print ("")
        print ("    1. Sólo validar")
        print ("    2. Ruta en AFD")
        print ("    3. Expandir con gramática")
        print ("    4. Ayuda")
        print ("    5. Regresar a pantalla inicial")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.soloValidar() #Ingresar NT
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.rutaEnAFD() #Ingresar Terminales
            elif opcion == 3:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.expandirGramatica() #Ingresar Terminales
            elif opcion == 4:
                ayuda()
            elif opcion == 5:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                MenuPrincipal.inicio()
            else:
                print ("Introduce un numero entre 1 y 5")

#
# **********************************  GRAMÁTICAS TIPO 2 Y AP ******************************
#
class GRM_TIPO2:
    nombre = '' # Declaramos el atributo nombre

    diccionario_grmtipo2_noterminales = dict() #Declaramos diccionario que contiene los nombres de AFDs y su conjunto de estados pertenecientes a cada uno
    diccionario_grmtipo2_terminales = dict() #Declaramos diccionario que contiene los nombres de AFDs y su conjunto de alfabeto pertenecientes a cada uno
    diccionario_grmtipo2_noterminal_inicial = dict() #Declaramos diccionario que contiene los estados iniciales del AFD
    diccionario_grmtipo2_noterminal_aceptacion = dict() #Declaramos diccionario que contiene los estados de aceptacion del AFD
    diccionario_grmtipo2_producciones = dict() #Declaramos diccionario que contiene los estados de aceptacion del AFD
    diccionario_grmtipo2_producciones_metodo2 = dict() #Declaramos diccionario el metodo 2 para reportes
    diccionario_grmtipo2_producciones_metodo2_original = dict() #Declaramos diccionario el metodo 2 transformado a metodo 1 para usarlos en las validación de cadenas

    listaNoTerminales = []
    listaTerminales = []
    listaNoTerminalInicial = []
    listaNoTerminalesAceptacion = []
    listaProducciones = []
    listaProduccionesMetodo2 = []

    def __init__(self, nombre): #Inicializamos la gramática pasando por parámetros el nombre y self.
        self.nombre = nombre

    def inicio(self):
        # INSTANCIAMOS LA CLASE DENTRO DE SÍ MISMA y creamos el objeto xy que referencia al objeto gramática
        xy = GRM_TIPO2 (self.nombre) # Pasamos en la instancia el parámetro del nombre de la gramática que se utiliza en ese momento 
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ INGRESAR O MODIFICAR GRAMÁTICA #########################")
        xy.mostrar_menu(self.listaNoTerminales, self.listaTerminales, self.listaNoTerminalInicial, self.listaNoTerminalesAceptacion, self.listaProducciones, self.listaProduccionesMetodo2) #Llamamos al método menú

    # Declaramos más MÉTODOS que llevan el parámetro self, que se refiere al objeto del método que se está siendo llamado, es decir self
    def ingresarTerminales(self):
        xy = GRM_TIPO2 (self.nombre)
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ INGRESAR O MODIFICAR GRAMÁTICA >> Ingresar Terminales (Alfabeto) de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_terminales()

    def ingresarNoTerminales(self):
        xy = GRM_TIPO2 (self.nombre)
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ INGRESAR O MODIFICAR GRAMÁTICA >> Ingresar no terminales (Estados) de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_no_terminales()

    def estadoInicial(self):
        xy = GRM_TIPO2 (self.nombre)
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ INGRESAR O MODIFICAR GRAMÁTICA >> No Terminal Inicial (Estado inicial) de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_no_terminales_inicial()

    def ingresarProducciones(self):
        xy = GRM_TIPO2 (self.nombre)
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ INGRESAR O MODIFICAR GRAMÁTICA >> Ingresar producciones (Transiciones) de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_ingresar_producciones()

    def borrarProducciones(self):
        xy = GRM_TIPO2 (self.nombre)
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ INGRESAR O MODIFICAR GRAMÁTICA >> Borrar producciones de "+ self.nombre +"  #########################")
        print ("")
        xy.menu_borrar_producciones()

    def menu_ingresar_terminales(self):
        xy = GRM_TIPO2(self.nombre)
        if xy.diccionario_grmtipo2_terminales: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_grmtipo2_terminales: #Verificamos que la clave (nombre de AFD) exista
                print ("Los símbolos (alfabeto) o terminales guardado de "+self.nombre+" son: "+xy.diccionario_grmtipo2_terminales[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese un símbolo o terminal de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar símbolo o terminal: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_terminales(estado)

    def guardar_terminales(self,estado):
        xy = GRM_TIPO2(self.nombre)
        if estado:
            if (estado.isspace()):
                print ("No puedes ingresar simbolos vacios.")
            else:
                if(len(estado)>1):
                    print ("Solo puedes ingresar un terminal a la vez")
                elif estado.isupper():
                    print ("No se puede ingresar letras mayúsculas")
                elif estado in self.listaTerminales: # Imprime lo de abajo
                    print ("El símbolo o terminal "+estado+ " ya existe en la Gramática "+ self.nombre +". Por favor, ingrese otro símbolo del alfabeto o terminal.")
                else:  
                    self.listaTerminales.append(estado)
                    xy.diccionario_grmtipo2_terminales.update({self.nombre:xy.recorrer_lista_terminales()})
                    print ("Símbolos del alfabeto o terminales guardados: "+xy.diccionario_grmtipo2_terminales[self.nombre])
        else:
            print("No puedes ingresar un símbolo vacio. Por ingresa un símbolo o terminal.")

    def menu_ingresar_no_terminales(self): #No Terminales
        xy = GRM_TIPO2(self.nombre)
        if xy.diccionario_grmtipo2_noterminales: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_grmtipo2_noterminales: #Verificamos que la clave (nombre de AFD) exista
                print ("Los No Terminales guardados de "+self.nombre+" son: "+xy.diccionario_grmtipo2_noterminales[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese el No Terminal de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar No Terminal: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_no_terminal(estado)

    def guardar_no_terminal(self,estado):
        xy = GRM_TIPO2(self.nombre)
        estado1 = ''
        estado = estado.replace(" ","")
        estado = estado.replace("*","")
        if estado:
            estado1 = estado[0:1]
            if estado1.islower():
                print ("La primera letra debe ser mayúscula")
            elif estado1.isdigit():
                print("La primera letra debe ser mayúscula, no números ni caracteres extraños.")
            elif not estado1 in string.ascii_uppercase:
                print("Puedes ingresar solo letras mayúsculas, no números ni caracteres extraños.")
            else:
                estadox=estado+"*"
                if estadox in self.listaNoTerminales: # Imprime lo de abajo
                    print ("El estado o No Terminal "+estado+ " ya existe en la Gramática "+ self.nombre +". Por favor, ingresa otro estado o No Terminal.")
                else:
                    self.listaNoTerminales.append(estado+'*')
                    xy.diccionario_grmtipo2_noterminales.update({self.nombre:xy.recorrer_lista_no_terminales()})
                    print ("Estados guardados o No Terminales: "+xy.diccionario_grmtipo2_noterminales[self.nombre])
                    print (self.listaNoTerminales)
        else:
            print("No puedes ingresar un estado vacio. Por ingresa un estado.")

    def menu_ingresar_no_terminales_inicial(self):
        xy = GRM_TIPO2(self.nombre)
        if xy.diccionario_grmtipo2_noterminal_inicial: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_grmtipo2_noterminal_inicial: #Verificamos que la clave (nombre de AFD) exista
                print ("El estado inicial o no terminal inicial guardado de "+self.nombre+" es: "+xy.diccionario_grmtipo2_noterminal_inicial[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese un estado inicial o no terminal inicial de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar No terminal inicial: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_no_terminal_inicial(estado)

    def guardar_no_terminal_inicial(self,estado):
        xy = GRM_TIPO2(self.nombre)
        estado = estado.replace(" ","")
        estado = estado.replace("*","")
        if estado:
            if xy.diccionario_grmtipo2_noterminales: #Verificamos que no esté vacio el diccionario de estados de aceptacion
                if self.nombre in xy.diccionario_grmtipo2_noterminales: #Verificamos que la clave (nombre de AFD) exista
                    estadox=estado+"*"
                    if not estadox in self.listaNoTerminales: #Si no existe el estado ingresado en los estados declarados, hacer:
                        print ("El estado ingresado o no terminal inicial no existe en los estados declarados de la Gramática: " + self.nombre)
                    else:
                        self.listaNoTerminalInicial.clear()
                        self.listaNoTerminalInicial.append(estado)
                        xy.diccionario_grmtipo2_noterminal_inicial.update({self.nombre:estado})
                        print ("Estado o no terminal inicial guardado exitosamente: "+xy.diccionario_grmtipo2_noterminal_inicial[self.nombre])
                else:
                    print ("El estado ingresado o no terminal inicial no existe en los estados o No Terminales declarados de la Gramática: " + self.nombre)
            else:
                print ("El estado o no terminal inicial ingresado no existe en los estados o No Terminales declarados de la Gramática: " + self.nombre)
        else:
            print("No puedes ingresar un estado o no terminal inicial vacio. Por ingresa un estado o no terminal inicial.")

    def menu_ingresar_producciones(self):
        xy = GRM_TIPO2(self.nombre)
        if xy.diccionario_grmtipo2_producciones: #Verificamos que no esté vacio el diccionario
            if self.nombre in xy.diccionario_grmtipo2_producciones: #Verificamos que la clave (nombre de AFD) exista
                print ("Las producciones guardadas de "+self.nombre+" son: "+xy.diccionario_grmtipo2_producciones[self.nombre])
                print ("")
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese las producciones de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar producción: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.guardar_producciones(estado)

    def menu_borrar_producciones(self):
        xy = GRM_TIPO2(self.nombre)
        salir = False
        opcion = 0
        print ("Escriba salir para regresar al menú anterior o ingrese las producciones a borrar de: "+ self.nombre)
        print ("")

        while not salir:
            print ("")
            estado = input("Ingresar producción a borrar: ")
            if estado == "salir":
                salir = True
                os.system(var)
                xy.inicio()
            else:
                xy.borrar_producciones(estado)

    def guardar_producciones(self,estado):
        xy = GRM_TIPO2(self.nombre)
        estado1 = ""
        estado2 = ""
        simbolo = ""
        cadena1 = []
        cadena2 = []

        lista1 = []
        pos_inicial1 = -1
        lista2 = []
        pos_inicial2 = -1
        posicion_coma = 0
        posicion_pc = 0

        estado_estado = ""

        estado = estado.replace(" ","")

        if estado:
            if not ">" in estado:
                print ("No existe el caracter especial '>'en la cadena de texto. Por favor, ingresa una cadena de texto correta.")
            elif ">" in estado:
                    
                    cadena1 = estado.split(">")
                    estado1 = cadena1[0] #Obtenemos el estado 1
                    estado_estado = estado1[0:1]
                    estado2 = cadena1[1]
                    #estado1 = estado1.upper()

                    if "epsilon" in cadena1[1] or "Epsilon" in cadena1[1]:
                        estado2 = "epsilon"
                    elif(len(estado)<=2):
                        estado2 = "epsilon"

                    if estado_estado.isdigit():
                        print("La primera letra del No Terminal sólo puede ser letras mayúsculas, no números ni caracteres extraños")
                    elif not estado_estado in string.ascii_uppercase:
                        print("La primera letra del No Terminal sólo puede ser letras mayúsculas, no números ni caracteres extraños")
                    elif self.nombre in xy.diccionario_grmtipo2_noterminales: #Verificamos que la clave (nombre de AFD) exista
                        estadox=estado1+"*"
                        if not estadox in self.listaNoTerminales:
                        #if not estado1 in xy.diccionario_grmtipo2_noterminales[self.nombre]: #Si no existe el estado ingresado en los estados declarados, hacer:
                            print ("El No Terminal ingresado no existe en los No Terminales declarados de la Gramática Tipo 2: " + self.nombre)
                        elif xy.revisar_doble_estado_transicion_metodo1(estado1,estado2)=='t':
                            print ("Intenta ingresar dos producciones de forma repetida.")
                        else:
                            self.listaProducciones.append(estado1+">"+estado2+"*")
                            xy.diccionario_grmtipo2_producciones.pop(self.nombre,None) # Eliminamos el elemento o vaciamos el mismo
                            xy.diccionario_grmtipo2_producciones.update({self.nombre:xy.recorrer_lista_transiciones_metodo1_afd()})
                            print ("Producciones guardadas exitosamente separadas por * (Diccionario): "+xy.diccionario_grmtipo2_producciones[self.nombre])
                            print ("Producciones guardadas exitosamente separadas por * (Lista):")
                            print (xy.listaProducciones)
                            #if estado2 == 'epsilon':
                            #     xy.diccionario_grmtipo2_noterminal_aceptacion.update({self.nombre:estado1})
                    else:
                        print ("Los No Terminales ingresados no existen en los No Terminales declarados de la gramática: " + self.nombre) 
        else:
            print("No puedes ingresar producciones vacías. Por favor, ingresa una producción.")

    def borrar_producciones(self,estado):
        xy = GRM_TIPO2(self.nombre)
        estado1 = ""
        estado2 = ""
        simbolo = ""
        cadena1 = []
        cadena2 = []

        estado = estado.replace(" ","")
        estado = estado.replace("*","")

        if estado:
            if not ">" in estado:
                print ("No existe el caracter especial '>'en la cadena de texto. Por favor, ingresa una cadena de texto correta.")
            elif ">" in estado:
                    cadena1 = estado.split(">")
                    estado1 = cadena1[0] #Obtenemos el estado 1
                    estado2 = cadena1[1]
                    estado1 = estado1.upper()

                    if "epsilon" in cadena1[1] or "Epsilon" in cadena1[1]:
                        estado2 = "epsilon"
                    elif(estado[len(estado)-1]=='>'):
                        estado2 = "epsilon"

                    if xy.revisar_doble_estado_transicion_metodo1(estado1,estado2)=='t':
                        for i in range(len(xy.listaProducciones)-1, -1, -1):
                            if xy.listaProducciones[i] == estado1+">"+estado2+"*":
                                tranquis = xy.diccionario_grmtipo2_producciones[self.nombre].replace(xy.listaProducciones[i],"")
                                xy.diccionario_grmtipo2_producciones.pop(self.nombre,None) # Eliminamos el elemento o vaciamos el mismo
                                xy.diccionario_grmtipo2_producciones.update({self.nombre:tranquis})
                                del xy.listaProducciones[i]
                        print ("La producción ha sido borrada exitosamente")
                    else:
                        print ("La producción ingresada no existe en las producciones declarados de la gramática: " + self.nombre)
        else:
            print("No puedes ingresar producciones vacías. Por favor, ingresa una producción.")

    def mostrar_menu(self, pendejo, pendejo_alfabeto, pendejo_estado_inicial, pendejo_estados_aceptacion, pendejo_lista_transiciones_afd, pendejo_lista_transiciones_afd_m2):
        xy = GRM_TIPO2(self.nombre)

        xy.transformar_dict_to_list_producciones()
        xy.transformar_dict_to_list_noterminales(xy.diccionario_grmtipo2_noterminales, xy.listaNoTerminales)
        xy.transformar_dict_to_list_general(xy.diccionario_grmtipo2_terminales, xy.listaTerminales)
        xy.transformar_dict_to_list_noterminale_inicial(xy.diccionario_grmtipo2_noterminal_inicial, xy.listaNoTerminalInicial)

        salir = False
        opcion = 0
        
        print ("")
        print ("    1. Ingresar terminales (alfabeto)")
        print ("    2. Ingresar no terminales (estados)")
        print ("    3. Ingresar producciones")
        print ("    4. Borrar producciones")
        print ("    5. No terminal inicial")
        print ("    6. Regresar al menú de Gramática Tipo 2")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.ingresarTerminales() #Ingresar NT
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.ingresarNoTerminales() #Ingresar Terminales
            elif opcion == 3:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.ingresarProducciones() #Ingresar Terminales
            elif opcion == 4:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.borrarProducciones() #Ingresar Terminales
            elif opcion == 5:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.estadoInicial()
            elif opcion == 6:

                pendejo.clear() #Borramos lista de estados
                pendejo_alfabeto.clear() #Borramos lista de alfabeto
                pendejo_estado_inicial.clear() # Borramos el estado inicial
                pendejo_estados_aceptacion.clear() #Borramos estados de aceptacion
                pendejo_lista_transiciones_afd.clear()
                pendejo_lista_transiciones_afd_m2.clear()
                
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                menu_general_grm_tipo2()
            else:
                print ("Introduce un numero entre 1 y 6")


    #*******************************************    Métodos generales ********************************

    def recorrer_lista_no_terminales(self):
        x = ''
        for i in self.listaNoTerminales:
            x = x + i
        return x

    def recorrer_lista_terminales(self):
        x = ''
        for i in self.listaTerminales:
            x = x + i
        return x

    def recorrer_lista_no_terminales_aceptacion(self):
        x = ''
        for i in self.listaNoTerminalesAceptacion:
            x = x + i
        return x

    def recorrer_lista_transiciones_metodo1_afd(self):
        x = ''
        for i in self.listaProducciones:
            x = x + i
        return x

    def concatenar_letras_comas(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        can = "{"+can+"}"
        return can

    def concatenar_letras_comas_sin_llaves(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        return can

    def revisar_doble_estado_transicion_metodo1(self,e1,e2):
        estado1 = ""
        estado2 = ""
        cadena1 = []
        cadena2 = []
        y = 'f'
        if self.listaProducciones:
            for x in self.listaProducciones:
                x = x.replace("*","")
                cadena1 = x.split(">")
                if cadena1[1] == "epsilon":
                    estado2 = "epsilon"
                else:
                    estado2 = cadena1[1]
                estado1 = cadena1[0]
                estado2 = cadena1[1]
                if e1 == estado1 and e2 == estado2:
                    y = 't'
        return y

    def transformar_dict_to_list_producciones(self):
        xy = GRM_TIPO2(self.nombre)
        xy.listaProducciones.clear()
        y = ''
        if self.nombre in xy.diccionario_grmtipo2_producciones:
            for x in xy.diccionario_grmtipo2_producciones[self.nombre]:
                if x!='*':
                    y = y + x
                else:
                    xy.listaProducciones.append(y+'*')
                    y = ''
        else:
            xy.listaProducciones.clear()

    def transformar_dict_to_list_general(self,d,l):
        l.clear()
        if self.nombre in d:
            for x in d[self.nombre]:
                l.append(x)
        else:
            l.clear()

    def transformar_dict_to_list_noterminales(self,d,l):
        l.clear()
        y = ''
        if self.nombre in d:
            for x in d[self.nombre]:
                if x!='*':
                    y = y + x
                else:
                    l.append(y+'*')
                    y = ''
        else:
            l.clear()

    def transformar_dict_to_list_noterminale_inicial(self,d,l):
        l.clear()
        y = ''
        if self.nombre in d:
            for x in d[self.nombre]:
                y = y + x
            l.append(y)
            y = ''
        else:
            l.clear()

    def salir_menu(self):
        xy = GRM_TIPO2(self.nombre)
        salir = False
        opcion = 0
        
        print ("")
        print ("Ingrese << 0 >> para regresar al menú anterior")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 0:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                menu_general_grm_tipo2() #Ingresar NT
            else:
                print ("Introduce 0 para regresar al menú anterior")


# **************************************************** GENERAR AUTÓMATA ****************************************************************

class GENERAR_AUTOMATA:
    nombre = '' # Declaramos el atributo nombre

    #Declaramos las variables, listas y diccionarios a usar
    diccionario_transiciones_automatas_pila = dict() #Declaramos diccionario que contiene los nombres de AFDs y su conjunto de estados pertenecientes a cada uno
    lista_transiciones_automatas_pila = [] # Servirá para guardarlo en los diccionarios
    lista_producciones_transiciones = [] # Servirá para graficar el paso 5
    lista_estados_transiciones = [] # Servirá para graficar el paso 5

    pila = []
    entrada = []
    entrada_string = ""
    transiciones_automata = []
    transiciones_impresas = []

    estados = ["i","p","q","f"]
    #trans = [("A","B", 1),("A","E",0),("A","E",1),("A","A",1),("A","D",1),("F","F",1),("D","C",1),("B","A",0), ("E","C",0),("F","D",0), ("C","A",0), ("B","B", 1)]
    trans = []
    inicial = ["i"]
    alf = []
    terminal = ()
    l = list(terminal)
    l.append("f")
    terminal = tuple(l)

    x_contador_pila = 0

    def __init__(self, nombre): #Inicializamos el autómata pasando por parámetros el nombre y self.
        self.nombre = nombre

    def inicio(self):
        # INSTANCIAMOS LA CLASE DENTRO DE SÍ MISMA y creamos el objeto xy que referencia al objeto Generar Autómata
        xy = GENERAR_AUTOMATA (self.nombre) # Pasamos en la instancia el parámetro del nombre de la gramática que se utiliza en ese momento 
        xy.generarAutomata() #Llamamos al método Generar Autómata

    def generarAutomata(self):
        xy = GENERAR_AUTOMATA (self.nombre)
        xxx = GRM_TIPO2(self.nombre)

        #Declaramos las variables de transiciones
        x1 = ""
        x2 = ""
        x3 = ""
        x4 = ""
        x5 = ""

        print ("#######################  PROYECTO 2  #########################")
        print ("#######################  Generación de autómata de pila asociada a la gramática "+ self.nombre +"  #########################")
        print ("")

        # Agregamos los terminales de la gramática al alfabeto del Autómata de pila
        if xxx.diccionario_grmtipo2_terminales: #Verificamos que no esté vacio el diccionario
            if self.nombre in xxx.diccionario_grmtipo2_terminales: #Verificamos que la clave (nombre de AFD) exista
                for x in xxx.diccionario_grmtipo2_terminales[self.nombre]:
                    xy.alf.append(x)
                
                #Paso 3 de i a p
                x1 = "i" # Declaramos el estado actual
                x2 = xy.leer_entrada(xy.entrada, xy.entrada_string) # Leemos el símbolo del alfabeto que lee la entrada
                x3 = xy.pop(xy.pila, xy.x_contador_pila) #Extraemos símbolo de la pila
                x4 = "p" # Declaramos el estado a pasar
                x5 = xy.push(xy.pila, "#", "#") #Insertamos símbolo en la pila
                xy.push_transiciones_automata(3, x1, x2, x3, x4, x5)
                xy.x_contador_pila = 0
                self.lista_transiciones_automatas_pila.append(x1+", "+x2+", "+x3+"; "+x4+", "+x5+"*")
                xy.diccionario_transiciones_automatas_pila.update({self.nombre:xy.recorrer_lista_transiciones_metodo1_afd()})


                #Paso 4 de p a q
                if xxx.diccionario_grmtipo2_noterminal_inicial: #Verificamos que no esté vacio el diccionario
                    if self.nombre in xxx.diccionario_grmtipo2_noterminal_inicial: #Verificamos que la clave (nombre de AFD) exista
                        x1 = "p" # Declaramos el estado actual
                        x2 = xy.leer_entrada(xy.entrada, xy.entrada_string) # Leemos el símbolo del alfabeto que lee la entrada
                        x3 = xy.pop(xy.pila, xy.x_contador_pila) #Extraemos símbolo de la pila
                        x4 = "q" # Declaramos el estado a pasar
                        x5 = xy.push(xy.pila, xxx.diccionario_grmtipo2_noterminal_inicial[self.nombre], xxx.diccionario_grmtipo2_noterminal_inicial[self.nombre]) #Insertamos símbolo en la pila que sería el Estado Inicial de la Gramática
                        xy.push_transiciones_automata(4, x1, x2, x3, x4, x5)
                        xy.x_contador_pila = 1
                        self.lista_transiciones_automatas_pila.append(x1+", "+x2+", "+x3+"; "+x4+", "+x5+"*")
                        xy.diccionario_transiciones_automatas_pila.update({self.nombre:xy.recorrer_lista_transiciones_metodo1_afd()})

                        #Paso 5 de q a q
                        xy.transformar_dict_to_list_producciones()
                        mi_cont = 0
                        for x in xy.lista_producciones_transiciones:
                            x1 = "q" # Declaramos el estado actual
                            x2 = xy.leer_entrada(xy.entrada, xy.entrada_string) # Leemos el símbolo del alfabeto que lee la entrada
                            if mi_cont == 0:
                                if xxx.diccionario_grmtipo2_noterminal_inicial[self.nombre] == xy.lista_estados_transiciones[0]:
                                    #xsdd = xy.pop(xy.pila, xy.x_contador_pila) #Extraemos símbolo de la pila
                                    x5 = xy.push(xy.pila, xy.lista_estados_transiciones[mi_cont], x) #Insertamos símbolo en la pila que sería el Estado Inicial de la Gramática
                                    x3 = xy.pop(xy.pila, xy.x_contador_pila) #Extraemos símbolo de la pila
                                    xsdd = xy.pop(xy.pila, xy.x_contador_pila) #Extraemos símbolo de la pila
                                    x4 = "q" # Declaramos el estado a pasar
                                    xy.push(xy.pila, xy.lista_estados_transiciones[xy.pendejos(mi_cont)], "abcdef") #Insertamos símbolo en la pila que sería el Estado Inicial de la Gramática
                                else:
                                    x5 = xy.push(xy.pila, xy.lista_estados_transiciones[mi_cont], x) #Insertamos símbolo en la pila que sería el Estado Inicial de la Gramática
                                    x3 = xy.pop(xy.pila, xy.x_contador_pila) #Extraemos símbolo de la pila
                                    x4 = "q" # Declaramos el estado a pasar
                            else:
                                x5 = xy.push(xy.pila, xy.lista_estados_transiciones[mi_cont], x) #Insertamos símbolo en la pila que sería el Estado Inicial de la Gramática
                                x3 = xy.pop(xy.pila, xy.x_contador_pila) #Extraemos símbolo de la pila
                                x4 = "q" # Declaramos el estado a pasar
                            xy.push_transiciones_automata(5, x1, x2, x3, x4, x5)
                            xy.x_contador_pila = 2
                            self.lista_transiciones_automatas_pila.append(x1+", "+x2+", "+x3+"; "+x4+", "+x5+"*")
                            xy.diccionario_transiciones_automatas_pila.update({self.nombre:xy.recorrer_lista_transiciones_metodo1_afd()})
                            mi_cont = mi_cont + 1

                        #Paso 6 de q a q
                        for k in xxx.diccionario_grmtipo2_terminales[self.nombre]:
                            x5 = xy.push(xy.pila, k, "λ")
                            x2 = k
                            x3 = xy.pop(xy.pila, xy.x_contador_pila) #Extraemos símbolo de la pila
                            xy.push_transiciones_automata(5, x1, x2, x3, x4, x5)
                            xy.x_contador_pila = 2
                            self.lista_transiciones_automatas_pila.append(x1+", "+x2+", "+x3+"; "+x4+", "+x5+"*")
                            xy.diccionario_transiciones_automatas_pila.update({self.nombre:xy.recorrer_lista_transiciones_metodo1_afd()})
                            mi_cont = mi_cont + 1


                        #Paso 7 de q a f
                        x1 = "q" # Declaramos el estado actual
                        x2 = xy.leer_entrada(xy.entrada, xy.entrada_string) # Leemos el símbolo del alfabeto que lee la entrada
                        x3 = xy.pop(xy.pila, xy.x_contador_pila) #Extraemos símbolo de la pila
                        x3 = xy.pop(xy.pila, xy.x_contador_pila) #Extraemos símbolo de la pila
                        x4 = "f" # Declaramos el estado a pasar
                        x5 = xy.push(xy.pila, "λ", "λ") #Insertamos símbolo en la pila
                        xy.push_transiciones_automata(3, x1, x2, x3, x4, x5)
                        xy.x_contador_pila = 0
                        self.lista_transiciones_automatas_pila.append(x1+", "+x2+", "+x3+"; "+x4+", "+x5+"*")
                        xy.diccionario_transiciones_automatas_pila.update({self.nombre:xy.recorrer_lista_transiciones_metodo1_afd()})


                        print (xy.trans)
                        print (xy.estados)
                        print (xy.inicial)
                        print (xy.terminal)
                        print (xy.alf)
                        print ("Transiciones diccionario: "+xy.diccionario_transiciones_automatas_pila[self.nombre])
                        print (xy.pila)
                        print (xy.x_contador_pila)









                        xy.draw(xy.alf, xy.estados, xy.inicial, xy.trans, xy.terminal)
                        print ("El Autómata se ha generado exitosamente")

            else:
                print ("No hay terminales declarados de la gramática")
        else:
            print ("No hay terminales declarados de la gramática")




        
        xy.salir_menu()


    #***************************** Funciones para generar el autómata de pila usando el paradigma funcional **************************

    def pendejos(self, mi_cont):
        xy = GENERAR_AUTOMATA (self.nombre)
        cant = 0
        if mi_cont >= len(xy.lista_estados_transiciones):
            cant = mi_cont
        else:
            cant = mi_cont + 1
        return cant

    def leer_entrada(self, ent_arreglo, ent_string):
        x = ''
        if ent_string == "":
            x = 'λ'
        return x 

    def push(self, pila, simbolo_insertar_pila, simbolo_a_devolver):
        x = simbolo_insertar_pila
        z = simbolo_a_devolver
        #x = x[0:1]
        pila.append(x)
        return z 

    def pop(self, pila, contador):
        xy = GENERAR_AUTOMATA (self.nombre)
        x = ''
        if contador == 0:
            x = 'λ'
        elif contador == 1:
            x = pila.pop()
        elif contador == 2:
            x = pila.pop()
        return x 

    def push_transiciones_automata(self,paso, x1, x2, x3, x4, x5):
        xy = GENERAR_AUTOMATA (self.nombre)
        xxx = GRM_TIPO2(self.nombre)
        xxxx = []
        my_list = []
        #transiciones = xxx.diccionario_afd_transiciones[self.nombre].replace(";",",")
        #my_list = transiciones.split(",")
        
        """if paso != 3:
            for x in transiciones:
                if x!='*':
                    if x!=',':
                        xxxx.append(x)
                    else: 
                        xy.trans.append(tuple(xxxx))
                        xxxx.clear()
        el"""
        if paso == 3 or paso == 4 or paso==5:
            alles = x2+",  "+x3+";  "+x5
            xxxx = [x1, x4, alles]
            xy.trans.append(tuple(xxxx))
            xxxx.clear()



    def draw(self,alfabeto, estados, inicio, trans, final):
        print("inicio:", str(inicio))
        g = gv.Digraph(format='png')
        g.graph_attr['rankdir'] = 'LR'
        g.node('ini', shape="point")
        for e in estados:
            if e in final:
                g.node(e, shape="doublecircle")
            else:
                g.node(e)
            if e in inicio:
                g.edge('ini',e)
        for t in trans:
            #if t[2] not in alfabeto:
            #    return 0
            g.edge(t[0], t[1], label=str(t[2]), len='1.00')
        #g.render(view=True)
        g.render(self.nombre+'.gv', view=True)


    #*******************************************    Métodos generales ********************************

    def concatenar_letras_comas(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        can = "{"+can+"}"
        return can

    def concatenar_letras_comas_sin_llaves(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        return can

    def concatenar_simbolos_de_pila(self):
        xxx = GRM_TIPO2(self.nombre)
        can = ''
        can2 = ''
        can_total = ''
        for x in xxx.diccionario_grmtipo2_terminales[self.nombre]:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        for x in xxx.diccionario_grmtipo2_noterminales[self.nombre]:
            can2 = can2 + x +","
        if can2[len(can2)-1] == ",":
            can2 = can2[:len(can2) - 1]
        can_total = '{'+can+','+can2+','+'#}'
        return can_total

    def recorrer_lista_transiciones_metodo1_afd(self):
        x = ''
        for i in self.lista_transiciones_automatas_pila:
            x = x + i
        return x

    def string_to_list(self, cadena, lista):
        for i in cadena:
            lista.append(i)

    def transformar_dict_to_list_producciones(self):
        xy = GRM_TIPO2(self.nombre)
        xxxx = GENERAR_AUTOMATA(self.nombre)
        xxxx.lista_producciones_transiciones.clear()
        y = ''
        z = ''
        contador = 0
        cadena1 = []
        if self.nombre in xy.diccionario_grmtipo2_producciones:
            for x in xy.diccionario_grmtipo2_producciones[self.nombre]:
                if x!='*':
                    y = y + x
                else:
                    #cadena1 = xy.diccionario_grmtipo2_producciones[self.nombre][contador].split(">")
                    cadena1 = y.split(">")
                    #z = y[0:1]
                    z = cadena1[0]
                    #y = y[2:]
                    y = cadena1[1]

                    print (cadena1)
                    


                    xxxx.lista_producciones_transiciones.append(y)
                    xxxx.lista_estados_transiciones.append(z)
                    y = ''
                    z = ''
                    contador = contador + 1
        else:
            xxxx.lista_producciones_transiciones.clear()
            xxxx.lista_estados_transiciones.clear()

    def salir_menu(self):
        xy = GENERAR_AUTOMATA(self.nombre)
        salir = False
        opcion = 0
        
        print ("")
        print ("Ingrese << 0 >> para regresar al menú anterior")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 0:


                xy.lista_transiciones_automatas_pila.clear() #Borramos lista de estados
                xy.pila.clear()
                xy.entrada.clear()
                xy.entrada_string = ""
                xy.transiciones_automata.clear()
                xy.transiciones_impresas.clear()
                xy.trans.clear()
                xy.alf.clear()

                xy.lista_producciones_transiciones.clear()
                xy.lista_estados_transiciones.clear()

                #xy.terminal.clear()


                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                menu_general_grm_tipo2()
            else:
                print ("Introduce 0 para regresar al menú anterior")


# ****************************************************VISUALIZAR AUTÓMATA ****************************************************************

class VISUALIZAR_AUTOMATA:
    nombre = '' # Declaramos el atributo nombre

    def __init__(self, nombre): #Inicializamos el autómata pasando por parámetros el nombre y self.
        self.nombre = nombre

    def inicio(self):
        # INSTANCIAMOS LA CLASE DENTRO DE SÍ MISMA y creamos el objeto xy que referencia al objeto Visualizar Autómata
        xy = VISUALIZAR_AUTOMATA (self.nombre) # Pasamos en la instancia el parámetro del nombre de la gramática que se utiliza en ese momento 
        xy.visualizarAutomata() #Llamamos al método Visualizar Autómata

    def visualizarAutomata(self):
        xy = VISUALIZAR_AUTOMATA (self.nombre)
        xxx = GRM_TIPO2(self.nombre)
        xyxy = GENERAR_AUTOMATA(self.nombre)
        print ("#######################  PROYECTO 2  #########################")
        print ("#######################  Visualizar autómata de pila asociada a la gramática "+ self.nombre +"  #########################")
        print ("")

        print ("    Séxtupla del Autómata de Pila asociada a la gramática: "+self.nombre)
        print ("")

        print ("        S: {i, p, q, f}")
        #Este está correcto
        if xxx.diccionario_grmtipo2_terminales: #Verificamos que no esté vacio el diccionario
            if self.nombre in xxx.diccionario_grmtipo2_terminales: #Verificamos que la clave exista
                print ("        Σ (Terminales o Alfabeto): " +xy.concatenar_letras_comas(xxx.diccionario_grmtipo2_terminales[self.nombre]))
            else:
                print ("        No está definido el alfabeto o Terminales de la gramática "+self.nombre)
        else:
            print ("       No está definido el alfabeto o Terminales de la gramática "+self.nombre)

        #Este está correcto
        if xxx.diccionario_grmtipo2_terminales: #Verificamos que no esté vacio el diccionario
            if self.nombre in xxx.diccionario_grmtipo2_terminales: #Verificamos que la clave exista
                if xxx.diccionario_grmtipo2_noterminales: #Verificamos que no esté vacio el diccionario
                    if self.nombre in xxx.diccionario_grmtipo2_noterminales: #Verificamos que la clave exista
                                print ("        Γ (Simbolos de Pila del Autómata): " +xy.concatenar_simbolos_de_pila())
                    else:
                        print ("        No está definido los No Terminales de la gramática "+self.nombre)
                else:
                    print ("       No está definido los No Terminales de la gramática "+self.nombre)
            else:
                print ("        No está definido el alfabeto o Terminales de la gramática "+self.nombre)
        else:
            print ("       No está definido el alfabeto o Terminales de la gramática "+self.nombre)

        print ("        L: { i }")
        print ("        F: { f }")
        
        if xyxy.diccionario_transiciones_automatas_pila: #Verificamos que no esté vacio el diccionario
            if self.nombre in xyxy.diccionario_transiciones_automatas_pila: #Verificamos que la clave exista
                print ("        T: ")
                print ("            "+xy.separar_transiciones_del_automata())
            else:
                print ("        No están definidas las transiciones del autómata de Pila "+self.nombre)
        else:
            print ("       No están definidas las transiciones del autómata de Pila "+self.nombre)


        #i = Image.open(self.nombre+'.gv.png','r') 
        #i.show()

        path1 = pathlib.Path(self.nombre+'.gv.png')
        path2 = pathlib.Path("C:/Users/USUARIO/proyecto1_lenguajes/"+self.nombre+".gv.png")
        path3 = pathlib.Path("C:/Users/USUARIO/"+self.nombre+".gv.png")
        #path4 = pathlib.Path(self.nombre+'.gv.png')

        if path1.is_file():
            i = Image.open(self.nombre+'.gv.png','r') 
            i.show()
        elif path2.is_file():
            i = Image.open("C:/Users/USUARIO/proyecto1_lenguajes/"+self.nombre+".gv.png",'r') 
            i.show()
        elif path3.is_file():
            i = Image.open("C:/Users/USUARIO/"+self.nombre+".gv.png",'r') 
            i.show()
        else:
            direccion = pedir_direccion_imagen_grm_tipo2_visualizar_automata()
            path4 = pathlib.Path(direccion)
            if path4.is_file():
                i = Image.open(direccion,'r') 
                i.show()
            else:
                print ("No se encontró archivo en la dirección ingresada.")

        xy.salir_menu()


    #*******************************************    Métodos generales ********************************

    def concatenar_letras_comas(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        can = "{"+can+"}"
        return can

    def concatenar_letras_comas_sin_llaves(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        return can

    def concatenar_simbolos_de_pila(self):
        xxx = GRM_TIPO2(self.nombre)
        can = ''
        can2 = ''
        can_total = ''
        y = ''
        for x in xxx.diccionario_grmtipo2_terminales[self.nombre]:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        for x in xxx.diccionario_grmtipo2_noterminales[self.nombre]:
            if x!='*':
                y = y + x
            else:
                can2 = can2 + y +","
                y = ''
        if can2[len(can2)-1] == ",":
            can2 = can2[:len(can2) - 1]
        can_total = '{'+can+','+can2+','+'#}'
        return can_total

    def separar_transiciones_del_automata(self):
        xyxy = GENERAR_AUTOMATA(self.nombre)
        can = ''
        can2 = ''
        can_total = ''
        y = ''
        for x in xyxy.diccionario_transiciones_automatas_pila[self.nombre]:
            if x!='*':
                y = y + x
            else:
                can2 = can2 + y +"\n"+"            "
                y = ''
        return can2

    def salir_menu(self):
        xy = VISUALIZAR_AUTOMATA(self.nombre)
        salir = False
        opcion = 0
        
        print ("")
        print ("Ingrese << 0 >> para regresar al menú anterior")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 0:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                menu_general_grm_tipo2()
            else:
                print ("Introduce 0 para regresar al menú anterior")


    def menu_no_imagen(self):
        xy = VISUALIZAR_AUTOMATA(self.nombre)
        salir = False
        opcion = 0
        
        print ("")
        print ("No se ha encontrado la imagen en los archivos buscados. Ingresa la dirección de la imagen, o Ingrese << 0 >> para regresar al menú anterior")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 0:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                menu_general_grm_tipo2()
            else:
                print ("Introduce 0 para regresar al menú anterior")

 # ****************************************************EVALUAR CADENA ****************************************************************
class EVALUAR_CADENA:
    nombre = '' # Declaramos el atributo nombre
    diccionario_cadena_a_evaluar = dict()
    listaProducciones = []
    listaProduccionesAuxiliar = []

    trans_arbol_normal = []

    pila = []
    pila_imprimir = []
    entrada = []
    entrada_imprimir = []
    transicion = []
    transicion_imprimir = []

    pila_dibujar_arbol = []


    def __init__(self, nombre): #Inicializamos la clase pasando por parámetros el nombre y self.
        self.nombre = nombre

    def evaluarCadena(self):
        xy = EVALUAR_CADENA (self.nombre)
        xy.menu_evaluar_cadena()

    def menu_evaluar_cadena(self):
        xy = EVALUAR_CADENA(self.nombre)

        xy.transformar_dict_to_list_producciones()
        xy.trans_arbol_normal.clear()
        xy.listaProduccionesAuxiliar = xy.listaProducciones[:]



        xy.pila.clear()
        xy.pila_imprimir.clear()
        xy.entrada.clear()
        xy.entrada_imprimir.clear()
        xy.transicion.clear()
        xy.transicion_imprimir.clear()
        xy.pila_dibujar_arbol.clear()



        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ EVALUAR CADENA de "+ self.nombre +"  #########################")
        print ("")
        salir = False
        opcion = 0
        
        print ("")
        print ("    1. Ingresar cadena")
        print ("    2. Ver resultado de la cadena ingresada (Generación del Arbol Sintáctico)")
        print ("    3. Generar reporte (Validación de la cadena con Autómata de Pila)")
        print ("    4. Regresar al menú de Gramática Tipo 2")
            
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.ingresarCadena() #Ingresar NT
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.verResultadoCadena() #Ingresar Terminales
            elif opcion == 3:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.generarReporteCadena() #Ingresar Terminales
            elif opcion == 4:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                menu_general_grm_tipo2()
            else:
                print ("Introduce un numero entre 1 y 4")

    def ingresarCadena(self):
        xy = EVALUAR_CADENA (self.nombre)
        cadena_a_evaluar = input("Introduce la cadena a evaluar: ")
        if (len(cadena_a_evaluar)>0):
            print ("La cadena ha sido ingresada con éxito")
            xy.diccionario_cadena_a_evaluar.update({self.nombre:cadena_a_evaluar})
        else:
            print ("Debes ingresar una cadena")
        xy.salir_menu()

    def verResultadoCadena(self):
        xy = EVALUAR_CADENA (self.nombre)
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### Resultado de la cadena ingresada  #########################")
        print ("")
        xy.evaluarCadenaMetodo()

    def generarReporteCadena(self):
        xy = EVALUAR_CADENA (self.nombre)
        xxx = GENERAR_AUTOMATA(self.nombre)
        yyy = GRM_TIPO2(self.nombre)
        print ("#######################  PROYECTO 2  #########################")
        print ("####################### Reporte de la cadena ingresada  #########################")
        print ("")

        contador = 0

        if xxx.diccionario_transiciones_automatas_pila: #Verificamos que no esté vacio el diccionario
            if self.nombre in xxx.diccionario_transiciones_automatas_pila: #Verificamos que la clave exista
                if xy.diccionario_cadena_a_evaluar: #Verificamos que no esté vacio el diccionario
                    if self.nombre in xy.diccionario_cadena_a_evaluar: #Verificamos que la clave exista
                        xy.separar_transiciones_del_automata() # Llenamos la lista de transiciones
                        for i in xy.diccionario_cadena_a_evaluar[self.nombre]:
                            xy.entrada.append(i)
                        xy.entrada_imprimir.append(xy.list_to_string(xy.entrada)) # Llenamos la entrada a imprimir
                        #Paso 1
                        xy.pila_imprimir.append(xy.pop(xy.pila,0))
                        xy.push(xy.pila, "#", "#", 0)
                        xy.transicion_imprimir.append("("+xy.transicion[0]+")")

                        #Paso 2
                        xy.entrada_imprimir.append(xy.list_to_string(xy.entrada)) # Llenamos la entrada a imprimir
                        xy.pila_imprimir.append(xy.pop(xy.pila,2))
                        xy.push(xy.pila, yyy.diccionario_grmtipo2_noterminal_inicial[self.nombre], yyy.diccionario_grmtipo2_noterminal_inicial[self.nombre], 0)
                        xy.transicion_imprimir.append("("+xy.transicion[1]+")")

                        #Paso 3
                        """xy.entrada_imprimir.append(xy.list_to_string(xy.entrada)) # Llenamos la entrada a imprimir
                        xy.pila_imprimir.append(xy.pop(xy.pila,1))
                        xy.push(xy.pila, "zMNz", "zMNz", 0)
                        xy.transicion_imprimir.append(xy.transicion[2])"""


                       

                        #Paso 4
                        #for x in xy.list_to_string(xy.entrada):
                        cccd = 0
                        for x in range(1,50):
                            if cccd == 0:
                                if len(xy.pila)>1 and len(xy.entrada)>0:
                                    xy.pila_imprimir.append(xy.list_to_string_reverse(xy.pila)) #Resolvimos el problema a mostrar en pila
                                    xy.entrada_imprimir.append(xy.list_to_string(xy.entrada)) #Resolvimos el problema de la entrada
                                    pila_for = xy.pop(xy.pila,1) #z
                                    if pila_for == xy.entrada[0]:
                                        t_imp = "(q, "+pila_for+", "+pila_for+"; "+ "q, "+ "λ)"
                                        xy.transicion_imprimir.append(t_imp) #Resolvimos el problema de transiciones
                                        del xy.entrada[0]
                                    else:
                                        loli = xy.search_produccion(pila_for, xy.entrada[0], xy.transicion, xy.entrada)
                                        if loli != '':
                                            t_imp = "(q, λ, "+pila_for+"; q, "+loli+")"
                                            xy.transicion_imprimir.append(t_imp) #Resolvimos el problema de transiciones
                                            xy.push(xy.pila, loli, loli, 5)
                                        else:
                                            #xy.pila_imprimir.pop()
                                            #xy.pila_imprimir.append("-------------") #Resolvimos el problema a mostrar en pila
                                            #xy.entrada_imprimir.pop()
                                            #xy.entrada_imprimir.append("-------------") #Resolvimos el problema de la entrada
                                            xy.transicion_imprimir.append("CADENA INVALIDA")
                                            cccd = 1
                                elif len(xy.pila)==1 and xy.pila[0]=="#" and len(xy.entrada)==0:
                                    xy.pila_imprimir.append(xy.list_to_string_reverse(xy.pila)) #Resolvimos el problema a mostrar en pila
                                    xy.entrada_imprimir.append("-------------") #Resolvimos el problema de la entrada
                                    pila_for = xy.pop(xy.pila,1) #z
                                    t_imp = "(q, λ, "+pila_for+"; f, λ)"
                                    xy.transicion_imprimir.append(t_imp)
                                elif len(xy.pila)==0 and len(xy.entrada)==0:
                                    xy.pila_imprimir.append("-------------") #Resolvimos el problema a mostrar en pila
                                    xy.entrada_imprimir.append("-------------") #Resolvimos el problema de la entrada
                                    xy.transicion_imprimir.append("CADENA ACEPTADA")
                                    cccd = 1
                                else:
                                    xy.pila_imprimir.append("-------------") #Resolvimos el problema a mostrar en pila
                                    xy.entrada_imprimir.append("-------------") #Resolvimos el problema de la entrada
                                    xy.transicion_imprimir.append("CADENA INVALIDA")
                                    cccd = 1




                            #if pila_for == xy.entrada:


                        
                        """xy.entrada_imprimir.append(xy.diccionario_cadena_a_evaluar[self.nombre]) # Llenamos la entrada a imprimir
                        xy.pila_imprimir.append(xy.pop(xy.pila,1))
                        xy.push(xy.pila, "λ", "λ", 1)
                        xy.transicion_imprimir.append(xy.transicion[2])"""


                        #MOSTRAMOS LA DATA A GUARDAR EN FORMATO LISTA
                        """data = {
                        'PILA': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
                        'ENTRADA': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
                        'TRANSICIÓN': [27, 31, 36, 53, 48, 36, 40, 34]}"""
                        data = {
                        'PILA': xy.pila_imprimir,
                        'ENTRADA': xy.entrada_imprimir,
                        'TRANSICIÓN': xy.transicion_imprimir}

                        #GUARDAMOS ARCHIVO CSV
                        df = pd.DataFrame(data, columns = ['PILA', 'ENTRADA', 'TRANSICIÓN'])
                        df.to_csv('example_semicolon.csv', sep='$')



                        path1 = pathlib.Path('example_semicolon.csv')
                        path2 = pathlib.Path("C:/Users/USUARIO/example_semicolon.csv")
                        path3 = pathlib.Path("C:/Users/USUARIO/proyecto1_lenguajes/example_semicolon.csv")

                        if path1.is_file():
                            #LEEMOS ARCHIVO CSV
                            df = pd.read_csv('example_semicolon.csv', sep='$', skiprows=1,
                                 names=['ID', 'PILA', 'ENTRADA', 'TRANSICIÓN'],
                                 na_values=['?'],
                                 index_col='ID')
                            df.head()
                        elif path2.is_file():
                            #LEEMOS ARCHIVO CSV
                            df = pd.read_csv('C:/Users/USUARIO/example_semicolon.csv', sep='$', skiprows=1,
                                 names=['ID', 'PILA', 'ENTRADA', 'TRANSICIÓN'],
                                 na_values=['?'],
                                 index_col='ID')
                            df.head()
                        elif path3.is_file():
                            #LEEMOS ARCHIVO CSV
                            df = pd.read_csv('C:/Users/USUARIO/proyecto1_lenguajes/example_semicolon.csv', sep='$', skiprows=1,
                                 names=['ID', 'PILA', 'ENTRADA', 'TRANSICIÓN'],
                                 na_values=['?'],
                                 index_col='ID')
                            df.head()



                        

                        #IMPRIMIMOS ARCHIVO CSV
                        print(tabulate(df, headers=['PILA', 'ENTRADA','TRANSICIÓN'], stralign='right', tablefmt='fancy_grid'))


                    else:
                        print("La cadena está vacia. Por favor, ingresa una cadena en el paso 1")
                else:
                    print("La cadena está vacia. Por favor, ingresa una cadena en el paso 1")
            else:
                print("No existen las transiciones del autómata de pila declaradas")
        else:
            print("No existen las transiciones del autómata de pila declaradas")        
        

        xy.salir_menu()

    def search_produccion(self, ppp, caracter_entrada, trans, entrada_completa):
        xy = EVALUAR_CADENA (self.nombre)
        xxx = GRM_TIPO2(self.nombre)
        y = ''
        estado = []
        estado3 = []
        cadena1 = ''
        cadena2 = ''
        cadena3 = ''
        est = []

        x = ''


        contador = 0

        for z in trans:
            if contador == 0:
                z.replace(" ", "")
                estado = z.split(";")
                cadena1 = estado[0]
                cadena2 = estado[1]

                cadena1 = cadena1.replace(" ","")
                
                cadena2 = cadena2.replace(" ","")
                dam = cadena2[2].replace(" ","")


                estado3 = cadena2.split(",")
                cadena3 = estado3[1]
 
                if dam == caracter_entrada and ppp == cadena1[4][0]:
                    ccc = 1
                    for d in cadena3: #Recorre la producción
                        if d.islower(): #Si es mayúscula
                            if d in entrada_completa:
                                if ccc == len(cadena3):
                                    contador = 1
                                    x = cadena3
                            else:
                                x = -1
                        else:
                            if ccc == len(cadena3):
                                contador = 1
                                x = cadena3
                        ccc = ccc + 1
        return x

    def list_to_string_reverse(self, lista):
        x = ''
        for i in reversed(lista):
            x = x + i
        return x

    def list_to_string(self, lista):
        x = ''
        for i in lista:
            x = x + i
        return x

    # Métodos para recorrer el AFD y evaluar la cadena
    def leer_entrada(self, ent_arreglo, ent_string):
        x = ''
        if ent_string == "":
            x = 'λ'
        return x 

    def push(self, pila, simbolo_insertar_pila, simbolo_a_devolver, contador):
        x = simbolo_insertar_pila
        z = simbolo_a_devolver

        if contador == 5:
            stringlength=len(simbolo_insertar_pila) # calculate length of the list
            slicedString=simbolo_insertar_pila[stringlength::-1] # slicing 
            for i in slicedString:
                pila.append(i)

        if contador == 0:
            pila.append(x)
        return z  

    def pop(self, pila, contador):
        xy = EVALUAR_CADENA (self.nombre)
        x = ''
        if contador == 0:
            x = 'λ'
        elif contador == 1:
            if pila:
                x = pila.pop()
        elif contador == 2:
            x = '#'
        return x

    def string_to_list(self, cadena, lista):
        for i in cadena:
            lista.append(i)

    def separar_transiciones_del_automata(self):
        xy = EVALUAR_CADENA (self.nombre)
        xyxy = GENERAR_AUTOMATA(self.nombre)
        can = ''
        can2 = ''
        y = ''
        for x in xyxy.diccionario_transiciones_automatas_pila[self.nombre]:
            if x!='*':
                y = y + x
            else:
                xy.transicion.append(y)
                y = ''

    def evaluarCadenaMetodo(self):
        xy = EVALUAR_CADENA (self.nombre)
        xxx = GRM_TIPO2(self.nombre)
        cadena1 = []
        cadena2 = []
        contador_producciones = 0

        contador2 = 0
        estado = ""
        estado1 = ""
        estado2 = ""
        recorrido_gramatica_a_imprimir = ""
        recorrido_gramatica = ""

        if xy.diccionario_cadena_a_evaluar:
            if self.nombre in xy.diccionario_cadena_a_evaluar: #Verificamos que la clave exista
                cad = xy.diccionario_cadena_a_evaluar[self.nombre]
            else:
                cad = ''
        else:
            cad = ''



        if len(cad)>=0:
            if xxx.diccionario_grmtipo2_producciones: #Verificamos que no esté vacio el diccionario
                if self.nombre in xxx.diccionario_grmtipo2_producciones: #Verificamos que la clave exista
                    #Pasamos de diccionario a lista para poderlo leer más fácil:
                    xy.transformar_dict_to_list_producciones()
                    
                    salir = False
                    dam = 0
                    #for x in xy.listaProducciones: #Vamos letra por letra de la entrada
                    for x in range(1,50):
                        if dam == 0: #Mientras no se haya aceptado o no aceptado
                            if xy.saberCadena(cad,xxx.diccionario_grmtipo2_terminales[self.nombre]) == 'S':
                            #if x in xxx.diccionario_grmtipo2_terminales[self.nombre]: # Si existe el caracter en el alfabeto
                                if dam == 0:

                                    if contador_producciones == len(xy.listaProducciones):
                                        contador_producciones = 0

                                    cadena1 = xy.listaProducciones[contador_producciones].split(">")
                                    estado1 = cadena1[0] # Estados
                                    estado2 = cadena1[1] # Producciones
                                    contador_letra_producciones = 0
                                    #if x == estado2[contador_letra_producciones]:
                                    if cad[0:1] == estado2[contador_letra_producciones]:
                                        recorrido_gramatica_a_imprimir = recorrido_gramatica_a_imprimir + xy.listaProducciones[contador_producciones]
                                        
                                        xy.pila_dibujar_arbol.append(xy.listaProducciones[contador_producciones])
                                        
                                        recorrido_gramatica = estado2
                                        print ("Recorrido gramática a imprimir: "+recorrido_gramatica_a_imprimir)
                                        print ("Recorrido gramática: "+estado2)
                                        #Desde acá es el problema
                                        
                                        """for y in recorrido_gramatica: #Recorre letra por letra la producción
                                            if y.isupper(): #Si es mayúscula
                                                print ("Encontró mayúscula en: "+y)
                                                recorrido_gramatica = recorrido_gramatica.replace(y,xy.buscarTrans(y, cad, xy.listaProduccionesAuxiliar)) #Reemplazar la mayúscula por el estado
                                                print ("El nuevo recorrido gramática es: "+recorrido_gramatica)"""
                                        
                                        #while any(c in string.ascii_uppercase for c in recorrido_gramatica):
                                        
                                        """for y in recorrido_gramatica: #Recorre letra por letra la producción
                                                if y.isupper(): #Si es mayúscula
                                                    if xy.buscarTrans(y, cad, xy.listaProducciones) != -1:
                                                        print ("Encontró mayúscula en: "+y)
                                                        recorrido_gramatica = recorrido_gramatica.replace(y,xy.buscarTrans(y, cad, xy.listaProducciones)) #Reemplazar la mayúscula por el estado
                                                        print ("El nuevo recorrido gramática es: "+recorrido_gramatica)
                                                    else:
                                                        print ("")
                                                        print ("*************************************************************************")
                                                        print ("                             CADENA INVÁLIDA                             ")
                                                        print ("*************************************************************************")
                                                        print ("")
                                                        salir = True
                                                        dam = 1"""

                                        for y in recorrido_gramatica: #Recorre letra por letra la producción
                                                if y.isupper(): #Si es mayúscula
                                                    print ("Encontró mayúscula en: "+y)
                                                    recorrido_gramatica = recorrido_gramatica.replace(y,xy.transArbolNormal(xy.buscarTrans(y, cad, xy.listaProducciones))) #Reemplazar la mayúscula por el estado
                                                    print ("El nuevo recorrido gramática es: "+recorrido_gramatica)
                                                    

                                        for y in recorrido_gramatica: #Recorre letra por letra la producción
                                                if y.isupper(): #Si es mayúscula
                                                    print ("Encontró mayúscula en: "+y)
                                                    recorrido_gramatica = recorrido_gramatica.replace(y,xy.transArbolNormal(xy.buscarTrans(y, cad, xy.listaProducciones))) #Reemplazar la mayúscula por el estado
                                                    print ("El nuevo recorrido gramática es: "+recorrido_gramatica)
                                                    

                                        for y in recorrido_gramatica: #Recorre letra por letra la producción
                                                if y.isupper(): #Si es mayúscula
                                                    print ("Encontró mayúscula en: "+y)
                                                    recorrido_gramatica = recorrido_gramatica.replace(y,xy.transArbolNormal(xy.buscarTrans(y, cad, xy.listaProducciones))) #Reemplazar la mayúscula por el estado
                                                    print ("El nuevo recorrido gramática es: "+recorrido_gramatica)
                                                    

                                        for y in recorrido_gramatica: #Recorre letra por letra la producción
                                                if y.isupper(): #Si es mayúscula
                                                    print ("Encontró mayúscula en: "+y)
                                                    recorrido_gramatica = recorrido_gramatica.replace(y,xy.transArbolNormal(xy.buscarTrans(y, cad, xy.listaProducciones))) #Reemplazar la mayúscula por el estado
                                                    print ("El nuevo recorrido gramática es: "+recorrido_gramatica)
                                                    

                                        for y in recorrido_gramatica: #Recorre letra por letra la producción
                                                if y.isupper(): #Si es mayúscula
                                                    print ("Encontró mayúscula en: "+y)
                                                    recorrido_gramatica = recorrido_gramatica.replace(y,xy.transArbolNormal(xy.buscarTrans(y, cad, xy.listaProducciones))) #Reemplazar la mayúscula por el estado
                                                    print ("El nuevo recorrido gramática es: "+recorrido_gramatica)
                                                    


                                        #recorrido_gramatica = xy.buscarTransRecursivo(recorrido_gramatica, cad, xy.listaProduccionesAuxiliar)
                                            
                                        if recorrido_gramatica == cad:
                                            print ("")
                                            print ("*************************************************************************")
                                            print ("                             CADENA ACEPTADA                             ")
                                            print ("*************************************************************************")
                                            print ("")
                                            salir = True
                                            dam = 1

                                            xy.generarArbolNormal()
                                            #xy.draw2()


                                        else:
                                            print ("")
                                            print ("*************************************************************************")
                                            print ("                             CADENA INVÁLIDA                             ")
                                            print ("*************************************************************************")
                                            print ("")
                                            salir = True
                                            dam = 1
                                        

                                        contador_letra_producciones = contador_letra_producciones + 1
                                    
                                    else:
                                        print ("")
                                        print ("*************************************************************************")
                                        print ("                             CADENA INVÁLIDA                             ")
                                        print ("*************************************************************************")
                                        print ("")
                                        salir = True
                                        dam = 1
                                    contador_producciones = contador_producciones + 1
                            else:
                                print ("Cadena inválida, ya que un caracter de la entrada no pertenece al alfabeto del lenguaje")
                                salir = True












                    """for x in cad: #Comenzamos a recorrer la entrada
                        if contador >=0:
                            if x in xxx.diccionario_grmtipo2_terminales[self.nombre]:
                                cadena1 = xy.listaProducciones[contador].split(">")
                                estado1 = cadena1[0] # Estados
                                estado2 = cadena1[1] # Producciones
                                #Hasta acá vamos bien
                                if x == estado2[contador]:
                                    print ("Encontró caracter igual en: ")
                                    print (contador)
                                    recorrido_gramatica_a_imprimir = recorrido_gramatica_a_imprimir + xy.listaProducciones[contador]
                                    recorrido_gramatica = estado2
                                    for x in recorrido_gramatica:
                                        if x.isupper():
                                            print ("Encontró mayúscula en: "+x)
                                            if x in estado1:
                                                recorrido_gramatica = recorrido_gramatica.replace(x,estado2)
                                                print ("El nuevo recorrido gramática es: "+recorrido_gramatica)
                                        else:
                                            if recorrido_gramatica == cad:
                                                print ("Cadena aceptada")
                                                print (recorrido_gramatica_a_imprimir)
                                                print (recorrido_gramatica)
                                                contador = -1
                                            else:
                                                contador = contador + 1
                                else:
                                    contador = contador + 1
                            else:
                                print ("Cadena inválida, ya que un caracter de la entrada no pertenece al alfabeto del lenguaje") 
                                contador = -2
                        elif contador == -1:
                            print ("Cadena Aceptada")
                        elif contador == -2:
                            print ("Cadena No Válida")"""
                else:
                    print ("No existe transiciones del autómata")
            else:
                print ("No existe transiciones del autómata")

        xy.salir_menu()


    def saberCadena(self, cad, lista):
        y = 'S'
        for x in cad:
            if not x in lista:
                y = 'N'
        return y

    def transArbolNormal(self, cad):
        xy = EVALUAR_CADENA (self.nombre)
        xy.trans_arbol_normal.append(cad)
        return cad

    def generarArbolNormal(self):
        xy = EVALUAR_CADENA (self.nombre)
        xxx = GRM_TIPO2(self.nombre)
        print(xy.pila_dibujar_arbol)

        estado1 = []
        cadena1 = ''
        cadena2 = ''

        arreglo_mandar = []
        arreglo_completo = []

        contador = 0
        inicio = ''
        for x in xy.pila_dibujar_arbol:
                estado1 = x.split(">")
                cadena1 = estado1[0]
                cadena2 = estado1[1]
                if contador ==0:
                    inicio = cadena1
                contador = 1
                arreglo_completo.append(cadena2)
                for y in cadena2:
                    """if cadena1+y in arreglo_mandar:
                        y = y+"."""
                    """elif cadena1+y+"." in arreglo_mandar:
                        y = y+".."
                    elif cadena1+y+".." in arreglo_mandar:
                        y = y+","
                    elif cadena1+y+"," in arreglo_mandar:
                        y = y+";"""

                    arreglo_mandar.append(cadena1+y)

        print (arreglo_mandar)
        xy.draw2(arreglo_mandar, inicio, arreglo_completo)

        #xy.draw(inicial,primeros_punteros, otros_punteros)

    def draw(self, arreglo, inicio, arreglo_completo):
        #print("inicio:", str(inicio))
        g = gv.Digraph(format='png')
        g.graph_attr['rankdir'] = 'TB'
        g.node('ini', shape="point")

        with g.subgraph() as s:
            s.attr(rank='same')
            s.node(inicio)
        
        #g.node('C')
        """for y in range(1,2):
            with g.subgraph() as s:
                s.attr(rank='same')
                for x in arreglo_completo[y][0]:
                    s.node(x)"""

        #with g.subgraph() as s:
            #s.attr(rank=same)
            #for x in arreglo_completo[0]:
            #s.node('z')
            #s.node('M')
            #s.node('N')
            #s.node('z')

        """with g.subgraph() as s:
            s.attr(rank='same')
            for x in arreglo_completo:
                s.node(x)"""

        #for e in estados:
        #        g.node(e)
        #for t in trans:
            #if t[2] not in alfabeto:
            #    return 0
            #g.edge(t[0], t[1], label=str(t[2]))
        #g.edges(['AB', 'AC', 'CD'])
        g.edges(arreglo)
        #g.render(view=True)
        g.render("arbol"+self.nombre+'.gv', view=True)

    def draw2 (self,arreglo, inicio, arreglo_completo):
        xy = EVALUAR_CADENA (self.nombre)
        arreglo_mandar = []
        graph = pydot.Dot(graph_type='graph')
        for i in arreglo_completo[0]:

            if inicio+i in arreglo_mandar:
                i = i + "."
            arreglo_mandar.append(inicio+i)
            edge = pydot.Edge(inicio, i)
            graph.add_edge(edge)




        #abc = len(arreglo_completo[0])
        #for w in range(0,xy.saberCantLista(arreglo_completo)):
        #for t in range(1,xy.saberNumMayus(arreglo_completo[0])):
        #Para M
        for i in arreglo_completo[1]:
                    for j in arreglo_completo[0]:
                        if j.isupper() and j in arreglo_completo[1]:
                            #if inicio + j in arreglo_mandar:
                            #    i = i+".."
                            if j == i:
                                i = i +".."
                            elif j+i in arreglo_mandar:
                                i = i +".."
                            elif j + i +".." in arreglo_mandar:
                                i = i+";"
                            elif j+i+";" in arreglo_mandar:
                                i = i+","
                            elif j+i+"," in arreglo_mandar:
                                i = i+"*"
                            arreglo_mandar.append(j+i)
                            edge = pydot.Edge(j, i)
                            i = ''
                            j = ''
                            graph.add_edge(edge)

        #Para N
        for i in arreglo_completo[2]:
                    for j in arreglo_completo[0]:
                        if j.isupper() and j in arreglo_completo[2]:
                            #if inicio + j in arreglo_mandar:
                            #    i = i+".."
                            if j == i:
                                i = i +".."
                            elif j+i in arreglo_mandar:
                                i = i +".."
                            elif j + i +".." in arreglo_mandar:
                                i = i+";"
                            elif j+i+";" in arreglo_mandar:
                                i = i+","
                            elif j+i+"," in arreglo_mandar:
                                i = i+"*"
                            arreglo_mandar.append(j+i)
                            edge = pydot.Edge(j, i)
                            i = ''
                            j = ''
                            graph.add_edge(edge)




        """for i in arreglo_completo[2]:
            for j in arreglo_completo[0]:
                if j.isupper() and j in arreglo_completo[2]:
                    if inicio + j in arreglo_mandar:
                        i = i+".."
                    elif j+i in arreglo_mandar:
                        i = i+".."
                    elif j+i+"." in arreglo_mandar:
                        i = i+","
                    elif j+i+".." in arreglo_mandar:
                        i = i+";"
                    elif j+i+"," in arreglo_mandar:
                        i = i+"*"
                    arreglo_mandar.append(j+i)
                    edge = pydot.Edge(j, i)
                    graph.add_edge(edge)"""




        """# now let us add some vassals
        vassal_num = 0
        for i in range(3):
            for j in range(2):
                edge = pydot.Edge("lord%d" % i, "vassal%d" % vassal_num)
                graph.add_edge(edge)
                vassal_num += 1"""

        # ok, we are set, let's save our graph into a file
        graph.write_png('example1_graph.png')


        


    def saberNumMayus(self, cad):
        y = 0
        for x in cad:
            if x.isupper():
                y = y +1
        return y

    def saberCantLista(self, cad):
        y = 0
        for x in cad:
                y = y +1
        return y


    def buscarTransRecursivo(self, recorrido_gramatica, cad, producciones):
        xy = EVALUAR_CADENA (self.nombre)
        recorrido = recorrido_gramatica
        for y in recorrido: #Recorre letra por letra la producción
            if y.isupper(): #Si es mayúscula
                print ("Encontró mayúscula en: "+y)
                recorrido = recorrido.replace(y,xy.buscarTrans(y, cad, producciones)) #Reemplazar la mayúscula por el estado
                print ("El nuevo recorrido gramática es: "+recorrido)
            else:
                xy.buscarTransRecursivo(recorrido, cad, producciones)
        return recorrido




    def buscarTrans(self, estado, cadena, producciones):
        xy = EVALUAR_CADENA (self.nombre)
        cad1 = []
        cad2 = []
        est = []
        contador = 0
        xyz = ''
        a_retornar = ''
        ccc = 0
        contador_estado = 0


        print("Estado: "+estado)
        print("Cadena: " +cadena)
        print(producciones)

        for y in producciones: # Recorre una producción a la vez, producción por producción
            #y.replace("*","")
            if contador == 0: #Mientras no haya encontrado la producción buscada a la letra mayúscula (ESTADO)
                est = y.split(">") # Partimos la producción actual
                cad1 = est[0] #estados
                cad2 = est[1] #producciones
                xyz = cad2 # guardamos producciones para disminuir
                if estado == cad1: #Si existe el estado en la lista de estados
                    for z1 in cad2: #Las veces repetidas serán igual al número de producciones -- Se repiten 4 veces
                        for z3 in xyz:
                            if z3.isupper(): #Si la letra es Mayúscula
                                xyz.replace(z3,"") #Eliminamos la letra
                        for z2 in xyz: #Las veces repetidas serán igual al número de producciones (Sin mayúsculas) -- Se repiten 2 veces
                            if contador == 0:
                                if z2 in cadena: 
                                    ccc = ccc + 1
                                    if ccc == len(xyz):
                                        contador = 1
                                        ccc = 0
                                        a_retornar = cad2
                                        xy.pila_dibujar_arbol.append(y)
                                        for i in range(len(producciones)-1, -1, -1):
                                            if producciones[i] == y:
                                                del producciones[i]
                                        #a_retornar = cad2
            if len(a_retornar)==0:
                a_retornar = "-1"
        return a_retornar




    #*******************************************    Métodos generales ********************************

    def concatenar_letras_comas(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        can = "{"+can+"}"
        return can

    def concatenar_letras_comas_sin_llaves(self, estado):
        can = ''
        for x in estado:
            can = can + x +","
        if can[len(can)-1] == ",":
            can = can[:len(can) - 1]
        return can

    def transformar_dict_to_list_producciones(self):
        xy = EVALUAR_CADENA (self.nombre)
        xxx = GRM_TIPO2(self.nombre)
        xy.listaProducciones.clear()
        y = ''
        if self.nombre in xxx.diccionario_grmtipo2_producciones:
            for x in xxx.diccionario_grmtipo2_producciones[self.nombre]:
                if x!='*':
                    y = y + x
                else:
                    xy.listaProducciones.append(y)
                    y = ''
        else:
            xy.listaProducciones.clear()

    def salir_menu(self):
        xy = EVALUAR_CADENA(self.nombre)
        salir = False
        opcion = 0
        
        print ("")
        print ("Ingrese << 0 >> para regresar al menú anterior")
        
        while not salir:
            opcion = pedirNumeroEntero()
            if opcion == 0:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                xy.menu_evaluar_cadena() #Ingresar NT
            else:
                print ("Introduce 0 para regresar al menú anterior")


def menu_general_grm_tipo2():
        salir = False
        opcion = 0

        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ GENERAL GRAMÁTICAS TIPO 2 #########################")
        print ("") 
        print ("    1. Ingresar / modificar gramática")
        print ("    2. Generar autómata de pila")
        print ("    3. Visualizar autómata")
        print ("    4. Validar cadena")
        print ("    5. Regresar a la carátula")
            
        while not salir:

            opcion = pedirNumeroEntero()

            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                cad = pedir_nombre_grm_tipo2()
                if cad != 'salir':
                    os.system(var)
                    xy = GRM_TIPO2(cad)
                    xy.inicio()
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                cad = pedir_nombre_grm_tipo2_generar_automata()
                if cad != 'salir':
                    os.system(var)
                    xy = GENERAR_AUTOMATA(cad)
                    xy.inicio()
            elif opcion == 3:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                cad = pedir_nombre_grm_tipo2_visualizar_automata()
                if cad != 'salir':
                    os.system(var)
                    xy = VISUALIZAR_AUTOMATA(cad)
                    xy.inicio()
            elif opcion == 4:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                cad = pedir_nombre_grm_tipo2_evaluar_cadena()
                if cad != 'salir':
                    os.system(var)
                    xy = EVALUAR_CADENA(cad)
                    xy.evaluarCadena()
            elif opcion == 5:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                MenuPrincipal.inicio()
            else:
                print ("Introduce un numero entre 1 y 5")

#
# **********************************  PANTALLA INICIAL ****************************** NÍTIDA
#
class PantallaInicial:
    def inicio():
        os.system(var) #Limpiamos o cambiamos pantalla
        print ("#######################  PROYECTO 2  #########################")
        print ("") 
        print ("    Curso: Lenguajes Formales y de Programación")
        print ("    Sección: B-")
        print ("    Carnet: 201603171")
        print ("")  
         
        # Función para detectar enter
        while True:
            i = input("Presiona enter para ingresar al menú de opciones:")
            if not i:
                break
            print("Tu ingresaste: ", i)
            
        os.system(var) #Limpiamos o cambiamos pantalla
        MenuPrincipal.inicio()

#
# **********************************  MENÚ PRINCIPAL ******************************
#
class MenuPrincipal:
    def inicio():
        
        salir = False
        opcion = 0

        print ("#######################  PROYECTO 2  #########################")
        print ("####################### MENÚ PRINCIPAL #########################")
        print ("") 
        print ("    1. Crear AFD")
        print ("    2. Crear gramática")
        print ("    3. Evaluar cadenas")
        print ("    4. Reportes")
        print ("    5. Cargar archivo de entrada")
        print ("    6. Guardar")
        print ("    7. Gramáticas Tipo 2 y AP")
        print ("    8. Salir")
            
        while not salir:

            opcion = pedirNumeroEntero()
         
            if opcion == 1:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                cad = pedir_nombre_afd()
                if cad != 'salir':
                    os.system(var)
                    xy = AFD(cad)
                    xy.inicio()
            elif opcion == 2:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                cad = pedir_nombre_grm()
                if cad != 'salir':
                    os.system(var)
                    xy = GRM(cad)
                    xy.inicio()
            elif opcion == 3:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                cad = pedir_nombre_grm_ecad()
                if cad != 'salir':
                    os.system(var)
                    xy = ECAD(cad) #Nos vamos al menú evaluar cadenas
                    xy.inicio()
                """c = canvas.Canvas("hola_mundo.pdf")
                c.drawString(100,750,"Hola mundo pdf!")
                c.save()"""
            elif opcion == 4:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                pedir_nombre_reporte()
            elif opcion == 5:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                pedir_nombre_cargar_archivo()
            elif opcion == 6:
                #salir = True
                #os.system(var) #Limpiamos o cambiamos pantalla
                #os.system("menu_guardar.py") #Ejecutamos el otro archivo y Ejecutamos Menú Principal
                print ("guardar.....")
            elif opcion == 7:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
                menu_general_grm_tipo2()
            elif opcion == 8:
                salir = True
                os.system(var) #Limpiamos o cambiamos pantalla
            else:
                print ("Introduce un numero entre 1 y 8")

PantallaInicial.inicio()