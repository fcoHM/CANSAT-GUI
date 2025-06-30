from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
import sys
from View.Components.GraficaGenerica import GraficaGenerica
import random

def main():
    app = QApplication(sys.argv)
    
    # Create an instance of the GraficaGenerica class
    grafica = GraficaGenerica("Demo Graph", "Time (s)", "Value", "red")
    grafica.show()

    datos_restantes = 20

    def agregar_dato():
        nonlocal datos_restantes
        
        dato = random.uniform(0, 100)  # Generate a random value between 0 and 100
        grafica.agregarDato(dato)
        datos_restantes -= 1
       
        

    timer = QTimer()
    timer.timeout.connect(agregar_dato)
    timer.start(1000)  # 1000 ms = 1 segundo

    sys.exit(app.exec())

if __name__ == "__main__":
    main()