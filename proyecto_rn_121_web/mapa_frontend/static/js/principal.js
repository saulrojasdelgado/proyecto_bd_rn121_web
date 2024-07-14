// Evento que se dispara al cargar la página web
document.addEventListener("DOMContentLoaded", iniciar)

// Función que se invoca con el disparo de "DOMContentLoaded"
function iniciar() {

// Objeto del mapa Leaflet
    var mapa = L.map('mapaid').setView([9.93, -84.20], 15);

// Capa base de OSM
    osm = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 50,
        attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(mapa);

    // Capa base de Carto
    positromap = L.tileLayer(
        "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png",
        {
          attribution:
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: "abcd",
          maxZoom: 50,
        }
    );

// Capa base de ESRI
    esriworld = L.tileLayer(
        "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        {
        attribution:
            "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
          
        }
    );

// Objeto de capas base
    var mapasbase = {
      OpenStreetMap: osm,
      "Carto Positron": positromap,
      "ESRI WorldImagery": esriworld,
    };

// Control de capas
    control_capas = L.control
    .layers(mapasbase, null, { collapsed: false })
    .addTo(mapa);

// Control de escala
    L.control.scale().addTo(mapa);

// Función asíncrona que realiza una solicitud HTTP (tipo GET) 
// a una URL especificada, procesa la respuesta JSON y luego
// ejecuta una función pasada como argumento con los datos JSON obtenidos.
    const fetchGetRequest = async(url, func) => {
        try {
            const response = await fetch(url)
            const json = await response.json()
            return func(json)
        } catch (error) {
            console.log(error.message)
        }    
    }




// Función que agrega los datos GeoJSON al mapa
const agregarPozos_rn121AlMapa = (json) => {
    // console.log(json)

    // Se obtienen los datos en GeoJSON
    Pozos_rn121 = L.geoJSON(json, {}).addTo(mapa);

    // Capa de puntos agrupados
    var Pozos_rn121_agrupadas = L.markerClusterGroup({
    spiderfyOnMaxZoom: true,
    });
    Pozos_rn121_agrupadas.addLayer(Pozos_rn121);

    // Capa de calor (heatmap)
    coordenadas = json.features.map((feat) =>
        feat.geometry.coordinates.reverse()
    );
    var Pozos_rn121_calor = L.heatLayer(coordenadas, { radius: 40, blur: 1, });


    // Se añade la capa al mapa y al control de capas
    Pozos_rn121_agrupadas.addTo(mapa);
    control_capas.addOverlay(
        Pozos_rn121_agrupadas,
        "Pozos agrupados"
    );

    Pozos_rn121_calor.addTo(mapa);
    control_capas.addOverlay(
        Pozos_rn121_calor,
        "Intensidad de Pozos (Calor)"
    );

    // Se agrgan los datos GeoJSON al mapa
    control_capas.addOverlay(Pozos_rn121, "Pozos pluviales");      
}

    // Llamado a fetchGetRequest()
    fetchGetRequest('/api/v1/Pozos_rn121', agregarPozos_rn121AlMapa)
}