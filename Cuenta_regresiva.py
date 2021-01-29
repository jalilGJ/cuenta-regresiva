# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:30:39 2020

@author: jalil gacrcia jeronimo
"""
print ("introdusca un numero para la cuenta regresiva")#se solicita un dato desde el teclado
numero=int(input())#se almacena el dato introducido desde el teclado
def cuenta_regresiva(numero):#Funcion recursiva
     numero -= 1#condicion o caso base
     if numero > 0:#condicion o caso base
         print (numero)
         cuenta_regresiva(numero)#se llama la funcion asi mismo,creando un buclea hasta llegar a igualar la condicion o funcion
     else:
         print ("Boooooooom!")
print (cuenta_regresiva(numero))