from dataclasses import dataclass
from typing import Dict, List, Set, Tuple, Optional
from datetime import datetime
import json
from collections import defaultdict, deque

def print_stations_by_line():
    """Imprime todas las estaciones organizadas por línea"""
    lineas = defaultdict(list)
    for estacion in metro_cdmx.keys():
        if ' L' in estacion:
            linea = 'L' + estacion.split(' L')[1]
            nombre_base = estacion.split(' L')[0]
            lineas[linea].append(nombre_base)
    
    print("\nEstaciones por línea:")
    for linea in sorted(lineas.keys()):
        print(f"\n{linea}:")
        for estacion in sorted(lineas[linea]):
            print(f"  - {estacion}")



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


# Definir las zonas y subzonas
zonas = {
    "Zona1": {
        "Subzona1": ["Ciudad_Azteca LB", "Plaza_Aragon LB", "Olimpica LB", "Ecatepec LB", "Muzquiz LB", "Rio_de_los_Remedios LB"],
        "Subzona2": ["Impulsora LB", "Nezahualcoyotl LB", "Villa_de_Aragon LB", "Bosque_de_Aragon LB", "Deportivo_Oceania LB", "Oceania L5"]
    },
    "Zona2": {
        "Subzona3": ["Martin_Carrera L6", "Martin_Carrera L4", "Talisman L4", "La_Villa L4"],
        "Subzona4": ["Bondojito L4", "Consulado L5", "Consulado L4", "Valle_Gomez L5", "Canal_del_Norte L4"],
        "Subzona5": ["Misterios L5", "Tlaltelolco L3", "La_Raza L3", "La_Raza L5", "Guerrero LB", "Guerrero L3"],
        "Subzona6": ["Politecnico L5", "Vallejo L6", "Instituto_del_Petroleo L6", "Instituto_del_Petroleo L5", "Autobuses_del_Norte L5", "Norte_45 L6"],
        "Subzona7": ["Indios_Verdes L3", "Deportivo_18_de_Marzo L3", "Deportivo_18_de_Marzo L6", "Lindavista L6", "Potrero L3"]
    },
    "Zona3": {
        "Subzona8": ["Oceania L5", "Oceania LB", "Eduardo_Molina L5", "Aragon L5", "Romero_Rubio LB", "Ricardo_Flores_Magon LB", "Aragon L5", "Deportivo_Oceania LB"],
        "Subzona9": ["Canal_del_Norte L4", "Morelos L4", "Morelos LB", "Tepito LB", "Merced L1", "Candelaria L1", "Candelaria L4", "San_Lazaro LB", "San_Lazaro L1", "Pino_Suarez L2"],
        "Subzona10": ["Moctezuma L1", "Balbuena L1", "Boulevard_Puerto_Aereo L1", "Terminal_Aerea L5", "Velodromo L9"],
        "Subzona11": ["La_Viga L8", "Jamaica L9", "Jamaica L4", "Mixiuhca L9", "Velodromo L9", "Santa_Anita L8", "Santa_Anita L4", "Chabacano L2", "Chabacano L9"],
        "Subzona12": ["Pantitlan L5", "Pantitlan L9", "Pantitlan L1", "Pantitlan LA", "Puebla L9", "Ciudad_deportiva L9", "Zaragoza L1", "Hangares L5", "Gomez_Farias L1", "Agricola_Oriental LA"]
    },
    "Zona4": {
        "Subzona13": ["Agricola_Oriental LA", "Canal_de_San_Juan LA", "Tepalcates LA", "Guelatao LA", "Pantitlan L1", "Pantitlan L5", "Pantitlan L9", "Pantitlan LA"],
        "Subzona14": ["Penon_Viejo LA", "Acatitla LA", "Santa_Marta LA", "Los_Reyes LA", "La_Paz LA"]
    },
    "Zona5": {
        "Subzona15": ["Coyuya L8", "Iztacalco L8", "Apatlalco L8", "Santa_Anita L4", "Santa_Anita L8"],
        "Subzona16": ["Aculco L8", "Escuadron_201 L8", "Atlalilco L12", "Atlalilco L8", "Iztapalapa L8", "Mexicaltzingo L12", "Ermita L2", "Ermita L12"],
        "Subzona17": ["Cerro_de_la_Estrella L8", "UAM-1 L8", "Constitucion_de_1917 L8"],
        "Subzona18": ["Culhuacan L12", "San_Andres_Tomatlan L12", "Lomas_Estrella L12", "Calle_11 L12"],
        "Subzona19": ["Periferico_Oriente L12", "Tezonco L12", "Olivos L12", "Nopalera L12", "Zapotitlan L12", "Tlaltenco L12", "Tlahuac L12"]
    },
    "Zona6": {
        "Subzona20": ["Division_del_Norte L3", "Zapata L3", "Zapata L12", "Parque_de_los_Venados L12", "Eje_Central L12", "Eugenia L3"],
        "Subzona21": ["Mixcoac L12", "Mixcoac L7", "Barranca_del_Muerto L7", "Hospital_20_de_Noviembre L12", "Insurgentes_Sur L12", "Coyoacan L3", "San_Antonio L7"],
        "Subzona22": ["Universidad L3", "Copilco L3", "Miguel_Angel_de_Quevedo L3", "Viveros L3"],
        "Subzona23": ["Nativitas L2", "Portales L2", "Ermita L12", "Ermita L2", "General_Anaya L2", "Tasquena L2", "Mexicaltzingo L12", "Villa_de_Cortes L2"]
    },

    "Zona7": {
        "Subzona24": ["Observatorio L1", "San_Antonio L1", "San_Pedro_de_los_Pinos L7", "Tacubaya L1", "Tacubaya L7", "Tacubaya L9", "Mixcoac L7", "Mixcoac L12"],
        "Subzona25": ["Patriotismo L9", "Chilpancingo L9", "Juancatlan L1", "Chapultepec L1", "Sevilla L1", "Insurgentes L1", "Cuauhtemoc L1", "Chilpancingo L9", "Centro_Medico L3", "Centro_Medico L9"],
        "Subzona26": ["San_Joaquin L7", "Polanco L7", "Auditorio L7", "Constituyentes L7", "Tacuba L7", "Tacuba L2"]
    },

    "Zona8": {
        "Subzona27": ["San_Cosme L2", "Normal L2", "Colegio_Militar L2", "Cuitlahuac L2", "Normal L2"],
        "Subzona28": ["Tacuba L2", "Tacuba L7", "Panteones L2", "Cuatro_Caminos L2", "Refineria L7", "San_Joaquin L7"],
        "Subzona29": ["Camarones L7", "El_Rosario L7", "Aquiles_Serdan L7", "El_Rosario L6", "Tezozomoc L6"],
        "Subzona30": ["Azcapotzalco L6", "Ferreria L6", "Norte_45 L6", "Vallejo L6"]
    },
    "Zona9": {
        "Subzona31": ["Eugenia L3", "Etiopia L3", "Viaducto L2", "Xola L2", "Villa_de_Cortes L2", "Nativitas L2", "Division_del_Norte L3"],
        "Subzona32": ["Centro_Medico L3", "Centro_Medico L9", "Lazaro_Cardenas L9", "Chabacano L2", "Chabacano L8", "Chabacano L8", "La_Viga L1"],
        "Subzona33": ["Hospital_General L3", "Obrera L8", "San_Antonio_Abdad L2", "Ninos_heroes L3", "Doctores L8"],
        "Subzona34": ["Cuathemoc L1", "Balderas L1", "Balderas L3", "Salto_del_Agua L2", "Salto_del_Agua L8", "Isabel_la_Catolica L1", "Pino_Suarez L1", "Pino_Suarez L2", "Merced L1"],
        "Subzona35": ["San_Juan_de_Letran L8", "Juarez L3", "Zocalo L2", "Allende L2", "Bellas_Artes L2", "Bellas_Artes L3"],
        "Subzona36": ["Hidalgo L2", "Hidalgo L3", "Revolucion L2", "San_Cosme L2", "Normal L2"],
        "Subzona37": ["Buenavista LB", "Guerrero L3", "Guerrero LB", "Garibaldi L8", "Garibaldi LB", "Lagunilla LB", "Tepito LB", "Tlaltelolco L3"]
    }
}

