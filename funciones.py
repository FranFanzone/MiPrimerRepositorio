from Registro import registro as reg
from Loggin import loggin as logg
import json

def opcion1():
    datos={}
    registro=reg(datos)
    datos.update(registro)
    with open("C:/Users/franc/OneDrive/Escritorio/Python/Registro-Loggin/BD.txt",'a') as BD:
        json.dump(datos, BD, indent=4)

def opcion2():
    datoslogg={}
    datosloggin=logg(datoslogg)
    datoslogg.update(datosloggin)
    with open("C:/Users/franc/OneDrive/Escritorio/Python/Registro-Loggin/BD.txt",) as LeerBase:
        leerdatos= json.load(LeerBase)
        for nombre in datoslogg.items():
            if nombre in leerdatos.items():
               print('Accediste.')
            else:
               print('Usuario no encontrado.')
def opcion3():
    with open("C:/Users/franc/OneDrive/Escritorio/Python/Registro-Loggin/BD.txt",'r') as LeerBase:
        leerdatos= json.load(LeerBase)
        print(leerdatos)
