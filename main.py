import sys
import os
import random
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from View.MonitoreoTiempoReal import MonitoreoTiempoReal
from Tools.Paths import rutaAbsoluta
from PySide6.QtGui import QIcon
from Controllers.CMonitoreoTiempoReal import CMonitoreoTiempoReal

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Obtener la ruta del script
    ruta_qss = rutaAbsoluta("View/Styles/Style.qss")


    icono_path = rutaAbsoluta("Media/icono.ico")

    # Aplicar estilo
    if os.path.exists(ruta_qss):
        with open(ruta_qss, "r") as f:
            app.setStyleSheet(f.read())

    # Crear ventana y controlador
    controlador = CMonitoreoTiempoReal()
    ventana = MonitoreoTiempoReal(controlador)
    ventana.setWindowIcon(QIcon(icono_path))
    ventana.setWindowTitle("CANSAT - Monitoreo Tiempo Real")
    ventana.showMaximized()

    

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