@dataclass
class Caso:
    """Representa un caso almacenado de una ruta"""
    origen: str
    destino: str
    ruta: List[str]
    transbordos: List[Tuple[str, str, str]]  # estación, de_línea, a_línea
    fecha_creacion: datetime
    contador_uso: int = 0
    calificacion_promedio: float = 0.0
    total_calificaciones: int = 0

@dataclass
class Estacion:
    """Representa una estación del metro con sus propiedades"""
    nombre: str
    lineas: List[str]
    conexiones: List[str]
    zona: str
    subzona: str
    es_transbordo: bool = False

class GestorEstaciones:
    """Gestiona la información y operaciones relacionadas con estaciones"""
    def __init__(self, metro_cdmx: dict, zonas: dict):
        self.estaciones: Dict[str, Estacion] = {}
        self.lineas: Dict[str, List[str]] = defaultdict(list)
        self.zonas = zonas
        self._procesar_datos_metro(metro_cdmx)

    def _procesar_datos_metro(self, metro_cdmx: dict):
        """Procesa los datos del metro en objetos Estacion estructurados"""
        for nombre_estacion, conexiones in metro_cdmx.items():
            nombre_base = nombre_estacion.split(' L')[0]
            linea = 'L' + nombre_estacion.split(' L')[1] if ' L' in nombre_estacion else None
            
            zona, subzona = self.encontrar_subzona(nombre_base)
            
            if nombre_base not in self.estaciones:
                self.estaciones[nombre_base] = Estacion(
                    nombre=nombre_base,
                    lineas=[],
                    conexiones=[],
                    zona=zona,
                    subzona=subzona
                )
            
            if linea:
                if linea not in self.estaciones[nombre_base].lineas:
                    self.estaciones[nombre_base].lineas.append(linea)
                self.lineas[linea].append(nombre_base)
            
            self.estaciones[nombre_base].conexiones.extend(
                [conn.split(' L')[0] for conn in conexiones]
            )
            self.estaciones[nombre_base].conexiones = list(set(
                self.estaciones[nombre_base].conexiones
            ))
        
        # Marcar estaciones de transbordo
        for estacion in self.estaciones.values():
            estacion.es_transbordo = len(estacion.lineas) > 1

    def encontrar_subzona(self, nombre_estacion: str) -> Tuple[str, str]:
        """Encuentra la zona y subzona de una estación"""
        for zona, subzonas in self.zonas.items():
            for subzona, estaciones in subzonas.items():
                if nombre_estacion in estaciones:
                    return zona, subzona
        return "Desconocida", "Desconocida"

    def obtener_transbordos_zona(self, zona: str) -> List[str]:
        """Encuentra estaciones de transbordo en una zona"""
        return [
            estacion.nombre for estacion in self.estaciones.values()
            if estacion.zona == zona and estacion.es_transbordo
        ]

    def imprimir_estaciones_por_linea(self):
        """Imprime todas las estaciones organizadas por línea"""
        for linea in sorted(self.lineas.keys()):
            print(f"\n{linea}:")
            for estacion in sorted(self.lineas[linea]):
                print(f"  - {estacion}")

