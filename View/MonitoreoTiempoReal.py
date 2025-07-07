from PySide6.QtWidgets import ( QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton, 
                               QComboBox, QLineEdit)
from View.Components.Visual3D import Visual3D
from View.Components.GraficaGenerica import GraficaGenerica

#clase para la ventana de monitoreo en timpo real
class VentanaMTR(QWidget):
    def __init__(self, controlador, rutaStl):
        super().__init__() # se manda a llamar el constructor la clase Qwidget 
        #ajustes de la ventana
        ContenidoPrincipal = QHBoxLayout() # contenedor horizontal que lleva todo el contenido
        ladoIzq = QVBoxLayout() # contenedor vertical para el modelos 3d 
        ladoDer = QVBoxLayout() # contenedor en tabla para las graficas que se van a colocar

        self.ruta = rutaStl


        # controlador de la ventana
        self.controlador = controlador # se recive la intancia del controlador
        self.controlador.vista = self # se le pasa la referencia de esta misma ventana

        #----------------------------------componentes lado IZQ------------------------------------
        etVisual = QLabel("Monitoreo 3D")
        etVisual.setObjectName("seccion")
        self.visual = Visual3D(self.ruta) # modelo 3D
        ladoIzq.addWidget(etVisual) # se agrega la etiqueta de seccion
        ladoIzq.addWidget(self.visual) # se agrego al lado derecho


        #----------------------------------componentes lado DER------------------------------------
        # Primer grid: encabezado, campos y controles de puerto
        gridControles = QGridLayout()
        etGraficas = QLabel("Monitoreo de datos")
        etGraficas.setObjectName("seccion")
        gridControles.addWidget(etGraficas, 0, 0, 1, 5)

        # espacio para darle nombre al lanzamiento
        etMision = QLabel("Mision:")
        etMision.setObjectName("etiquetaControl")
        self.nameMision = QLineEdit()
        gridControles.addWidget(etMision, 1, 0)
        self.nameMision.setPlaceholderText("Nombre de lanzamiento...")
        self.nameMision.setObjectName("campoText")
        gridControles.addWidget(self.nameMision, 1, 1, 1, 4)  # 1 fila, 3 columnas

        # desplegable puesto serial
        etPuertoSerial = QLabel("Puerto serial:")
        etPuertoSerial.setObjectName("etiquetaControl")
        gridControles.addWidget(etPuertoSerial, 2, 0)
        self.puertosSerial = QComboBox()
        self.puertosSerial.setObjectName("desplegable")
        gridControles.addWidget(self.puertosSerial, 2, 1)
        
        # seleccionador de velocidad
        etVelocidad = QLabel("Velocidad:")
        etVelocidad.setObjectName("etiquetaControl")
        gridControles.addWidget(etVelocidad, 2, 2)
        self.velocidad = QComboBox()
        self.velocidad.setObjectName("desplegable")
        self.velocidad.addItems(["1200","2400","4800","9600","19200","38400","57600","115200"])
        gridControles.addWidget(self.velocidad, 2, 3)

        # boton para actualizar los puertos
        self.actualizarBut = QPushButton("Actualizar")
        self.actualizarBut.setObjectName("boton")
        gridControles.addWidget(self.actualizarBut, 2, 4)

        # Segundo grid: gráficas
        gridGrafica = QGridLayout()
        self.temperatura = GraficaGenerica("Temperatura", "Tiempo (s)","Temperatura (°C)", "°C", "#FF5733")
        self.humedad = GraficaGenerica("Humedad", "Tiempo (s)", "Humedad (%)", "%", "#33A7FF")
        self.presion = GraficaGenerica("Presión", "Tiempo (s)", "Presión (Pa)", "Pa", "#33FF57")
        self.altura = GraficaGenerica("Altura", "Tiempo (s)", "Altura (m)", "m", "#FFFF33")
        self.co2 = GraficaGenerica("CO₂", "Tiempo (s)", "Concentración (ppm)", "ppm", "#FFFFFF")
        self.uv = GraficaGenerica("Radiación UV", "Tiempo (s)", "Índice UV", "UV", "#33FFFF")

        # Agregarlas en 2 filas y 3 columnas
        gridGrafica.addWidget(self.temperatura, 0, 0)
        gridGrafica.addWidget(self.humedad,     0, 1)
        gridGrafica.addWidget(self.presion,     0, 2)
        gridGrafica.addWidget(self.altura,      1, 0)
        gridGrafica.addWidget(self.co2,         1, 1)
        gridGrafica.addWidget(self.uv,          1, 2)

        # Layout para botones
        botonesLayout = QHBoxLayout()
        self.iniciarBut = QPushButton("Iniciar")
        self.iniciarBut.setObjectName("boton")

        self.detenerBut = QPushButton("Detener")
        self.detenerBut.setObjectName("boton")

        botonesLayout.addStretch()
        botonesLayout.addWidget(self.iniciarBut)
        botonesLayout.addWidget(self.detenerBut)

        # Agregar los grids al lado derecho (vertical)
        ladoDer.addLayout(gridControles)
        ladoDer.addLayout(gridGrafica)
        ladoDer.addLayout(botonesLayout)

        #agregar las disposiciones a la ventana principal del objeto
        ContenidoPrincipal.addLayout(ladoIzq) # agregar el lado izq 
        ContenidoPrincipal.addLayout(ladoDer) # agregar el lado der (ahora vertical con grids)
        ContenidoPrincipal.setStretch(0, 2)  # ladoIzq (30%)
        ContenidoPrincipal.setStretch(1, 8)  # ladoDer (70%)
        self.setLayout(ContenidoPrincipal) # definir lo que tiene el componente principal

