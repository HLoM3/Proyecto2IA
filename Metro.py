from collections import deque





"""En un diccionario se guardara todo el metro de la CDMX
Se guarda el elemento y las estaciones adyacentes
Cuando una estación es de transbordo, sus estaciones adyancetes incluye la misma estación pero de la otra línea"""
metro_cdmx = {
    # Línea 1 (Observatorio L1 - Pantitlán)
    #Transbordo
    'Pantitlan L1': ['Zaragoza L1', 'Pantitlan L5', 'Pantitlan L9', 'Pantitlan LA'],
    'Zaragoza L1': ['Pantitlan L1', 'Gomez_Farias L1'],
    'Gomez_Farias L1': ['Zaragoza L1', 'Boulevard_Puerto_Aereo L1'],
    'Boulevard_Puerto_Aereo L1': ['Gomez_Farias L1', 'Balbuena L1'],
    'Balbuena L1': ['Boulevard_Puerto_Aereo L1', 'Moctezuma L1'],
    'Moctezuma L1': ['Balbuena L1', 'San_Lazaro L1'],
    #Transbordo
    'San_Lazaro L1': ['Moctezuma L1', 'Candelaria L1', 'San Lazaro LB'],
    #Transbordo
    'Candelaria L1': ['San_Lazaro L1', 'Merced L1', 'Candelaria L4'],
    'Merced L1': ['Candelaria L1', 'Pino_Suarez L1'],
    'Pino_Suarez L1': ['Merced L1', 'Isabel_la_Catolica L1', 'Pino Suarez L2'],
    'Isabel_la_Catolica L1': ['Pino_Suarez L1', 'Salto_del_Agua L1'],
    #Transbordo
    'Salto_del_Agua L1': ['Isabel_la_Catolica L1', 'Balderas L1','Salto_del_Agua L8'],
    #Transbordo
    'Balderas L1': ['Salto_del_Agua L1', 'Cuauhtemoc L1','Balderas L3'],
    'Cuauhtemoc L1': ['Balderas L1', 'Insurgentes L1'],
    'Insurgentes L1': ['Cuauhtemoc L1', 'Sevilla L1'],
    'Sevilla L1': ['Insurgentes L1', 'Chapultepec L1'],
    'Chapultepec L1': ['Sevilla L1', 'Juanacatlan L1'],
    'Juanacatlan L1': ['Chapultepec L1', 'Tacubaya L1'],
    'Tacubaya L1': ['Juanacatlan L1', 'Observatorio L1', 'Tacubaya L7', 'Tacubaya L9'],
    'Observatorio L1': ['Tacubaya L1'],

    # Línea 2 (Cuatro_Caminos L1 - Tasqueña)
    'Cuatro_Caminos L2': ['Panteones L2'],
    'Panteones L2': ['Cuatro_Caminos L2', 'Tacuba L2'],
    #Transborde
    'Tacuba L2': ['Panteones L2', 'Cuitlahuac L2','Tacuba L7'],
    'Cuitlahuac L2': ['Tacuba L2', 'Popotla L2'],
    'Popotla L2': ['Cuitlahuac L2', 'Colegio_Militar L2'],
    'Colegio_Militar L2': ['Popotla L2', 'Normal L2'],
    'Normal L2': ['Colegio_Militar L2', 'San_Cosme L2'],
    'San_Cosme L2': ['Normal L2', 'Revolucion L2'],
    'Revolucion L2': ['San_Cosme L2', 'Hidalgo L2'],
    #Transborde
    'Hidalgo L2': ['Revolucion L2', 'Bellas_Artes L2', 'Hidalgo L3'],
    #Transborde
    'Bellas_Artes L2': ['Hidalgo L2', 'Allende L2','Bellas Artes L8'],
    'Allende L2': ['Bellas_Artes L2', 'Zocalo L2'],
    'Zocalo L2': ['Allende L2', 'Pino_Suarez L2'],
    #Transborde
    'Pino_Suarez L2': ['Zocalo L2', 'San_Antonio_Abad L2', 'Pino_Suarez L1'],
    'San_Antonio_Abad L2': ['Pino_Suarez L2', 'Chabacano L2'],
    #Transborde
    'Chabacano L2': ['San_Antonio_Abad L2', 'Viaducto L2', 'Chabacano L8', 'Chabacano L9'],
    'Viaducto L2': ['Chabacano L2', 'Xola L2'],
    'Xola L2': ['Viaducto L2', 'Villa_de_Cortes L2'],
    'Villa_de_Cortes L2': ['Xola L2', 'Nativitas L2'],
    'Nativitas L2': ['Portales L2', 'Villa_de_Cortes L2'],
    'Portales L2': ['Ermita L2', 'Nativitas L2'],
    #Transborde
    'Ermita L2': ['General_Anaya L2', 'Portales L2', 'Ermita L12'],
    'General_Anaya L2': ['Ermita L2', 'Tasquena L2'],
    'Tasquena L2': ['General_Anaya L2'],

    #Linea 3 (Indios Verdes L3 - Universidad)
    'Indios Verdes L3': ['Deportivo_18_de_Marzo'],
    #Transborde
    'Deportivo_18_de_Marzo L3': ['Indios Verdes L3', 'Potrero L3', 'Deportivo_18_de_Marzo L6'],
    'Potrero L3': ['Deportivo_18_de_Marzo L3','La_Raza L3'],
    #Transborde
    'La_Raza L3': ['Potrero L3', 'Tlaltelolco L3', 'La_Raza L5'],
    'Tlaltelolco L3': ['La_Raza L3', 'Guerrero L3'],
    #Transborde
    'Guerrero L3': ['Tlaltelolco L3', 'Hidalgo L3', 'Buenavista LB', 'Garibaldi'],
    'Hidalgo L3': ['Guerrero L3', 'Juarez L3', 'Hidalgo L2'],
    'Juarez L3': ['Hidalgo L3', 'Balderas L3'],
    'Balderas L3': ['Juarez L3', 'Ninos_heroes L3', 'Balderas L1'],
    'Ninos_heroes L3':['Balderas L3', 'Hospital_General L3'],
    'Hospital_General L3': ['Ninos_heroes L3','Centro_Medico L3'],
    #Transborde
    'Centro_Medico L3': ['Hospital_General L3', 'Etiopia L3', 'Centro_Medico L9'],
    'Etiopia L3': ['Centro_Medico L3','Eugenia L3'],
    'Eugenia L3': ['Etiopia L3', 'Division_del_Norte L3'],
    'Division_del_Norte L3': ['Eugenia L3', 'Zapata L3'],
    'Zapata L3': ['Division_del_Norte L3', 'Coyoacan L3', 'Zapata L12'],
    'Coyoacan L3': ['Zapata L3', 'Viveros L3'],
    'Viveros L3': ['Coyoacan L3', 'Miguel_Angel_de_Quevedo'],
    'Miguel_Angel_de_Quevedo': ['Viveros L3','Copilco L3'],
    'Copilco L3': ['Miguel_Angel_de_Quevedo', 'Universidad L3'],
    'Universidad L3': ['Copilco L3'],

    #Linea 4
    'Martin_Carrera L4': ['Talisman L4', 'Marin_Carrera L6'],
    'Talisman L4': ['Martin_Carrera L4', 'Bondojito L4'],
    'Bondojito L4': ['Talisman L4', 'Consulado L4'],
    'Consulado L4': ['Bondojito L4', 'Canal_del_Norte L4', 'Consulado L5'],
    'Canal_del_Norte L4': ['Consulado L4', 'Morelos L4'],
    'Morelos L4': ['Canal_del_Norte L4', 'Candelaria L4', 'Tepito LB', ''],
    'Candelaria L4': ['Morelos L4', 'Fray_Servando L4', 'Candelaria L1'],
    'Fray_Servando L4': ['Candelaria L4', 'Jamaica L4'],
    'Jamaica L4': ['Fray_Servando L4', 'Santa_Anita', 'Jamaica L9'],
    'Santa_Anita L4': ['Jamaica L4', 'Santa_Anita L8'],

    #Linea 5
    'Pantitlan L5': ['Hangares L5', 'Pantitlan L1', 'Pantitlan L9', 'Pantitlan LA'],
    'Hangares L5': ['Pantitlan L5', 'Terminal_Aerea L5'],
    'Terminal_Aerea L5': ['Hangares L5', 'Oceania L5'],
    'Oceania L5': ['Terminal_Aerea L5', 'Aragon L5'],
    'Aragon L5': ['Oceania L5', 'Eduardo_Molina L5'],
    'Eduardo_Molina L5': ['Aragon L5', 'Consulado L5'],
    'Consulado L5': ['Eduardo_Molina L5', 'Valle_Gomez L5', 'Consulado L4'],
    'Valle_Gomez L5': ['Consulado L5', 'Misterios'],
    'Misterios': ['Valle_Gomez L5', 'La Raza L5'],
    'La Raza L5': ['Misterios', 'Autobuses_del_Norte L5'],
    'Autobuses_del_Norte L5': ['La Raza L5', 'Instituto_del_Petroleo L5'],
    'Instituto_del_Petroleo L5': ['Autobuses_del_Norte L5', 'Politecnico L5', 'Instituto_del_Petroleo L6'],
    'Politecnico L5': ['Instituto del Petroleo L5'],

    #Linea 6
    'El_Rosario L6': ['Tezozomoc L6', 'Aquiles Serdan', 'El_Rosario L7'],
    'Tezozomoc L6': ['El_Rosario L6', 'UAM_Azcapotzalco L6'],
    'UAM_Azcapotzalco L6': ['Tezozómoc', 'Ferreria L6'],
    'Ferreria L6': ['UAM_Azcapotzalco L6', 'Norte_45 L6'],
    'Norte_45 L6': ['Ferreria L6', 'Vallejo L6'],
    'Vallejo L6': ['Norte_45 L6', 'Instituto_del_Petroleo L6'],
    'Instituto_del_Petroleo L6': ['Vallejo L6', 'Lindavista L6'],
    'Lindavista L6': ['Instituto_del_Petroleo L6', 'Deportivo_18_de_Marzo L6'],
    'Deportivo_18_de_Marzo L6': ['Lindavista L6', 'La_Villa L6', 'Deportivo_18_de_Marzo L3'],
    'La_Villa L6': ['Martin_Carrera L6', 'Deportivo_18_de_Marzo L6'],
    'Martin_Carrera L6': ['La_Villa L6'],

    #Linea 7
    'El_Rosario L7': ['Aquiles_Serdan L7', 'El_Rosario L6'],
    'Aquiles_Serdan L7': ['El_Rosario L7', 'Camarones L7'],
    'Camarones L7': ['Aquiles Serdan', 'Refineria L7'],
    'Refineria L7': ['Camarones L7', 'Tacuba L7'],
    'Tacuba L7': ['Refineria L7', 'San_Joaquin L7', 'Tacuba L2'],
    'San_Joaquin L7': ['Tacuba L7', 'Polanco L7'],
    'Polanco L7': ['San_Joaquin L7', 'Auditorio L7'],
    'Auditorio L7': ['Polanco L7', 'Constituyentes L7'],
    'Constituyentes L7': ['Auditorio L7', 'Tacubaya L7'],
    'Tacubaya L7': ['Constituyentes L7', 'San_Pedro_de_los_Pinos L7', 'Tacubaya L1', 'Tacubaya L9'],
    'San_Pedro_de_los_Pinos L7': ['Tacubaya L7', 'San_Antonio L7'],
    'San_Antonio L7': ['San_Pedro_de_los_Pinos L7', 'Mixcoac L7'],
    'Mixcoac L7': ['San_Antonio L7', 'Barranca_del_Muerto L7', 'Mixcoac L12'],
    'Barranca_del_Muerto L7': ['Mixcoac L7'],

    #Linea 8
    'Garibaldi L8': ['Bellas_Artes L8', 'Garibaldi LB'],
    'Bellas_Artes L8': ['Garibaldi L8', 'San_Juan_de_Letran L8'],
    'San_Juan_de_Letran L8': ['Bellas Artes L8', 'Salto_del_Agua L8'],
    'Salto_del_Agua L8': ['San_Juan_de_Letran L8', 'Doctores L8'],
    'Doctores L8': ['Salto_del_Agua L8', 'Obrera L8'],
    'Obrera L8': ['Doctores L8', 'Chabacano L8'],
    'Chabacano L8': ['Obrera L8', 'La Viga', 'Chabacano L9'],
    'La Viga': ['Chabacano L8', 'Santa_Anita L8'],
    'Santa_Anita L8': ['La Viga', 'Coyuya L8', 'Santa Anita L4'],
    'Coyuya L8': ['Santa_Anita L8', 'Iztacalco L8'],
    'Iztacalco L8': ['Coyuya L8', 'Apatlaco L8'],
    'Apatlaco L8': ['Iztacalco L8', 'Aculco L8'],
    'Aculco L8': ['Apatlaco L8', 'Escuadron_201 L8'],
    'Escuadron_201 L8': ['Aculco L8', 'Atlalilco L8'],
    'Atlalilco L8': ['Escuadron_201 L8', 'Iztapalapa L8', 'Atlalilco L12'],
    'Iztapalapa L8': ['Atlalilco L8', 'Cerro_de_la_Estrella L8'],
    'Cerro_de_la_Estrella L8': ['Iztapalapa L8', 'UAM-I L8'],
    'UAM-I L8': ['Cerro_de_la_Estrella L8', 'Constitucion_de_1917 L8'],
    'Constitucion_de_1917 L8': ['UAM-I L8'],

    #Linea 9
    'Pantitlan L9': ['Puebla L9', 'Pantitlan L1', 'Pantitlan L5', 'Pantitlan LA'],
    'Puebla L9': ['Pantitlan L9', 'Ciudad_Deportiva L9'],
    'Ciudad_Deportiva L9': ['Puebla L9', 'Velodromo L9'],
    'Velodromo L9': ['Ciudad_Deportiva L9', 'Mixiuhca L9'],
    'Mixiuhca L9': ['Velodromo L9', 'Jamaica L9'],
    'Jamaica L9': ['Mixiuhca L9', 'Chabacano L9'],
    'Chabacano L9': ['Jamaica L9', 'Lazaro_Cardenas L9', 'Chabacano L2', 'Chabacano L8'],
    'Lazaro_Cardenas L9': ['Chabacano', 'Centro_Medico L9'],
    'Centro_Medico L9': ['Lazaro_Cardenas L9', 'Chilpancingo L9', 'Centro Medico L3'],
    'Chilpancingo L9': ['Centro_Medico L9', 'Patriotismo L9'],
    'Patriotismo L9': ['Chilpancingo L9', 'Tacubaya L9'],
    'Tacubaya L9': ['Patriotismo L9', 'Tacubaya L7', 'Tacubaya L1'],

    #Linea A
    'Pantitlan LA': ['Agricola_Oriental LA', 'Pantitlan L1', 'Pantitlan L5', 'Pantitlan L9'],
    'Agricola_Oriental LA': ['Pantitlan LA', 'Canal_de_San_Juan LA'],
    'Canal_de_San_Juan LA': ['Agricola_Oriental LA', 'Tepalcates LA'],
    'Tepalcates LA': ['Canal_de_San_Juan LA', 'Guelatao LA'],
    'Guelatao LA': ['Tepalcates LA', 'Penon_Viejo LA'],
    'Penon_Viejo LA': ['Guelatao LA', 'Acatitla LA'],
    'Acatitla LA': ['Penon_Viejo LA', 'Santa_Marta LA'],
    'Santa_Marta LA': ['Acatitla LA', 'Los_Reyes LA'],
    'Los_Reyes LA': ['Santa_Marta LA', 'La_Paz LA'],
    'La_Paz LA': ['Los_Reyes LA'],

    #Linea B
    'Buenavista LB': ['Guerrero LB'],
    'Guerrero LB': ['Buenavista LB', 'Garibaldi LB', 'Guerrero L3'],
    'Garibaldi LB': ['Guerrero LB', 'Lagunilla LB', 'Garibaldi L8'],
    'Lagunilla LB': ['Garibaldi LB', 'Tepito LB'],
    'Tepito LB': ['Lagunilla LB', 'Morelos LB'],
    'Morelos LB': ['Tepito LB', 'San_Lazaro LB', 'Morelos L4'],
    'San_Lazaro LB': ['Morelos LB', 'Ricardo_Flores_Magon LB', 'San_Lazaro L1'],
    'Ricardo_Flores_Magon LB': ['San_Lazaro LB', 'Romero_Rubio LB'],
    'Romero_Rubio LB': ['Ricardo_Flores_Magon LB', 'Oceania LB'],
    'Oceania LB': ['Romero_Rubio LB', 'Deportivo_Oceania LB', 'Oceania L5'],
    'Deportivo_Oceania LB': ['Oceania LB', 'Villa_de_Aragon LB'],
    'Villa_de_Aragon LB': ['Deportivo_Oceania LB', 'Nezahualcoyotl LB'],
    'Nezahualcoyotl LB': ['Villa_de_Aragon LB', 'Impulsora LB'],
    'Impulsora LB': ['Nezahualcoyotl LB', 'Rio_de_los_Remedios LB'],
    'Rio_de_los_Remedios LB': ['Impulsora LB', 'Muzquiz LB'],
    'Muzquiz LB': ['Rio_de_los_Remedios LB', 'Ecatepec LB'],
    'Ecatepec LB': ['Muzquiz LB', 'Olimpica LB'],
    'Olimpica LB': ['Ecatepec LB', 'Plaza_Aragon LB'],
    'Plaza_Aragon LB': ['Olimpica LB', 'Ciudad_Azteca LB'],
    'Ciudad_Azteca LB': ['Plaza_Aragon LB'],

    #Linea 12
    'Mixcoac L12': ['Insurgentes_Sur L12', 'Mixcoac L7'],
    'Insurgentes_Sur L12': ['Mixcoac L12', '20_de_Noviembre L12'],
    '20_de_Noviembre L12': ['Insurgentes_Sur L12', 'Zapata L12'],
    'Zapata L12': ['20_de_Noviembre L12', 'Parque_de_los_Venados L12', 'Zapata L3'],
    'Parque_de_los_Venados L12': ['Zapata L12', 'Eje_Central L12'],
    'Eje_Central L12': ['Parque_de_los_Venados L12', 'Ermita L12'],
    'Ermita L12': ['Eje_Central L12', 'Mexicaltzingo L12', 'Ermita L12'],
    'Mexicaltzingo L12': ['Ermita L2', 'Atlalilco L12'],
    'Atlalilco L12': ['Mexicaltzingo L12', 'Culhuacan L12', 'Atlalilco L8'],
    'Culhuacan L12': ['Atlalilco L12', 'San_Andres_Tomatlan L12'],
    'San_Andres_Tomatlan L12': ['Culhuacan L12', 'Lomas_Estrella L12'],
    'Lomas_Estrella L12': ['San_Andres_Tomatlan L12', 'Calle_11 L12'],
    'Calle_11 L12': ['Lomas_Estrella L12', 'Periferico_Oriente L12'],
    'Periferico_Oriente L12': ['Calle_11 L12', 'Tezonco L12'],
    'Tezonco L12': ['Periferico_Oriente L12', 'Olivos L12'],
    'Olivos L12': ['Tezonco L12', 'Nopalera L12'],
    'Nopalera L12': ['Olivos L12', 'Zapotitlan L12'],
    'Zapotitlan L12': ['Nopalera L12', 'Tlaltenco L12'],
    'Tlaltenco L12': ['Zapotitlan L12', 'Tlahuac L12'],
    'Tlahuac L12': ['Tlaltenco L12']
}


