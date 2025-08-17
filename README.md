# 🚀 Interfaz de Monitoreo para Cohetes y Satélites

Este proyecto es una interfaz gráfica desarrollada con **PySide6**, diseñada para visualizar en tiempo real los datos transmitidos por sistemas de **cohetería experimental** y satélites tipo **CANSAT**.  

Su propósito es representar de manera clara la información recibida durante el vuelo o en fase de pruebas, ya sea proveniente de un **cohete** o de un **satélite**, dependiendo de lo que se esté monitoreando en ese momento.  

Entre los parámetros que se pueden visualizar se incluyen:  

- 🌡️ **Temperatura**  
- 📈 **Presión**  
- 🛰️ **Altura**  
- 📡 **Telemetría general del vuelo**  

De esta forma, la herramienta se convierte en un apoyo esencial para la interpretación y análisis de datos en proyectos aeroespaciales estudiantiles.  

---

## 🧩 Arquitectura del Proyecto

El sistema está basado en el patrón de diseño **MVC (Modelo - Vista - Controlador)**, lo cual permite:  

- 🧼 Separación clara de responsabilidades  
- 📦 Organización modular con clases orientadas a objetos  
- 🎨 Estilos visuales personalizables con hojas `.qss`  
- 🖼️ Vistas independientes por funcionalidad  
- 🔗 Fácil integración con otros sistemas  

Este enfoque ofrece una experiencia visual limpia, escalable y adaptable a las necesidades futuras del equipo.  

---

## ⚙️ Configuración del Entorno Virtual

### 1️⃣ Crear el entorno virtual

```bash
# En Windows
python -m venv env
env\Scripts\activate.bat

# En Linux o MacOS
python3 -m venv env
source env/bin/activate

#Instalar dependencias
pip install PySide6 vtk pyserial pandas matplotlib numpy
