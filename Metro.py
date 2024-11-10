from collections import deque





"""En un diccionario se guardara todo el metro de la CDMX
Se guarda el elemento y las estaciones adyacentes
Cuando una estación es de transbordo, sus estaciones adyancetes incluye la misma estación pero de la otra línea"""
metro_cdmx = {
    # Línea 1 (Observatorio - Pantitlán)
    #Transbordo
    'Pantitlan L1': ['Zaragoza', 'Pantitlan L5', 'Pantitlan L9', 'Pantitlan LA'],
    'Zaragoza': ['Pantitlan L1', 'Gomez Farias'],
    'Gomez Farias': ['Zaragoza', 'Boulevard Puerto Aereo'],
    'Boulevard Puerto Aereo': ['Gomez Farias', 'Balbuena'],
    'Balbuena': ['Boulevard Puerto Aereo', 'Moctezuma'],
    'Moctezuma': ['Balbuena', 'San Lazaro L1'],
    #Transbordo
    'San Lazaro L1': ['Moctezuma', 'Candelaria L1', 'San Lazaro LB'],
    #Transbordo
    'Candelaria L1': ['San Lazaro L1', 'Merced', 'Candelaria L4'],
    'Merced': ['Candelaria L1', 'Pino Suarez L1'],
    'Pino Suarez L1': ['Merced', 'Isabel la Catolica', 'Pino Suarez L2'],
    'Isabel la Catolica': ['Pino Suarez L1', 'Salto del Agua L1'],
    #Transbordo
    'Salto del Agua L1': ['Isabel la Catolica', 'Balderas L1','Salto del Agua L8'],
    #Transbordo
    'Balderas L1': ['Salto del Agua L1', 'Cuauhtemoc','Balderas L3'],
    'Cuauhtemoc': ['Balderas L1', 'Insurgentes'],
    'Insurgentes': ['Cuauhtemoc', 'Sevilla'],
    'Sevilla': ['Insurgentes', 'Chapultepec'],
    'Chapultepec': ['Sevilla', 'Juanacatlan'],
    'Juanacatlan': ['Chapultepec', 'Tacubaya L1'],
    'Tacubaya L1': ['Juanacatlan', 'Observatorio', 'Tacubaya L7', 'Tacubaya L9'],
    'Observatorio': ['Tacubaya L1'],

    # Línea 2 (Cuatro Caminos - Tasqueña)
    'Cuatro Caminos': ['Panteones'],
    'Panteones': ['Cuatro Caminos', 'Tacuba L2'],
    #Transborde
    'Tacuba L2': ['Panteones', 'Cuitlahuac','Tacuba L7'],
    'Cuitlahuac': ['Tacuba L2', 'Popotla'],
    'Popotla': ['Cuitlahuac', 'Colegio Militar'],
    'Colegio Militar': ['Popotla', 'Normal'],
    'Normal': ['Colegio Militar', 'San Cosme'],
    'San Cosme': ['Normal', 'Revolucion'],
    'Revolucion': ['San Cosme', 'Hidalgo L2'],
    #Transborde
    'Hidalgo L2': ['Revolucion', 'Bellas Artes L2', 'Hidalgo L3'],
    #Transborde
    'Bellas Artes L2': ['Hidalgo L2', 'Allende','Bellas Artes L8'],
    'Allende': ['Bellas Artes L2', 'Zocalo'],
    'Zocalo': ['Allende', 'Pino Suarez L2'],
    #Transborde
    'Pino Suarez L2': ['Zocalo', 'San Antonio Abad', 'Pino Suarez L1'],
    'San Antonio Abad': ['Pino Suarez L2', 'Chabacano L2'],
    #Transborde
    'Chabacano L2': ['San Antonio Abad', 'Viaducto', 'Chabacano L8', 'Chabacano L9'],
    'Viaducto': ['Chabacano L2', 'Xola'],
    'Xola': ['Viaducto', 'Villa de Cortes'],
    'Villa de Cortes': ['Xola', 'Nativitas'],
    'Nativitas': ['Portales', 'Villa de Cortés'],
    'Portales': ['Ermita L2', 'Nativitas'],
    #Transborde
    'Ermita L2': ['General Anaya', 'Portales', 'Ermita L12'],
    'General Anaya': ['Ermita L2', 'Tasquena'],
    'Tasquena': ['General Anaya'],

    #Linea 3 (Indios Verdes - Universidad)
    'Indios Verdes': ['Deportivo 18 de Marzo'],
    #Transborde
    'Deportivo 18 de Marzo L3': ['Indios Verdes', 'Potrero', 'Deportivo 18 de Marzo L6'],
    'Potrero': ['Deportivo 18 de Marzo L3','La Raza L3'],
    #Transborde
    'La Raza L3': ['Potrero', 'Tlaltelolco', 'La Raza L5'],
    'Tlaltelolco': ['La Raza L3', 'Guerrero L3'],
    #Transborde
    'Guerrero L3': ['Tlaltelolco', 'Hidalgo L3', 'Buenavista', 'Garibaldi'],
    'Hidalgo L3': ['Guerrero L3', 'Juarez', 'Hidalgo L2'],
    'Juarez': ['Hidalgo L3', 'Balderas L3'],
    'Balderas L3': ['Juarez', 'Ninos heroes', 'Balderas L1'],
    'Ninos heroes':['Balderas L3', 'Hospital General'],
    'Hospital General': ['Ninos heroes','Centro Medico L3'],
    #Transborde
    'Centro Medico L3': ['Hospital General', 'Etiopia', 'Centro Medico L9'],
    'Etiopia': ['Centro Medico L3','Eugenia'],
    'Eugenia': ['Etiopia', 'Division del Norte'],
    'Division del Norte': ['Eugenia', 'Zapata L3'],
    'Zapata L3': ['Division del Norte', 'Coyoacan', 'Zapata L12'],
    'Coyoacan': ['Zapata L3', 'Viveros'],
    'Viveros': ['Coyoacan', 'Miguel Angel de Quevedo'],
    'Miguel Angel de Quevedo': ['Viveros','Copilco'],
    'Copilco': ['Miguel Angel de Quevedo', 'Universidad'],
    'Universidad': ['Copilco'],

    #Linea 4
    'Martin Carrera L4': ['Talisman', 'Marin Carrera L6'],
    'Talisman': ['Martin Carrera L4', 'Bondojito'],
    'Bondojito': ['Talisman', 'Consulado L4'],
    'Consulado L4': ['Bondojito', 'Canal del Norte', 'Consulado L5'],
    'Canal del Norte': ['Consulado L4', 'Morelos L4'],
    'Morelos L4': ['Canal del Norte', 'Candelaria', 'Tepito', ''],
    'Candelaria': ['Morelos L4', 'Fray Servando', 'Merced', 'San Lazaro L1', 'San Lazaro LB'],
    'Fray Servando': ['Candelaria', 'Jamaica L4'],
    'Jamaica L4': ['Fray Servando', 'Santa Anita', 'Jamaica L9'],
    'Santa Anita L4': ['Jamaica L4', 'Santa Anita L8'],

    #Linea 5
    'Pantitlan L5': ['Hangares', 'Pantitlan L1', 'Pantitlan L9', 'Pantitlan LA'],
    'Hangares': ['Pantitlan L5', 'Terminal Aerea'],
    'Terminal Aerea': ['Hangares', 'Oceania L5'],
    'Oceania L5': ['Terminal Aerea', 'Aragon'],
    'Aragon': ['Oceania L5', 'Eduardo Molina'],
    'Eduardo Molina': ['Aragon', 'Consulado L5'],
    'Consulado L5': ['Eduardo Molina', 'Valle Gomez', 'Consulado L4'],
    'Valle Gomez': ['Consulado L5', 'Misterios'],
    'Misterios': ['Valle Gomez', 'La Raza L5'],
    'La Raza L5': ['Misterios', 'Autobuses del Norte'],
    'Autobuses del Norte': ['La Raza L5', 'Instituto del Petroleo L5'],
    'Instituto del Petroleo L5': ['Autobuses del Norte', 'Politecnico', 'Instituto del Petroleo L6'],
    'Politecnico': ['Instituto del Petroleo L5'],

    #Linea 6
    'El Rosario L6': ['Tezozomoc', 'Aquiles Serdan', 'El Rosario L7'],
    'Tezozomoc': ['El Rosario L6', 'UAM Azcapotzalco'],
    'UAM Azcapotzalco': ['Tezozómoc', 'Ferreria'],
    'Ferreria': ['UAM Azcapotzalco', 'Norte 45'],
    'Norte 45': ['Ferreria', 'Vallejo'],
    'Vallejo': ['Norte 45', 'Instituto del Petroleo L6'],
    'Instituto del Petroleo L6': ['Vallejo', 'Lindavista'],
    'Lindavista': ['Instituto del Petroleo L6', 'Deportivo 18 de Marzo L6'],
    'Deportivo 18 de Marzo L6': ['Lindavista', 'La Villa', 'Deportivo 18 de Marzo L3'],
    'La Villa': ['Martin Carrera L6', 'Deportivo 18 de Marzo L6'],
    'Martin Carrera L6': ['La Villa'],

    #Linea 7
    'El Rosario L7': ['Aquiles Serdan', 'El Rosario L6'],
    'Aquiles Serdan': ['El Rosario L7', 'Camarones'],
    'Camarones': ['Aquiles Serdan', 'Refineria'],
    'Refineria': ['Camarones', 'Tacuba L7'],
    'Tacuba L7': ['Refineria', 'San Joaquin', 'Tacuba L2'],
    'San Joaquin': ['Tacuba L7', 'Polanco'],
    'Polanco': ['San Joaquin', 'Auditorio'],
    'Auditorio': ['Polanco', 'Constituyentes'],
    'Constituyentes': ['Auditorio', 'Tacubaya L7'],
    'Tacubaya L7': ['Constituyentes', 'San Pedro de los Pinos', 'Tacubaya L1', 'Tacubaya L9'],
    'San Pedro de los Pinos': ['Tacubaya L7', 'San Antonio'],
    'San Antonio': ['San Pedro de los Pinos', 'Mixcoac L7'],
    'Mixcoac L7': ['San Antonio', 'Barranca del Muerto', 'Mixcoac L12'],
    'Barranca del Muerto': ['Mixcoac L7'],

    #Linea 8
    'Garibaldi L8': ['Bellas Artes L8', 'Garibaldi LB'],
    'Bellas Artes L8': ['Garibaldi L8', 'San Juan de Letran'],
    'San Juan de Letran': ['Bellas Artes L8', 'Salto del Agua L8'],
    'Salto del Agua L8': ['San Juan de Letrán', 'Doctores'],
    'Doctores': ['Salto del Agua L8', 'Obrera'],
    'Obrera': ['Doctores', 'Chabacano L8'],
    'Chabacano L8': ['Obrera', 'La Viga', 'Chabacano L9'],
    'La Viga': ['Chabacano L8', 'Santa Anita L8'],
    'Santa Anita L8': ['La Viga', 'Coyuya', 'Santa Anita L4'],
    'Coyuya': ['Santa Anita L8', 'Iztacalco'],
    'Iztacalco': ['Coyuya', 'Apatlaco'],
    'Apatlaco': ['Iztacalco', 'Aculco'],
    'Aculco': ['Apatlaco', 'Escuadrón 201'],
    'Escuadrón 201': ['Aculco', 'Atlalilco L8'],
    'Atlalilco L8': ['Escuadrón 201', 'Iztapalapa', 'Atlalilco L12'],
    'Iztapalapa': ['Atlalilco L8', 'Cerro de la Estrella'],
    'Cerro de la Estrella': ['Iztapalapa', 'UAM-I'],
    'UAM-I': ['Cerro de la Estrella', 'Constitucion de 1917'],
    'Constitucion de 1917': ['UAM-I'],

    #Linea 9
    'Pantitlan L9': ['Puebla', 'Pantitlan L1', 'Pantitlan L5', 'Pantitlan LA'],
    'Puebla': ['Pantitlan L9', 'Ciudad Deportiva'],
    'Ciudad Deportiva': ['Puebla', 'Velodromo'],
    'Velodromo': ['Ciudad Deportiva', 'Mixiuhca'],
    'Mixiuhca': ['Velodromo', 'Jamaica L9'],
    'Jamaica L9': ['Mixiuhca', 'Chabacano L9'],
    'Chabacano L9': ['Jamaica L9', 'Lazaro Cardenas', 'Chabacano L2', 'Chabacano L8'],
    'Lazaro Cardenas': ['Chabacano', 'Centro Medico L8'],
    'Centro Medico L8': ['Lazaro Cardenas', 'Chilpancingo', 'Centro Medico L3'],
    'Chilpancingo': ['Centro Medico L8', 'Patriotismo'],
    'Patriotismo': ['Chilpancingo', 'Tacubaya L9'],
    'Tacubaya L9': ['Patriotismo', 'Tacubaya L7', 'Tacubaya L1'],

    #Linea A
    'Pantitlan LA': ['Agricola Oriental', 'Pantitlan L1', 'Pantitlan L5', 'Pantitlan L9'],
    'Agricola Oriental': ['Pantitlan LA', 'Canal de San Juan'],
    'Canal de San Juan': ['Agricola Oriental', 'Tepalcates'],
    'Tepalcates': ['Canal de San Juan', 'Guelatao'],
    'Guelatao': ['Tepalcates', 'Peñón Viejo'],
    'Penon Viejo': ['Guelatao', 'Acatitla'],
    'Acatitla': ['Penon Viejo', 'Santa Marta'],
    'Santa Marta': ['Acatitla', 'Los Reyes'],
    'Los Reyes': ['Santa Marta', 'La Paz'],
    'La Paz': ['Los Reyes'],

    #Linea B
    'Buenavista': ['Guerrero LB'],
    'Guerrero LB': ['Buenavista', 'Garibaldi LB', 'Guerrero L3'],
    'Garibaldi LB': ['Guerrero LB', 'Lagunilla', 'Garibaldi L8'],
    'Lagunilla': ['Garibaldi LB', 'Tepito'],
    'Tepito': ['Lagunilla', 'Morelos LB'],
    'Morelos LB': ['Tepito', 'San Lazaro LB', 'Morelos L4'],
    'San Lazaro LB': ['Morelos LB', 'Ricardo Flores Magon', 'San Lazaro L1'],
    'Ricardo Flores Magon': ['San Lazaro LB', 'Romero Rubio'],
    'Romero Rubio': ['Ricardo Flores Magon', 'Oceania LB'],
    'Oceania LB': ['Romero Rubio', 'Deportivo Oceania', 'Oceania L5'],
    'Deportivo Oceania': ['Oceania LB', 'Villa de Aragón'],
    'Villa de Aragón': ['Deportivo Oceania', 'Nezahualcoyotl'],
    'Nezahualcoyotl': ['Villa de Aragón', 'Impulsora'],
    'Impulsora': ['Nezahualcoyotl', 'Rio de los Remedios'],
    'Rio de los Remedios': ['Impulsora', 'Muzquiz'],
    'Muzquiz': ['Rio de los Remedios', 'Ecatepec'],
    'Ecatepec': ['Muzquiz', 'Olimpica'],
    'Olimpica': ['Ecatepec', 'Plaza Aragon'],
    'Plaza Aragon': ['Olimpica', 'Ciudad Azteca'],
    'Ciudad Azteca': ['Plaza Aragon'],

    #Linea 12
    'Mixcoac L12': ['Insurgentes Sur', 'Mixcoac L7'],
    'Insurgentes Sur': ['Mixcoac L12', '20 de Noviembre'],
    '20 de Noviembre': ['Insurgentes Sur', 'Zapata L12'],
    'Zapata L12': ['20 de Noviembre', 'Parque de los Venados', 'Zapata L3'],
    'Parque de los Venados': ['Zapata L12', 'Eje Central'],
    'Eje Central': ['Parque de los Venados', 'Ermita L12'],
    'Ermita L12': ['Eje Central', 'Mexicaltzingo', 'Ermita L12'],
    'Mexicaltzingo': ['Ermita L2', 'Atlalilco L12'],
    'Atlalilco L12': ['Mexicaltzingo', 'Culhuacan', 'Atlalilco L8'],
    'Culhuacan': ['Atlalilco L12', 'San Andres Tomatlán'],
    'San Andres Tomatlan': ['Culhuacan', 'Lomas Estrella'],
    'Lomas Estrella': ['San Andres Tomatlan', 'Calle 11'],
    'Calle 11': ['Lomas Estrella', 'Periferico Oriente'],
    'Periferico Oriente': ['Calle 11', 'Tezonco'],
    'Tezonco': ['Periferico Oriente', 'Olivos'],
    'Olivos': ['Tezonco', 'Nopalera'],
    'Nopalera': ['Olivos', 'Zapotitlan'],
    'Zapotitlan': ['Nopalera', 'Tlaltenco'],
    'Tlaltenco': ['Zapotitlan', 'Tlahuac'],
    'Tlahuac': ['Tlaltenco']
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
inicio = 'Universidad'
destino = 'Buenavista'
ruta = encontrar_ruta(metro_cdmx, inicio, destino)

print("Ruta de {} a {}: {}".format(inicio, destino, ruta))