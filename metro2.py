from dataclasses import dataclass

from typing import Dict, List, Set, Tuple, Optional
from datetime import datetime, time
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque


# Metro network data for Mexico City

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