def encontrar_ruta(metro, inicio, destino):
    # Cola para BFS
    queue = deque([(inicio, [inicio])])  # Cada elemento es una tupla (estación actual, ruta tomada)
    visitados = set()  # Para no visitar estaciones dos veces

    while queue:
        estacion_actual, ruta = queue.popleft()
        # Si llegamos al destino, devolvemos la ruta
        if estacion_actual == destino:
            return ruta
        # Marcar como visitado
        visitados.add(estacion_actual)

        # Añadir las conexiones no visitadas a la cola
        for vecino in metro.get(estacion_actual, []):
            if vecino not in visitados:
                queue.append((vecino, ruta + [vecino]))

    return None  # Si no se encuentra ruta


# Ejemplo de uso
#inicio = 'Universidad'
#destino = 'Buenavista LB'
#ruta = encontrar_ruta(metro_cdmx, inicio, destino)

#print("Ruta de {} a {}: {}".format(inicio, destino, ruta))


# Definir las zonas y subzonas
zonas = {
    "Zona1": {
        "Subzona1": ["Ciudad_Azteca LB", "Plaza_Aragon LB", "Olimpica LB", "Ecatepec LB", "Muzquiz LB", "Rio_de_los_Remedios LB"],
        "Subzona2": ["Impulsora LB", "Nezahualcoyotl LB", "Villa_de_Aragon LB", "Bosque_de_Aragon LB", "Deportivo_Oceania LB"]
    },
    "Zona2": {
        "Subzona3": ["Martin_Carrera L6", "Martin_Carrera L4", "Talisman L4", "La_Villa L4"],
        "Subzona4": ["Bondojito L4", "Consulado L5", "Consulado L4", "Valle_Gomez L5"],
        "Subzona5": ["Misterios L5", "Tlaltelolco L3", "La_Raza L3", "La_Raza L5"],
        "Subzona6": ["Politecnico L5", "Vallejo L6", "Instituto_del_Petroleo L6", "Instituto_del_Petroleo L5", "Autobuses_del_Norte L5"],
        "Subzona7": ["Indios_Verdes L3", "Deportivo_18_de_Marzo L3", "Deportivo_18_de_Marzo L6", "Lindavista L6", "Potrero L3"]
    },
    "Zona3": {
        "Subzona8": ["Oceania L5", "Oceania LB", "Eduardo_Molina L5", "Aragon L5", "Romero_Rubio LB", "Ricardo_Flores_Magon LB"],
        "Subzona9": ["Canal_del_Norte L4", "Morelos L4", "Morelos LB", "Tepito LB", "Merced L1", "Candelaria L1", "Candelaria L4", "San_Lazaro LB", "San_Lazaro L1"],
        "Subzona10": ["Moctezuma L1", "Balbuena L1", "Boulevard_Puerto_Aereo L1", "Terminal_Aerea L5", "Velodromo L9"],
        "Subzona11": ["La_Viga L8", "Jamaica L9", "Jamaica L4", "Mixiuhca L9", "Velodromo L9", "Santa_Anita L8", "Santa_Anita L4"],
        "Subzona12": ["Pantitlan L5", "Pantitlan L9", "Pantitlan L1", "Pantitlan LA", "Puebla L9", "Ciudad_deportiva L9", "Zaragoza L1", "Hangares L5", "Gomez_Farias L1"]
    },
    "Zona4": {
        "Subzona13": ["Agricola_Oriental LA", "Canal_de_San_Juan LA", "Tepalcates LA", "Guelatao LA"],
        "Subzona14": ["Penon_Viejo LA", "Acatitla LA", "Santa_Marta LA", "Los_Reyes LA", "La_Paz LA"]
    },
    "Zona5": {
        "Subzona15": ["Coyuya L8", "Iztacalco L8", "Apatlalco L8"],
        "Subzona16": ["Aculco L8", "Escuadron_201 L8", "Atlalilco L12", "Atlalilco L8", "Iztapalapa L8", "Mexicaltzingo L12"],
        "Subzona17": ["Cerro_de_la_Estrella L8", "UAM-1 L8", "Constitucion_de_1917 L8"],
        "Subzona18": ["Culhuacan L12", "San_Andres_Tomatlan L12", "Lomas_Estrella L12", "Calle_11 L12"],
        "Subzona19": ["Periferico_Oriente L12", "Tezonco L12", "Olivos L12", "Nopalera L12", "Zapotitlan L12", "Tlaltenco L12", "Tlahuac L12"]
    },
    "Zona6": {
        "Subzona20": ["Division_del_Norte L3", "Zapata L3", "Zapata L12", "Parque_de_los_Venados L12", "Eje_Central L12"],
        "Subzona21": ["Mixcoac L12", "Mixcoac L7", "Barranca_del_Muerto L7", "Hospital_20_de_Noviembre L12", "Insurgentes_Sur L12", "Coyoacan L3"],
        "Subzona22": ["Universidad L3", "Copilco L3", "Miguel_Angel_de_Quevedo L3", "Viveros L3"],
        "Subzona23": ["Nativitas L2", "Portales L2", "Ermita L12", "Ermita L2", "General_Anaya L2", "Tasquena L2"]
    },

}

