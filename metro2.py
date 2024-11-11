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

@dataclass
class Station:
    name: str
    lines: List[str]
    connections: List[str]
    is_transfer: bool = False

@dataclass
class Route:
    stations: List[str]
    total_time: int  # in minutes
    transfers: List[Tuple[str, str, str]]  # (station, from_line, to_line)
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
        station = self.stations.get(station_name.split(' L')[0])
        return station.lines if station else []

    def get_connecting_line(self, station1: str, station2: str) -> str:
        """Determine which line connects two adjacent stations"""
        station1_lines = set(self.get_station_lines(station1))
        station2_lines = set(self.get_station_lines(station2))
        common_lines = station1_lines.intersection(station2_lines)
        return list(common_lines)[0] if common_lines else None



class MetroVisualizer:
    def __init__(self, metro_system: MetroSystem):
        self.metro_system = metro_system
        self.G = nx.Graph()
        self._build_graph()
        self.pos = nx.spring_layout(self.G, k=1, iterations=50)

    def _build_graph(self):
        """Build NetworkX graph from metro system"""
        # Add stations
        for station_name, station in self.metro_system.stations.items():
            self.G.add_node(station_name, 
                          lines=station.lines,
                          is_transfer=station.is_transfer)
            
            # Add connections
            for connection in station.connections:
                self.G.add_edge(station_name, connection)

    def visualize_route(self, route: Route):
        plt.figure(figsize=(15, 10))
        
        # Draw base network
        nx.draw_networkx_edges(self.G, self.pos, 
                             edge_color='lightgray',
                             alpha=0.5)
        
        # Draw stations
        nx.draw_networkx_nodes(self.G, self.pos,
                             node_color='lightgray',
                             alpha=0.5,
                             node_size=100)
        
        # Highlight route
        route_edges = list(zip(route.stations[:-1], route.stations[1:]))
        for i, (start, end) in enumerate(route_edges):
            color = self._get_line_color(route.line_sequence[i])
            nx.draw_networkx_edges(self.G, self.pos,
                                 edgelist=[(start, end)],
                                 edge_color=color,
                                 width=2)
        
        # Highlight transfers
        transfer_stations = [t[0] for t in route.transfers]
        if transfer_stations:
            nx.draw_networkx_nodes(self.G, self.pos,
                                 nodelist=transfer_stations,
                                 node_color='red',
                                 node_size=150)
        
        # Highlight start/end
        nx.draw_networkx_nodes(self.G, self.pos,
                             nodelist=[route.stations[0]],
                             node_color='green',
                             node_size=200)
        nx.draw_networkx_nodes(self.G, self.pos,
                             nodelist=[route.stations[-1]],
                             node_color='blue',
                             node_size=200)
        
        # Add labels for route stations
        labels = {station: station for station in route.stations}
        nx.draw_networkx_labels(self.G, self.pos, labels, font_size=8)
        
        plt.title(f"Route from {route.stations[0]} to {route.stations[-1]}\n"
                 f"Total time: {route.total_time} minutes, "
                 f"Transfers: {len(route.transfers)}")
        plt.axis('off')
        plt.show()

    def _get_line_color(self, line: str) -> str:
        """Return color for each metro line"""
        color_map = {
            'L1': '#FF1493',  # Rosa
            'L2': '#0000FF',  # Azul
            'L3': '#008000',  # Verde
            'L4': '#87CEEB',  # Celeste
            'L5': '#FFD700',  # Amarillo
            'L6': '#FF0000',  # Rojo
            'L7': '#FFA500',  # Naranja
            'L8': '#90EE90',  # Verde claro
            'L9': '#800080',  # Café
            'LA': '#800080',  # Morado
            'LB': '#808080',  # Gris
            'L12': '#B8860B', # Dorado
        }
        return color_map.get(line, '#000000')
    
class MexicoCityMetroRouter:
    def __init__(self, metro_cdmx: dict):
        self.metro_system = MetroSystem(metro_cdmx)
        self.visualizer = MetroVisualizer(self.metro_system)
        
    def find_route(self, start: str, end: str) -> Optional[Route]:
        """Find a route between two stations"""
        path = encontrar_ruta(metro_cdmx, start, end)
        if not path:
            return None

        # Get line sequence
        line_sequence = []
        transfers = []
        current_line = None

        for i in range(len(path) - 1):
            line = self.metro_system.get_connecting_line(path[i], path[i + 1])
            if line:  # Only add line if it's valid
                if line != current_line and current_line is not None:
                    transfers.append((path[i], current_line, line))
                current_line = line
                line_sequence.append(line)

        return Route(
            stations=path,
            total_time=self._estimate_time(path, transfers),
            transfers=transfers,
            line_sequence=line_sequence
        )

    def _estimate_time(self, path: List[str], transfers: List[Tuple[str, str, str]]) -> int:
        """Estimate travel time based on number of stations and transfers"""
        return len(path) * 3 + len(transfers) * 5  # 3 min per station, 5 min per transfer

    def visualize_route(self, route: Route):
        """Delegate visualization to the visualizer"""
        self.visualizer.visualize_route(route)

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

# Example usage
router = MexicoCityMetroRouter(metro_cdmx)

# Test the router
start_station = "Universidad"
end_station = "Pantitlan L1"

route = router.find_route(start_station, end_station)
if route:
    print(f"\nRoute found from {start_station} to {end_station}:")
    print(f"Stations: {' -> '.join(route.stations)}")
    print(f"Total time: {route.total_time} minutes")
    print(f"Number of transfers: {len(route.transfers)}")
    print("Transfers:", route.transfers)
    
    # Visualize the route using the router's visualize_route method
    router.visualize_route(route)
else:
    print(f"No route found between {start_station} and {end_station}")