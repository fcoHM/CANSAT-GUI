import PySide6 # para la parte visual
import vtk # modelos 3D
import pandas # para manipular datos o exportarlos 
import serial # para la recepcion de datos 

# aqui debe de ir la logica de el main que solo debe crear un objeto tipo book y pues dar inicio a la GUI
from PySide6.QtWidgets import QApplication
from View.MonitoreoTiempoReal import VentanaMTR

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = VentanaMTR()
    ventana.show()
    sys.exit(app.exec())
# ...existing code...