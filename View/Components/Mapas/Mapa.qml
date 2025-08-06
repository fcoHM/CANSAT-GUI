import QtQuick 2.15
import QtLocation 5.15
import QtPositioning 5.15

// Item es el contenedor base para los elementos visuales en QML.
Item {
    // anchors.fill: parent hace que este contenedor ocupe todo el espacio de su padre (la ventana).
    anchors.fill: parent

    // --- Configuración del proveedor del mapa ---
    // El Plugin especifica qué servicio de mapas se usará.
    Plugin {
        id: mapPlugin
        name: "osm" // "osm" se refiere a OpenStreetMap.
        // Este parámetro asegura que se use un servidor de tiles gratuito y sin marcas de agua.
        PluginParameter { name: "osm.mapping.host"; value: "https://tile.openstreetmap.org/" }
    }

    // --- El componente del Mapa ---
    Map {
        id: mapa
        anchors.fill: parent
        plugin: mapPlugin // Le dice al mapa que use el plugin que definimos arriba.
        zoomLevel: 14 // Nivel de zoom inicial.

        // Coordenada inicial donde se centrará el mapa al arrancar.
        center: QtPositioning.coordinate(22.15, -102.3)

        // --- Marcador en el mapa ---
        // MapQuickItem es un elemento que se puede posicionar en el mapa usando coordenadas.
        MapQuickItem {
            id: marcador
            // Coordenada inicial del marcador.
            coordinate: QtPositioning.coordinate(22.15, -102.3)
            
            // El anchorPoint ajusta dónde se "ancla" la imagen del marcador.
            // (width / 2, height) centra el punto de anclaje en la base del icono.
            anchorPoint.x: icon.width / 2
            anchorPoint.y: icon.height

            // sourceItem define la apariencia visual del marcador.
            sourceItem: Image {
                id: icon
                source: "https://cdn-icons-png.flaticon.com/512/684/684908.png" // URL del icono.
                width: 32
                height: 32
            }
        }

        // --- La conexión clave entre QML y Python ---
        // El elemento Connections se usa para "escuchar" las señales de un objeto.
        Connections {
            // 'target: gps' le dice que escuche al objeto "gps" que expusimos desde Python.
            target: gps
            
            // Esta función se ejecuta AUTOMÁTICAMENTE cada vez que el objeto 'gps' en Python
            // emite la señal 'coordenadas_actualizadas'.
            // El nombre de la función debe ser 'on' + el nombre de la señal (en formato camelCase).
            function onCoordenadas_actualizadas(lat, lon) {
                // 'lat' y 'lon' son los valores que se enviaron con la señal desde Python.
                
                // Actualiza la posición del marcador en el mapa con las nuevas coordenadas.
                marcador.coordinate = QtPositioning.coordinate(lat, lon)
                // Centra el mapa en la nueva posición del marcador.
                mapa.center = marcador.coordinate
            }
        }
    }
}