class GestorRutas:
    """Gestiona la búsqueda y manejo de rutas"""
    def __init__(self, gestor_estaciones: GestorEstaciones):
        self.gestor_estaciones = gestor_estaciones

    def busqueda_intrazonal(self, origen: str, destino: str) -> Optional[List[str]]:
        """Búsqueda dentro de una misma zona"""
        cola = deque([(origen, [origen])])
        visitados = set()
        
        while cola:
            actual, ruta = cola.popleft()
            if actual == destino:
                return ruta
            
            for vecino in self.gestor_estaciones.estaciones[actual].conexiones:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, ruta + [vecino]))
        
        return None

    def busqueda_entre_zonas(self, origen: str, destino: str) -> Optional[List[str]]:
        """Búsqueda entre diferentes zonas"""
        estacion_origen = self.gestor_estaciones.estaciones[origen]
        estacion_destino = self.gestor_estaciones.estaciones[destino]
        
        transbordos_origen = self.gestor_estaciones.obtener_transbordos_zona(estacion_origen.zona)
        transbordos_destino = self.gestor_estaciones.obtener_transbordos_zona(estacion_destino.zona)
        
        mejor_ruta = None
        mejor_longitud = float('inf')
        
        for t_origen in transbordos_origen:
            for t_destino in transbordos_destino:
                ruta1 = self.busqueda_intrazonal(origen, t_origen)
                if not ruta1:
                    continue
                
                ruta2 = self.busqueda_intrazonal(t_origen, t_destino)
                if not ruta2:
                    continue
                
                ruta3 = self.busqueda_intrazonal(t_destino, destino)
                if not ruta3:
                    continue
                
                ruta_total = ruta1[:-1] + ruta2[:-1] + ruta3
                if len(ruta_total) < mejor_longitud:
                    mejor_ruta = ruta_total
                    mejor_longitud = len(ruta_total)
        
        return mejor_ruta

