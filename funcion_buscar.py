import re,os
from proyecto_paquete_clases import Carpeta

def Buscar(letra):
    paqueteRegex = re.compile(r"(\d\d\d\d-\d\d-\d\d)+")
    lista_obj = []
    
    ruta_lista_archivos = os.listdir(letra + ":\\")
    lista_archivos = paqueteRegex.search(str(ruta_lista_archivos))
        

    #Existe la carpeta del paquete?
    if lista_archivos:  
        print(f"Fecha del paquete:{str(lista_archivos.group(0))}")
        nombre = input("Teclee el nombre de la carpeta a buscar: ")
        nombre = nombre.strip()
        buscar_nombre = None
        listado =[]
        
        
    
        print("Buscando...")
        print("="*100)
        for folder,subfolder,files in os.walk(os.path.join(letra + ":\\" ,str(lista_archivos[0])),topdown=False):
            buscar_nombre = re.search(rf"(?<![\w\d])({nombre})(?![\w\d])",folder,re.I)
            if buscar_nombre:
                for i in os.listdir(folder):
                    listado.append(os.path.join(folder + "\\" ,i))
                    

            else:
                for file in files:
                    buscar_nombre = re.search(rf"(?<![\w\d])({nombre})(?![\w\d])",file,re.I)
                    if buscar_nombre:
                        listado.append(folder + "\\" + file)
                        
                     

        if listado: #Existe ?
            
            for i in listado:
                obj = Carpeta()
                obj.setRuta_encontrada(i)
                lista_obj.append(obj)
        
        else:
            print("No existe la carpeta de 3DJuegos")
    else:
        print("No existe la carpeta del paquete")

    return lista_obj