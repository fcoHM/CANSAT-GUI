
from PySide6.QtCore import (QObject, Signal)

class GPS(QObject):
    coordenadas_actualizadas = Signal(float, float)
    signalZoom = Signal(int) # senial para hacer o queitar zoom

    def __init__(self):
        super().__init__()
        # se le da una posicion inicial al mapa
        self.lat = 22.78366121149007
        self.lon = -102.57292226517136

        # zoom inicial
        self.zoom = 14
        # se emite la senial
        self.coordenadas_actualizadas.emit(self.lat, self.lon)
        self.signalZoom.emit(self.zoom)
    
    def actualizarCordenadas(self, lat, lon):
        # se cambia la posicion a la llegada del GPS 
        self.lon = lon
        self.lat = lat
        # se emite la senial
        self.coordenadas_actualizadas.emit(lat, lon)

    def masZoom(self): # hacer zoom al mapa
        if self.zoom < 22: # ver que el ql zoom este bajo el rango maximo
            self.zoom +=2
            self.signalZoom.emit(self.zoom) # emitir la senial

    def menosZoom(self): # quitar zoom del mapa  
        if self.zoom > 6: # ver que el zoom este por encima del rango minimo
            self.zoom -=2
            self.signalZoom.emit(self.zoom) # emitir la senial

