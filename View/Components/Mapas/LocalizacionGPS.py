from PySide6.QtWidgets import(QWidget,QVBoxLayout, QHBoxLayout, QLabel)
from PySide6.QtCore import(QUrl,Slot)
from Tools.GPS import GPS
from PySide6.QtQuickWidgets import QQuickWidget
from Tools.Paths import rutaAbsoluta

class LocalizacionGPS(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(900,600) # tamanio minimo del gps
        # Layout principal
        main_layout = QVBoxLayout(self)

        # Vista del mapa
        self.mapa = QQuickWidget()
        self.mapa.setResizeMode(QQuickWidget.SizeRootObjectToView)
        main_layout.addWidget(self.mapa)

        # Adjuntamos la clase de gps
        self.gps = GPS()
        self.mapa.rootContext().setContextProperty("gps", self.gps)

        # Le damos el mapa al contexto de la vista rapida
        rutaMapa = rutaAbsoluta("View/Components/Mapas/Mapa.qml")
        qml_url = QUrl.fromLocalFile(rutaMapa)
        self.mapa.setSource(qml_url)

    def cambiarCordenadas(self, lon, lat):
        self.gps.actualizarCordenadas(lon, lat)

    