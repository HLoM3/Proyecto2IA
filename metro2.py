from dataclasses import dataclass

from typing import Dict, List, Set, Tuple, Optional
from datetime import datetime, time
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque


# Metro network data for Mexico City

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


@dataclass
class Station:
    name: str
    lines: List[str]
    connections: List[str]
    is_transfer: bool = False

@dataclass
class Route:
    stations: List[str]
    total_time: int
    transfers: List[Tuple[str, str, str]]
    line_sequence: List[str]

class MetroSystem:
    def __init__(self, metro_data: dict):
        self.stations: Dict[str, Station] = {}
        self.lines: Dict[str, List[str]] = defaultdict(list)
        self._process_metro_data(metro_data)

    def _process_metro_data(self, metro_data: dict):
        """Process the metro_cdmx data into structured station and line information"""
        # Process stations and identify lines
        for station_name, connections in metro_data.items():
            # Extract line information from station name
            base_name = station_name.split(' L')[0]
            line = 'L' + station_name.split(' L')[-1] if ' L' in station_name else None
            
            # Get or create station
            if base_name not in self.stations:
                self.stations[base_name] = Station(
                    name=base_name,
                    lines=[],
                    connections=[]
                )
            
            # Add line if present
            if line:
                if line not in self.stations[base_name].lines:
                    self.stations[base_name].lines.append(line)
                self.lines[line].append(base_name)
            
            # Add connections
            self.stations[base_name].connections.extend(
                [conn.split(' L')[0] for conn in connections]
            )
            
            # Remove duplicates in connections
            self.stations[base_name].connections = list(set(
                self.stations[base_name].connections
            ))
            
        # Mark transfer stations
        for station in self.stations.values():
            station.is_transfer = len(station.lines) > 1

    def get_station_lines(self, station_name: str) -> List[str]:
        """Get all lines that serve a station"""
        base_name = station_name.split(' L')[0]
        station = self.stations.get(base_name)
        return station.lines if station else []

    def get_connecting_line(self, station1: str, station2: str) -> str:
        """Determine which line connects two adjacent stations"""
        station1_base = station1.split(' L')[0]
        station2_base = station2.split(' L')[0]
        
        station1_lines = set(self.get_station_lines(station1_base))
        station2_lines = set(self.get_station_lines(station2_base))
        common_lines = station1_lines.intersection(station2_lines)
        return list(common_lines)[0] if common_lines else 'L1'

class MexicoCityMetroRouter:
    def __init__(self, metro_cdmx: dict):
        self.metro_system = MetroSystem(metro_cdmx)
        
    def find_route(self, start: str, end: str) -> Optional[Route]:
        """Find a route between two stations"""
        path = encontrar_ruta(metro_cdmx, start, end)
        if not path:
            return None

        line_sequence = []
        transfers = []
        current_line = None

        for i in range(len(path) - 1):
            current_station = path[i]
            next_station = path[i + 1]
            
            line = self.metro_system.get_connecting_line(current_station, next_station)
            line_sequence.append(line)
            
            if current_line is not None and line != current_line:
                transfers.append((current_station, current_line, line))
            
            current_line = line

        return Route(
            stations=path,
            total_time=self._estimate_time(path, transfers),
            transfers=transfers,
            line_sequence=line_sequence
        )

    def _estimate_time(self, path: List[str], transfers: List[Tuple[str, str, str]]) -> int:
        """Estimate travel time based on number of stations and transfers"""
        return len(path) * 3 + len(transfers) * 5  # 3 min per station, 5 min per transfer

    def get_available_stations(self) -> List[str]:
        """Get list of all available stations"""
        return sorted(list(metro_cdmx.keys()))

def encontrar_ruta(metro, inicio, destino):
    queue = [(inicio, [inicio])]
    visitados = set()

    while queue:
        estacion_actual, ruta = queue.pop(0)
        if estacion_actual == destino:
            return ruta
        visitados.add(estacion_actual)

        for vecino in metro.get(estacion_actual, []):
            if vecino not in visitados:
                queue.append((vecino, ruta + [vecino]))

    return None

def print_stations_by_line():
    """Print all stations organized by line"""
    lines = defaultdict(list)
    for station in metro_cdmx.keys():
        if ' L' in station:
            line = 'L' + station.split(' L')[1]
            base_name = station.split(' L')[0]
            lines[line].append(base_name)
    
    print("\nEstaciones por línea:")
    for line in sorted(lines.keys()):
        print(f"\n{line}:")
        for station in sorted(lines[line]):
            print(f"  - {station}")