# Implementación de búsquedas específicas (dentro de una subzona, entre subzonas y entre zonas)
def busqueda_interzonal(estacion_inicio, estacion_destino):
    # BFS para búsqueda de la ruta más corta dentro de una subzona
    from collections import deque

    visitados = set()
    cola = deque([[estacion_inicio]])

    while cola:
        ruta = cola.popleft()
        estacion_actual = ruta[-1]

        if estacion_actual == estacion_destino:
            return ruta

        if estacion_actual not in visitados:
            visitados.add(estacion_actual)
            for vecino in metro_cdmx.get(estacion_actual, []):
                if vecino not in visitados:
                    nueva_ruta = list(ruta)
                    nueva_ruta.append(vecino)
                    cola.append(nueva_ruta)

    return None  # Si no hay ruta


def busqueda_entre_subzonas(estacion_inicio, estacion_destino, zona):
    # Encuentra la subzona de inicio y destino
    subzona_inicio, subzona_destino = None, None
    for subzona, estaciones in zonas[zona].items():
        if estacion_inicio in estaciones:
            subzona_inicio = subzona
        if estacion_destino in estaciones:
            subzona_destino = subzona

    if subzona_inicio == subzona_destino:
        # Mismo subzona, búsqueda interzonal
        return busqueda_interzonal(estacion_inicio, estacion_destino)
    else:
        # Diferentes subzonas, conecta a través de BFS entre subzonas
        ruta = busqueda_interzonal(estacion_inicio, estacion_destino)
        if ruta:
            return ruta
        else:
            # Si no hay ruta directa, buscar transbordos
            # Aquí puedes implementar una búsqueda que intente conectar ambas subzonas vía estaciones de transbordo
            for estacion in zonas[zona][subzona_inicio]:
                for destino in zonas[zona][subzona_destino]:
                    inter_ruta = busqueda_interzonal(estacion, destino)
                    if inter_ruta:
                        return [estacion_inicio] + inter_ruta + [estacion_destino]

    return None  # Si no hay ruta

