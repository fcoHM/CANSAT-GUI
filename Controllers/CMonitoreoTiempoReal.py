# logica de ventana monitoreo en tiempo real
from Tools.SerialManager import SerialManager
from PySide6.QtCore import Slot
import random

class CMonitoreoTiempoReal:

    def __init__(self):
        self.serialManager = SerialManager() # herramienta para el manejo de puertos seriales
        self.vista = None
        # Conectar la señal de datos recibidos al slot de actualización
        self.serialManager.linea_recibida.connect(self.actualizar_grafica)

    
    def actualizar_puertos(self): # actualizar los puertos, mandando una nueva lista
        puertos = self.serialManager.listar_puertos()
        self.vista.puertosSerial.clear()
        self.vista.puertosSerial.addItems(puertos)
    
    def listar_puertos(self): # listar los puertos que estan conectados
        return self.serialManager.listar_puertos()

    def conectar_puerto(self): # conecta un puesrto serial segun le digamos cual
        puerto = self.vista.obtener_puerto()
        velocidad = self.vista.obtener_velocidad()
        self.serialManager.set_baudios(velocidad)
        
        if self.serialManager.conectar(puerto):
            self.vista.mostrar_mensaje("Éxito", f"Conectado a {puerto} a {velocidad} baudios.")
            self.actualizar_puertos()
        else:
            self.vista.mostrar_mensaje("Error", f"No se pudo conectar a {puerto}.", "warning")

    def desconectar_puerto(self): # desconecta el puerto serial que se esta utilizando
        if self.serialManager.desconectar():
            self.vista.mostrar_mensaje("Éxito", "Se cerró la comunicación con el puerto.")
            self.actualizar_puertos()
        else:
            self.vista.mostrar_mensaje("Error", "No se cerró la comunicación con el puerto.", "warning")

    @Slot(str)
    def actualizar_grafica(self, linea=""):# procesamiento de la cadena de texto
        if not linea:
            return  # si la línea está vacía, no hacer nada

        try:
            # suponiendo que los datos son: rotX, rotY, rotZ, temp, ...
            datos = [float(valor) for valor in linea.split(",")]
            
            # Asegurarse de que hay suficientes datos antes de acceder a ellos
            if len(datos) >= 3:
                # Añadir una pequeña variación aleatoria para simular movimiento
                rotX = datos[0] + random.uniform(-2, 2)
                rotY = datos[1] + random.uniform(-2, 2)
                rotZ = datos[2] + random.uniform(-2, 2)

                # datos[0], datos[1], datos[2] para la orientación
                self.vista.visual.actualizarOrientacion(rotX, rotY, rotZ)
                
                # datos[3] para la temperatura (si existen)
                # if len(datos) > 3:
                #     self.vista.temperatura.agregarDato(datos[3])
            else:
                print(f"Advertencia: Se recibieron datos incompletos: {linea}")

        except (ValueError, IndexError) as e:
            print(f"Error al procesar la línea de datos: '{linea}'. Error: {e}")
        

    def iniciar_monitoreo(self): # inicar el escaneo del puerto serial
        self.serialManager.iniciar_escaneo()
    

    def detener_monitoreo(self): # detener el ecaneo del puerto serial
        if self.serialManager.detener_escaneo(): 
            self.vista.mostrar_mensaje("Exito", "Se  detuvo el escaneo del puerto")
            
        else:
            self.vista.mostrar_mensaje("Error", "No se  detuvo el escaneo del puerto", "warning")