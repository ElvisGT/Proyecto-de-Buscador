import os,re

class Carpeta:
    ruta_encontrada = None
    
    def setRuta_encontrada(self,ruta_encontrada):
        self.ruta_encontrada = ruta_encontrada
    
    
    def getRuta_encontrada(self):
            return self.ruta_encontrada
    
    def Mostrar(self):
            print(f"Ruta:{self.getRuta_encontrada()}")

    