# Definir las zonas y subzonas
zonas = {
    "Zona1": {
        "Subzona1": ["Ciudad_Azteca LB", "Plaza_Aragon LB", "Olimpica LB", "Ecatepec LB", "Muzquiz LB",
                     "Rio_de_los_Remedios LB"],
        "Subzona2": ["Impulsora LB", "Nezahualcoyotl LB", "Villa_de_Aragon LB", "Bosque_de_Aragon LB",
                     "Deportivo_Oceania LB"]
    },
    "Zona2": {
        "Subzona1": ["Martin_Carrera L6", "Martin_Carrera L4", "Talisman L4", "La_Villa L4"],
        "Subzona2": ["Bondojito L4", "Consulado L5", "Consulado L4", "Valle_Gomez L5"],
        "Subzona3": ["Misterios L5", "Tlaltelolco L3", "La_Raza L3", "La_Raza L5"],
        "Subzona4": ["Politecnico L5", "Vallejo L6", "Instituto_del_Petroleo L6", "Instituto_del_Petroleo L5",
                     "Autobuses_del_Norte L5"],
        "Subzona5": ["Indios_Verdes L3", "Deportivo_18_de_Marzo L3", "Deportivo_18_de_Marzo L6", "Lindavista L6",
                     "Potrero L3"]
    },
    "Zona3": {
        "Subzona1": ["Oceania L5", "Oceania LB", "Eduardo_Molina L5", "Aragon L5", "Romero_Rubio LB",
                     "Ricardo_Flores_Magon LB"],
        "Subzona2": ["Canal_del_Norte L4", "Morelos L4", "Morelos LB", "Tepito LB", "Merced L1", "Candelaria L1",
                     "Candelaria L4", "San_Lazaro LB", "San_Lazaro L1"],
        "Subzona3": ["Moctezuma L1", "Balbuena L1", "Boulevard_Puerto_Aereo L1", "Terminal_Aerea L5", "Velodromo L9"],
        "Subzona4": ["La_Viga L8", "Jamaica L9", "Jamaica L4", "Mixiuhca L9", "Velodromo L9", "Santa_Anita L8",
                     "Santa_Anita L4"],
        "Subzona5": ["Pantitlan L5", "Pantitlan L9", "Pantitlan L1", "Pantitlan LA", "Puebla L9", "Ciudad_deportiva L9",
                     "Zaragoza L1", "Hangares L5", "Gomez_Farias L1"]
    },
    "Zona4": {
        "Subzona1": ["Agricola_Oriental LA", "Canal_de_San_Juan LA", "Tepalcates LA", "Guelatao LA"],
        "Subzona2": ["Penon_Viejo LA", "Acatitla LA", "Santa_Marta LA", "Los_Reyes LA", "La_Paz LA"]
    },
    "Zona5": {
        "Subzona1": ["Coyuya L8", "Iztacalco L8", "Apatlalco L8"],
        "Subzona2": ["Aculco L8", "Escuadron_201 L8", "Atlalilco L12", "Atlalilco L8", "Iztapalapa L8",
                     "Mexicaltzingo L12"],
        "Subzona3": ["Cerro_de_la_Estrella L8", "UAM-1 L8", "Constitucion_de_1917 L8"],
        "Subzona4": ["Culhuacan L12", "San_Andres_Tomatlan L12", "Lomas_Estrella L12", "Calle_11 L12"],
        "Subzona5": ["Periferico_Oriente L12", "Tezonco L12", "Olivos L12", "Nopalera L12", "Zapotitlan L12",
                     "Tlaltenco L12", "Tlahuac L12"]
    },
    "Zona6": {
        "Subzona1": ["Division_del_Norte L3", "Zapata L3", "Zapata L12", "Parque_de_los_Venados L12",
                     "Eje_Central L12"],
        "Subzona2": ["Mixcoac L12", "Mixcoac L7", "Barranca_del_Muerto L7", "Hospital_20_de_Noviembre L12",
                     "Insurgentes_Sur L12", "Coyoacan L3"],
        "Subzona3": ["Universidad L3", "Copilco L3", "Miguel_Angel_de_Quevedo L3", "Viveros L3"],
        "Subzona4": ["Nativitas L2", "Portales L2", "Ermita L12", "Ermita L2", "General_Anaya L2", "Tasquena L2"]
    },

}


# Función para encontrar la zona y subzona de una estación
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


def main():
    router = MexicoCityMetroRouter(metro_cdmx)
    
    while True:
        print("\n=== Sistema de Rutas del Metro CDMX ===")
        print("1. Buscar ruta")
        print("2. Ver estaciones por línea")
        print("3. Salir")
        
        choice = input("\nSeleccione una opción (1-3): ")
        
        if choice == "1":
            print("\nEstaciones disponibles:")
            print_stations_by_line()
            
            print("\nIngrese la estación de origen (ejemplo: 'Universidad' o 'Pantitlan L1')")
            start = input("Origen: ").strip()
            
            print("\nIngrese la estación de destino (ejemplo: 'Universidad' o 'Pantitlan L1')")
            end = input("Destino: ").strip()
            
            route = router.find_route(start, end)
            
            if route:
                print(f"\nRuta encontrada de {start} a {end}:")
                print(f"Estaciones: {' -> '.join(route.stations)}")
                print(f"Tiempo total estimado: {route.total_time} minutos")
                print(f"Número de transbordos: {len(route.transfers)}")
                if route.transfers:
                    print("\nTransbordos:")
                    for station, from_line, to_line in route.transfers:
                        print(f"  - En {station}: cambiar de línea {from_line} a línea {to_line}")
            else:
                print(f"\nNo se encontró ruta entre {start} y {end}")
                
        elif choice == "2":
            print_stations_by_line()
            
        elif choice == "3":
            print("\n¡Gracias por usar el Sistema de Rutas del Metro CDMX!")
            break
            
        else:
            print("\nOpción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()