class GestorCasos:
    """Gestiona el almacenamiento y recuperación de casos"""
    def __init__(self):
        self.memoria_casos: Dict[str, Caso] = {}
        self.cargar_casos()

    def cargar_casos(self):
        """Carga casos desde almacenamiento persistente"""
        try:
            with open('casos_metro.json', 'r') as f:
                datos_casos = json.load(f)
                for clave_caso, datos in datos_casos.items():
                    # Convertir la fecha de string a datetime
                    datos['fecha_creacion'] = datetime.fromisoformat(datos['fecha_creacion'])
                    self.memoria_casos[clave_caso] = Caso(**datos)
        except FileNotFoundError:
            pass

    def guardar_casos(self):
        """Guarda casos en almacenamiento persistente"""
        datos_casos = {}
        for k, v in self.memoria_casos.items():
            # Crear un diccionario con los datos del caso
            datos_caso = {
                'origen': v.origen,
                'destino': v.destino,
                'ruta': v.ruta,
                'transbordos': v.transbordos,
                'fecha_creacion': v.fecha_creacion.isoformat(),  # Convertir datetime a string
                'contador_uso': v.contador_uso,
                'calificacion_promedio': v.calificacion_promedio,
                'total_calificaciones': v.total_calificaciones
            }
            datos_casos[k] = datos_caso
            
        with open('casos_metro.json', 'w') as f:
            json.dump(datos_casos, f, indent=2)

    def guardar_nuevo_caso(self, origen: str, destino: str, ruta: List[str], transbordos: List[Tuple[str, str, str]]):
        """Almacena un nuevo caso en la memoria"""
        caso = Caso(
            origen=origen,
            destino=destino,
            ruta=ruta,
            transbordos=transbordos,
            fecha_creacion=datetime.now()
        )
        self.memoria_casos[f"{origen}-{destino}"] = caso
        self.guardar_casos()

    def calificar_ruta(self, origen: str, destino: str, calificacion: int):
        """Permite calificar rutas para mejorar la calidad de los casos"""
        clave_caso = f"{origen}-{destino}"
        if clave_caso in self.memoria_casos:
            caso = self.memoria_casos[clave_caso]
            caso.total_calificaciones += 1
            caso.calificacion_promedio = (
                (caso.calificacion_promedio * (caso.total_calificaciones - 1)) + calificacion
            ) / caso.total_calificaciones
            self.guardar_casos()

