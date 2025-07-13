import os
import sys

#cracion de ruta absoluta 
def rutaAbsoluta(relativa): #recive ruta relativa
    if getattr(sys, 'frozen', False): #si esta empaquetada
        base = sys._MEIPASS
    else:
        # Se retrocede un nivel para que la ruta base sea la raíz del proyecto.
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # si es codigo
    return os.path.join(base, relativa)