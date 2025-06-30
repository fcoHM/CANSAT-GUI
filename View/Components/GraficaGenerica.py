from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel) 

from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraficaGenerica(QWidget):
    def __init__(self, nombreGrafica, nomX, nomY, color): #constructor del componente garfico
        super().__init__()
        self.resize(500, 300)  # Tamaño inicial de la ventana QT

        # Contedores para datos y tiempo
        self.tiemposT = []      # Eje X: tiempo en segundos temporales
        self.datosT = []      # Eje Y: datos mandados del CanSat temporales
        self.tiempos = []      # Eje X: tiempo en segundos persistentes
        self.datos = []      # Eje Y: datos mandados del CanSat persistentes

        self.segundos = 0      # Contador que simula el paso del tiempo
        self.grafica = nombreGrafica  # nombre de la grafica
        self.ejeX = nomX # nombre del eje x
        self.ejeY = nomY # nombre del eje y 
        self.color = color # nombre de a linea trasadora 

        #acomodo de la ventana
        layout = QVBoxLayout() # disposicion vertical

        # grafica  con matplotlib y canvas paea renderizarla
        self.figura = Figure(figsize=(6,4))
        self.canvas = FigureCanvas(self.figura)
        self.ax = self.figura.add_subplot(111)  # eje de la figura

        # Estilo inicial del gráfico
        self.ax.set_title(self.grafica, fontsize=10, color="white")
        self.ax.set_xlabel(self.ejeX, fontsize=8, color="white")
        self.ax.set_ylabel(self.ejeY, fontsize=8, color="white")
        self.ax.tick_params(axis="x", labelsize=7, rotation=45, color="white", labelcolor="white")
        self.ax.tick_params(axis="y", labelsize=7, color="white", labelcolor="white")
        self.ax.grid(True, linestyle="--", alpha=0.5, color="white") # cuadriculado de la grafica 
        self.ax.set_facecolor("#141924")  # Fondo del área de la gráfica
        self.figura.patch.set_facecolor("#141924")  # Fondo exterior del canvas

        # Agregar canvas de la gráfica al layout
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        # Etiqueta informativa para mostrar el último dato recibido
        self.info = QLabel("⏳ Iniciando monitoreo...")
        layout.addWidget(self.info)

        #self.timer = QTimer()
        # self.timer.timeout.connect(self.simular_dato)  ## aqui posiblemnete vamos a usar el metodo de actualizar la grafica ya que el valor lo vamos a recibir  por otro lado 
        # self.timer.start(1000)  # 1000 ms = 1 segundo

# metodos funcionales de la clase

    # metodo para agregar un dato a la garfica
    def agregarDato(self, dato):
        self.segundos  += 1 # se incrementa el segundo para ir teniendo una relacion valor/tiempo

        # agregar los datos a las listas
        self.tiemposT.append(self.segundos) # se agrega el nuevo segundo temporal
        self.datosT.append(dato) # se agrega el nuevo dato temporal
        self.tiempos.append(self.segundos) # se agrega el nuevo segundo 
        self.datos.append(dato) # se agrega el nuevo dato

        # validar la cantidad de datos persistentes en  la grafica 
        if len(self.tiemposT) > 15:
            self.tiemposT.pop(0)
            self.datosT.pop(0)
    
        self.actualizarGrafica() # corregido el nombre del método
        self.info.setText(f"📡 Último dato: {dato:.2f}")

    # metodo para actualizar la grafica
    def actualizarGrafica(self):
        self.ax.clear() # limpia la grafica
        self.ax.plot(self.tiemposT, self.datosT, color=self.color, linewidth=2) # grafica los datos temporales

        # Mostrar los valores numéricos sobre cada punto
        for x, y in zip(self.tiemposT, self.datosT):
            self.ax.text(x, y, f"{y:.2f}", fontsize=7, color="white", ha="center", va="bottom")

        # diseño del repintado
        self.ax.set_title(self.grafica, fontsize=10, color ="white")
        self.ax.set_xlabel(self.ejeX, fontsize=8, color ="white")
        self.ax.set_ylabel(self.ejeY, fontsize=8, color ="white")
        self.ax.tick_params(axis="x", labelsize=7, rotation=45, color="white", labelcolor="white")
        self.ax.tick_params(axis="y", labelsize=7, color="white", labelcolor="white")
        self.ax.grid(True, linestyle="--", alpha=0.5, color ="white") # cuadriculado de la grafica 
        self.ax.set_facecolor("#141924")  # Fondo del área de la gráfica
        self.figura.patch.set_facecolor("#141924")  # Fondo exterior del canvas
        self.figura.tight_layout()
        self.canvas.draw() # actualiza/repintado de la interface 



# metodos get y set para las listas
    #recuperamos la lista con los tiempos realizados
    def getTiempos(self): 
        return self.tiempos 
    
    # recuperamos la lista con los datos que entraron
    def getDatos(self):
        return self.datos