class MetroRouterCDMX:
    def __init__(self, metro_cdmx: dict, zonas: dict):
        self.gestor_estaciones = GestorEstaciones(metro_cdmx, zonas)
        self.gestor_rutas = GestorRutas(self.gestor_estaciones)
        self.gestor_casos = GestorCasos()
        self.metro_cdmx = metro_cdmx
        
        # Pesos para estrategias de razonamiento
        self.peso_casos = 0.9
        self.peso_modelo = 0.1

    def _obtener_nombre_base(self, estacion: str) -> str:
        """Obtiene el nombre base de la estación sin el número de línea"""
        return estacion.split(' L')[0] if ' L' in estacion else estacion

    def encontrar_ruta(self, origen: str, destino: str) -> Optional[List[str]]:
        """Método principal que combina razonamiento basado en casos y modelos"""
        # Primero intentar con casos
        ruta_caso = self._buscar_ruta_por_casos(origen, destino)
        if ruta_caso and self._evaluar_calidad_ruta(ruta_caso) > 0.8:
            return ruta_caso
        
        # Si no hay caso adecuado, usar el modelo
        ruta_modelo = self._buscar_ruta_por_modelo(origen, destino)
        
        # Almacenar la nueva ruta como caso
        if ruta_modelo:
            transbordos = self._identificar_transbordos(ruta_modelo)
            self.gestor_casos.guardar_nuevo_caso(origen, destino, ruta_modelo, transbordos)
        
        return ruta_modelo

    def _buscar_ruta_por_casos(self, origen: str, destino: str) -> Optional[List[str]]:
        """
        Búsqueda usando razonamiento basado en casos
        1. Busca casos exactos
        2. Si no hay caso exacto, busca casos similares
        3. Adapta casos similares si es necesario
        """
        # 1. Búsqueda de caso exacto
        caso_exacto = self._buscar_caso_exacto(origen, destino)
        if caso_exacto:
            if caso_exacto.calificacion_promedio >= 4.0:
                caso_exacto.contador_uso += 1
                return caso_exacto.ruta
            elif caso_exacto.calificacion_promedio < 2.0:
                # Si el caso tiene mala calificación, mejor buscar alternativa
                return None

        # 2. Búsqueda de casos similares
        casos_similares = self._buscar_casos_similares(origen, destino)
        if casos_similares:
            # Intentar adaptar el mejor caso similar
            for caso in casos_similares:
                ruta_adaptada = self._adaptar_caso(caso, origen, destino)
                if ruta_adaptada:
                    return ruta_adaptada

        return None

    def _buscar_caso_exacto(self, origen: str, destino: str) -> Optional[Caso]:
        """Busca un caso que coincida exactamente con origen y destino"""
        clave_caso = f"{origen}-{destino}"
        return self.gestor_casos.memoria_casos.get(clave_caso)

    def _buscar_casos_similares(self, origen: str, destino: str) -> List[Caso]:
        """
        Busca casos similares basados en varios criterios:
        - Misma línea de metro
        - Zona geográfica similar
        - Distancia similar
        - Buenas calificaciones previas
        """
        casos_similares = []
        
        # Obtener información de las estaciones
        linea_origen = origen.split(' L')[1] if ' L' in origen else None
        linea_destino = destino.split(' L')[1] if ' L' in destino else None
        
        # Obtener zona de las estaciones
        zona_origen = self.gestor_estaciones.encontrar_subzona(self._obtener_nombre_base(origen))[0]
        zona_destino = self.gestor_estaciones.encontrar_subzona(self._obtener_nombre_base(destino))[0]

        for caso in self.gestor_casos.memoria_casos.values():
            similitud = 0.0
            
            # 1. Similitud de líneas (40% del peso)
            caso_linea_origen = caso.origen.split(' L')[1] if ' L' in caso.origen else None
            caso_linea_destino = caso.destino.split(' L')[1] if ' L' in caso.destino else None
            
            if linea_origen == caso_linea_origen:
                similitud += 0.2
            if linea_destino == caso_linea_destino:
                similitud += 0.2
                
            # 2. Similitud de zonas (30% del peso)
            caso_zona_origen = self.gestor_estaciones.encontrar_subzona(
                self._obtener_nombre_base(caso.origen))[0]
            caso_zona_destino = self.gestor_estaciones.encontrar_subzona(
                self._obtener_nombre_base(caso.destino))[0]
                
            if zona_origen == caso_zona_origen:
                similitud += 0.15
            if zona_destino == caso_zona_destino:
                similitud += 0.15
                
            # 3. Calificación del caso (20% del peso)
            if caso.total_calificaciones > 0:
                similitud += min(0.2, (caso.calificacion_promedio / 5.0) * 0.2)
            
            # 4. Frecuencia de uso (10% del peso)
            similitud += min(0.1, (caso.contador_uso / 100) * 0.1)
            
            # Agregar si la similitud es suficiente
            if similitud >= 0.6:  # Umbral de similitud
                casos_similares.append((similitud, caso))
        
        # Ordenar por similitud y retornar los casos
        return [caso for _, caso in sorted(casos_similares, 
                                        key=lambda x: x[0], 
                                        reverse=True)]

    def _adaptar_caso(self, caso: Caso, nuevo_origen: str, nuevo_destino: str) -> Optional[List[str]]:
        """
        Adapta un caso similar para resolver el nuevo problema
        Puede incluir:
        1. Extender la ruta
        2. Acortar la ruta
        3. Modificar transbordos
        """
        ruta_adaptada = []
        
        # Si el origen es diferente, encontrar conexión al caso original
        if nuevo_origen != caso.origen:
            ruta_inicio = self._buscar_ruta_por_modelo(nuevo_origen, caso.ruta[0])
            if ruta_inicio:
                ruta_adaptada.extend(ruta_inicio[:-1])
        
        # Agregar la ruta del caso
        ruta_adaptada.extend(caso.ruta)
        
        # Si el destino es diferente, encontrar conexión desde el caso
        if nuevo_destino != caso.destino:
            ruta_fin = self._buscar_ruta_por_modelo(caso.ruta[-1], nuevo_destino)
            if ruta_fin:
                ruta_adaptada.extend(ruta_fin[1:])
        
        # Verificar si la ruta adaptada es válida
        if ruta_adaptada:
            # Evaluar calidad de la adaptación
            calidad = self._evaluar_calidad_ruta(ruta_adaptada)
            if calidad >= 0.7:  # Umbral de calidad para adaptaciones
                return ruta_adaptada
        
        return None

    def _buscar_ruta_por_modelo(self, origen: str, destino: str) -> Optional[List[str]]:
        """Búsqueda usando el modelo jerárquico"""
        # Usar el diccionario metro_cdmx directamente para la búsqueda
        return self.bfs_encontrar_ruta(self.metro_cdmx, origen, destino)

    def bfs_encontrar_ruta(self, metro, inicio, destino):
        """Implementación de BFS para encontrar ruta"""
        visitados = set()
        cola = [(inicio, [inicio])]

        while cola:
            nodo_actual, ruta = cola.pop(0)

            if nodo_actual == destino:
                return ruta

            for vecino in metro.get(nodo_actual, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, ruta + [vecino]))

        return None

    def _identificar_transbordos(self, ruta: List[str]) -> List[Tuple[str, str, str]]:
        """Identifica puntos de transbordo en una ruta"""
        transbordos = []
        linea_actual = None
        
        for i in range(len(ruta) - 1):
            estacion = ruta[i]
            siguiente = ruta[i + 1]
            
            # Obtener la línea de cada estación
            linea_actual_str = estacion.split(' L')[-1] if ' L' in estacion else None
            linea_siguiente_str = siguiente.split(' L')[-1] if ' L' in siguiente else None
            
            if linea_actual_str and linea_siguiente_str and linea_actual_str != linea_siguiente_str:
                transbordos.append((estacion, f"L{linea_actual_str}", f"L{linea_siguiente_str}"))
        
        return transbordos

    def _evaluar_calidad_ruta(self, ruta: List[str]) -> float:
        """Evalúa la calidad de una ruta"""
        if not ruta:
            return 0.0
        
        transbordos = len(self._identificar_transbordos(ruta))
        penalizacion_transbordos = max(0, 1 - (transbordos * 0.2))
        
        penalizacion_longitud = max(0, 1 - (len(ruta) * 0.05))
        
        # Contar transbordos como estaciones que aparecen en múltiples líneas
        transbordos_principales = sum(
            1 for estacion in ruta 
            if ' L' in estacion
        )
        eficiencia_transbordos = min(1, transbordos_principales * 0.2)
        
        return (penalizacion_transbordos * 0.4 + penalizacion_longitud * 0.4 + eficiencia_transbordos * 0.2)
