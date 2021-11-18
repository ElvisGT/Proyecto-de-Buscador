from funcion_buscar import Buscar
import os



####Mostrar Datos####
suma = 0
if os.path.exists("F:\\"):
    listado_objetos = Buscar("F")
    suma+=1
    for i in listado_objetos:
        i.Mostrar()
        print("="*100)

if os.path.exists("G:\\"):
    listado_objetos = Buscar("G")
    suma+=1
    for i in listado_objetos:
        i.Mostrar()
        print("="*100)

if os.path.exists("H:\\"):
    listado_objetos = Buscar("H")
    suma+=1
    for i in listado_objetos:
        i.Mostrar()
        print("="*100)

if os.path.exists("I:\\"):
    listado_objetos = Buscar("I")
    suma+=1
    for i in listado_objetos:
        i.Mostrar() 
        print("="*100)    

  
if suma == 0:
    print("No ha insertado ninguna unidad")

input("Presione Enter para finalizar")