def encontrar_zona_subzona(estacion):
    for zona, subzonas in zonas.items():
        for subzona, estaciones in subzonas.items():
            if estacion in estaciones:
                return zona, subzona
    return None, None

# Búsqueda de la ruta entre estaciones
def encontrar_ruta(estacion_inicio, estacion_destino):
    zona_inicio, subzona_inicio = encontrar_zona_subzona(estacion_inicio)
    zona_destino, subzona_destino = encontrar_zona_subzona(estacion_destino)

    if zona_inicio == zona_destino:
        if subzona_inicio == subzona_destino:
            # Ruta dentro de la misma subzona
            return busqueda_interzonal(estacion_inicio, estacion_destino)
        else:
            # Ruta dentro de la misma zona pero diferentes subzonas
            return busqueda_entre_subzonas(estacion_inicio, estacion_destino, zona_inicio)
    else:
        # Ruta entre diferentes zonas
        return busqueda_entre_zonas(estacion_inicio, estacion_destino)

def busqueda_entre_zonas(estacion_inicio, estacion_destino):
    # Encuentra la zona y subzona de inicio y destino
    zona_inicio, subzona_inicio = encontrar_zona_subzona(estacion_inicio)
    zona_destino, subzona_destino = encontrar_zona_subzona(estacion_destino)

    # Si están en la misma zona, utiliza `busqueda_entre_subzonas`
    if zona_inicio == zona_destino:
        return busqueda_entre_subzonas(estacion_inicio, estacion_destino, zona_inicio)
    else:
        # Diferentes zonas: intenta conectar a través de transbordos
        # Primero busca ruta en zona de inicio hacia una estación de transbordo a la otra zona
        ruta_inicio = []
        for estacion_intermedia in zonas[zona_inicio][subzona_inicio]:
            ruta_inicio = busqueda_interzonal(estacion_inicio, estacion_intermedia)
            if ruta_inicio:
                break

        # Luego, busca ruta en la zona de destino desde una estación de transbordo
        ruta_destino = []
        for estacion_intermedia in zonas[zona_destino][subzona_destino]:
            ruta_destino = busqueda_interzonal(estacion_intermedia, estacion_destino)
            if ruta_destino:
                break

        if ruta_inicio and ruta_destino:
            # Concatena la ruta de inicio y la ruta de destino
            return ruta_inicio + ruta_destino[1:]

    return None  # Si no hay ruta

print(encontrar_zona_subzona("Impulsora LB"))

print(encontrar_ruta("Indios_Verdes L3", "Potrero L3"))