def main():
    router = MetroRouterCDMX(metro_cdmx, zonas)
    
    while True:
        print("\n=== Sistema de Rutas del Metro CDMX ===")
        print("1. Buscar ruta")
        print("2. Ver estaciones por línea")
        print("3. Calificar una ruta")
        print("4. Ver estadísticas de casos")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            print("\nEstaciones disponibles:")
            print_stations_by_line()
            
            print("\nIngrese la estación de origen (ejemplo: 'Universidad L3' o 'Pantitlan L1')")
            origen = input("Origen: ").strip()
            
            print("\nIngrese la estación de destino (ejemplo: 'Universidad L3' o 'Pantitlan L1')")
            destino = input("Destino: ").strip()
            
            try:
                ruta = router.encontrar_ruta(origen, destino)
                
                if ruta:
                    print(f"\nRuta encontrada de {origen} a {destino}:")
                    print(f"Estaciones: {' -> '.join(ruta)}")
                    transbordos = router._identificar_transbordos(ruta)
                    print(f"\nTiempo estimado: {len(ruta) * 3 + len(transbordos) * 5} minutos")
                    print(f"Número de estaciones: {len(ruta)}")
                    print(f"Número de transbordos: {len(transbordos)}")
                    
                    if transbordos:
                        print("\nTransbordos:")
                        for estacion, de_linea, a_linea in transbordos:
                            print(f"  - En {estacion}: cambiar de línea {de_linea} a línea {a_linea}")
                    
                    # Modificado para acceder a través de gestor_casos
                    clave_caso = f"{origen}-{destino}"
                    if clave_caso in router.gestor_casos.memoria_casos:
                        caso = router.gestor_casos.memoria_casos[clave_caso]
                        print(f"\nEsta ruta se ha usado {caso.contador_uso} veces")
                        if caso.total_calificaciones > 0:
                            print(f"Calificación promedio: {caso.calificacion_promedio:.1f}/5.0")
                    else:
                        print("\nEsta es una nueva ruta generada por el sistema")
                else:
                    print(f"\nNo se encontró ruta entre {origen} y {destino}")
                    
            except KeyError as e:
                print(f"\nError: Estación no encontrada: {e}")
            except Exception as e:
                print(f"\nError al buscar la ruta: {e}")
                
        elif opcion == "2":
            print_stations_by_line()
            
        elif opcion == "3":
            try:
                print("\nCalificar una ruta utilizada:")
                origen = input("Ingrese la estación de origen: ").strip()
                destino = input("Ingrese la estación de destino: ").strip()
                
                clave_caso = f"{origen}-{destino}"
                # Modificado para acceder a través de gestor_casos
                if clave_caso in router.gestor_casos.memoria_casos:
                    try:
                        calificacion = int(input("Califique la ruta (1-5): ").strip())
                        if 1 <= calificacion <= 5:
                            router.gestor_casos.calificar_ruta(origen, destino, calificacion)
                            print("¡Gracias por su calificación!")
                        else:
                            print("Error: La calificación debe estar entre 1 y 5")
                    except ValueError:
                        print("Error: Por favor ingrese un número válido")
                else:
                    print("No se encontró un caso guardado para esta ruta")
            except Exception as e:
                print(f"Error al calificar la ruta: {e}")
                
        elif opcion == "4":
            try:
                print("\nEstadísticas de casos almacenados:")
                # Modificado para acceder a través de gestor_casos
                if router.gestor_casos.memoria_casos:
                    print(f"\nTotal de casos almacenados: {len(router.gestor_casos.memoria_casos)}")
                    casos_usados = sum(1 for caso in router.gestor_casos.memoria_casos.values() 
                                     if caso.contador_uso > 0)
                    print(f"Casos utilizados: {casos_usados}")
                    
                    # Mostrar los casos más utilizados
                    casos_ordenados = sorted(
                        router.gestor_casos.memoria_casos.values(),
                        key=lambda x: x.contador_uso,
                        reverse=True
                    )[:5]
                    
                    if casos_ordenados:
                        print("\nRutas más utilizadas:")
                        for caso in casos_ordenados:
                            print(f"  - {caso.origen} → {caso.destino}: {caso.contador_uso} veces")
                            if caso.total_calificaciones > 0:
                                print(f"    Calificación: {caso.calificacion_promedio:.1f}/5.0")
                else:
                    print("No hay casos almacenados todavía")
            except Exception as e:
                print(f"Error al mostrar estadísticas: {e}")
                
        elif opcion == "5":
            print("\n¡Gracias por usar el Sistema de Rutas del Metro CDMX!")
            break
            
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()