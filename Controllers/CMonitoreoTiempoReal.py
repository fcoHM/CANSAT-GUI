# logica de ventana monitoreo en tiempo real
from Tools.SerialManager import SerialManager
from PySide6.QtCore import Slot

class CMonitoreoTiempoReal:

    def __init__(self):
        self.serialManager = SerialManager() # herramienta para el manejo de puertos seriales
        self.vista = None
        # Conectar la señal de datos recibidos al slot de actualización
        self.serialManager.linea_recibida.connect(self.actualizar_graficos)

    
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
    def actualizar_graficos(self, linea=""):# procesamiento de la cadena de texto
        if not linea:
            return  # si la línea está vacía, no hacer nada

        try:
            # ACCX,ACCY,ACCZ,GYRX,GYRY,GYRZ,TEMP,HUM,PRESS,ALT,GAS,LAT,LON
            datos = [float(valor) for valor in linea.split(",")]
            
            # Asegurarse de que hay suficientes datos antes de acceder a ellos
            if len(datos) >= 13:
                # Acelerometro (no se usan en la GUI, pero se leen)
                # acrx = datos[0]
                # acry = datos[1]
                # acrz = datos[2]

                # Datos del giroscopio para el visualizador 3D
                gx = datos[3]
                gy = datos[4]
                gz = datos[5]

                # Datos de los sensores para las gráficas
                tem = datos[6]
                humedad = datos[7]
                press = datos[8]
                alt = datos[9]
                calAire = datos[10]
                
                # Datos del GPS
                lat = datos[11]
                lon = datos[12]

                # Se envian los datos a la vista para ser actualizados
                self.vista.actualizarInformacion(gx, gy, gz, tem, humedad, press, alt, calAire, lon, lat)

            else:
                print(f"Advertencia: Se recibieron datos incompletos: {linea}")

        except (ValueError, IndexError) as e:
            print(f"Error al procesar la línea de datos: '{linea}'. Error: {e}")
        

    def iniciar_monitoreo(self): # inicar el escaneo del puerto serial
        if self.serialManager.iniciar_escaneo():
            self.vista.mostrar_mensaje("Exito", "Se inicio el monitoreo")
        else:
            self.vista.mostrar_mensaje("Error", "No se inicio el monitoreo", "warning")

    

    def detener_monitoreo(self): # detener el ecaneo del puerto serial
        if self.serialManager.detener_escaneo() and self.serialManager.desconectar():
            self.actualizar_puertos()
            self.vista.temperatura.limpiarVista()
            self.vista.visual.limpiarVista()
            self.vista.mostrar_mensaje("Exito", "Se  detuvo el escaneo y se desconecto el puerto")
        else:
            self.vista.mostrar_mensaje("Error", "No se detuvo el escaneo del puerto", "warning")

    