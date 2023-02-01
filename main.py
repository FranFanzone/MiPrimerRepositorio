from funciones import *
import json
continuar=True
while continuar:
  opcion=input('Seleccione una opcion...\n\t"1" Registrarse.\n\t"2" Iniciar sesion.\n\t"3" Ver base de datos.\n\t"4" Salir del programa.\n\t')
  if opcion=='1':
     menu=opcion1()
  if opcion=='2': 
     menu=opcion2()
  if opcion=='3':
     menu=opcion3()
  if opcion=='4':
     continuar=False