from PySide6.QtWidgets import ( QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton)

#clase para la ventana de monitoreo en timpo real
class VentanaMTR(QWidget):
    def __init__(self):
        super().__init__() # se manda a llamar el constructor la clase Qwidget 
        #ajustes de la ventana
        ContenidoPrincipal = QHBoxLayout() # contenedor horizontal que lleva todo el contenido
        ladoIzq = QVBoxLayout() # contenedor vertical para el modelos 3d 
        ladoDer = QGridLayout() # contenedor en tabla para las graficas que se van a colocar

        #componentes que debe tener la ventana 



        
        #agregar las disposiciones a la ventana principal del objeto
        ContenidoPrincipal.addLayout(ladoIzq) # agregar el lado izq 
        ContenidoPrincipal.addLayout(ladoDer) # agregar el lad der
        self.setLayout(ContenidoPrincipal) # definir lo que tiene el componente principal

    