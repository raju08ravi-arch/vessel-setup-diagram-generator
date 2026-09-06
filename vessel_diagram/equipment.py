"""
Equipment definitions for vessel setup diagrams
"""

from enum import Enum
from dataclasses import dataclass
from typing import Tuple, Optional

class EquipmentType(Enum):
    """Equipment type categories"""
    GYROSCOPE = "gyroscope"
    SONAR = "sonar"
    ANTENNA = "antenna"
    COMPUTER = "computer"
    POWER = "power"
    NETWORK = "network"
    STORAGE = "storage"
    OTHER = "other"

@dataclass
class Equipment:
    """Equipment on vessel"""
    name: str
    equipment_type: EquipmentType
    position: Tuple[float, float]  # (x, y) coordinates in meters
    size: Tuple[float, float] = (0.5, 0.5)  # (width, height) in meters
    color: str = "#3498db"
    rotation: float = 0.0  # degrees
    icon: Optional[str] = None
    
    # Equipment-specific properties
    height_above_deck: float = 0.0  # meters
    cable_connections: list = None
    notes: str = ""
    
    def __post_init__(self):
        if self.cable_connections is None:
            self.cable_connections = []
    
    def get_color(self) -> str:
        """Get equipment color based on type"""
        colors = {
            EquipmentType.GYROSCOPE: "#e74c3c",      # Red
            EquipmentType.SONAR: "#3498db",           # Blue
            EquipmentType.ANTENNA: "#f39c12",         # Orange
            EquipmentType.COMPUTER: "#2ecc71",        # Green
            EquipmentType.POWER: "#9b59b6",           # Purple
            EquipmentType.NETWORK: "#1abc9c",         # Turquoise
            EquipmentType.STORAGE: "#95a5a6",         # Gray
            EquipmentType.OTHER: "#34495e",           # Dark Blue
        }
        return colors.get(self.equipment_type, self.color)
    
    def connect_to(self, other_equipment: 'Equipment'):
        """Add cable connection to another equipment"""
        self.cable_connections.append({
            'to': other_equipment.name,
            'type': 'cable'
        })

class VesselEquipment:
    """Pre-defined equipment configurations"""
    
    # Navigation & Positioning
    OCTANS = {
        'name': 'Octans',
        'type': EquipmentType.GYROSCOPE,
        'size': (0.4, 0.4),
        'notes': 'Attitude/Heading sensor'
    }
    
    MULTIBEAM = {
        'name': 'Multibeam Sonar',
        'type': EquipmentType.SONAR,
        'size': (0.6, 0.8),
        'notes': 'Multi-beam echo sounder'
    }
    
    TRIMBLE_MPS = {
        'name': 'Trimble MPS',
        'type': EquipmentType.ANTENNA,
        'size': (0.3, 0.3),
        'notes': 'Multi-band Positioning System'
    }
    
    GPS_ANTENNA_1 = {
        'name': 'GPS Antenna 1 (Primary)',
        'type': EquipmentType.ANTENNA,
        'size': (0.25, 0.25),
        'notes': 'Primary GPS receiver'
    }
    
    GPS_ANTENNA_2 = {
        'name': 'GPS Antenna 2 (Secondary)',
        'type': EquipmentType.ANTENNA,
        'size': (0.25, 0.25),
        'notes': 'Secondary GPS receiver'
    }
    
    TIDE_ANTENNA = {
        'name': 'Differential GNSS Antenna (Tide)',
        'type': EquipmentType.ANTENNA,
        'size': (0.2, 0.2),
        'notes': 'Tide/RTK correction antenna'
    }
    
    COMPUTER = {
        'name': 'Survey Computer',
        'type': EquipmentType.COMPUTER,
        'size': (0.4, 0.3),
        'notes': 'Data acquisition & processing'
    }
    
    POWER_SUPPLY = {
        'name': 'Power Supply & UPS',
        'type': EquipmentType.POWER,
        'size': (0.5, 0.4),
        'notes': 'Backup power system'
    }
    
    NETWORK_SWITCH = {
        'name': 'Network Switch',
        'type': EquipmentType.NETWORK,
        'size': (0.3, 0.3),
        'notes': 'Data network hub'
    }
    
    DATA_STORAGE = {
        'name': 'Data Storage',
        'type': EquipmentType.STORAGE,
        'size': (0.3, 0.4),
        'notes': 'External drive/NAS'
    }
