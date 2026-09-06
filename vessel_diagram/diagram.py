"""
Main vessel diagram generator class
"""

from typing import List, Tuple, Optional, Dict
from .equipment import Equipment, EquipmentType
from .renderer import SVGRenderer, PDFRenderer

class VesselDiagram:
    """Generate vessel setup diagrams from equipment data"""
    
    def __init__(self, 
                 vessel_name: str = "Survey Vessel",
                 length: float = 12.0,
                 beam: float = 8.0,
                 draft: float = 1.5):
        """
        Initialize vessel diagram
        
        Args:
            vessel_name: Name of the vessel
            length: Length of vessel in meters (LOA)
            beam: Beam (width) of vessel in meters
            draft: Draft of vessel in meters
        """
        self.vessel_name = vessel_name
        self.length = length
        self.beam = beam
        self.draft = draft
        self.equipment: List[Equipment] = []
        self.cable_routes: List[Dict] = []
        self.metadata = {}
    
    def add_equipment(self, 
                     name: str, 
                     position: Tuple[float, float],
                     equipment_type: str,
                     size: Tuple[float, float] = (0.5, 0.5),
                     height_above_deck: float = 0.0,
                     notes: str = ""):
        """
        Add equipment to vessel diagram
        
        Args:
            name: Equipment name
            position: (x, y) coordinates in meters
            equipment_type: Type of equipment (string key)
            size: (width, height) in meters
            height_above_deck: Height above deck in meters
            notes: Equipment notes/description
        """
        # Convert string to EquipmentType
        try:
            eq_type = EquipmentType[equipment_type.upper()]
        except KeyError:
            eq_type = EquipmentType.OTHER
        
        equipment = Equipment(
            name=name,
            equipment_type=eq_type,
            position=position,
            size=size,
            height_above_deck=height_above_deck,
            notes=notes
        )
        
        self.equipment.append(equipment)
        return equipment
    
    def add_cable_route(self,
                       from_equipment: str,
                       to_equipment: str,
                       cable_type: str = "Ethernet",
                       color: str = "#000000"):
        """
        Add cable connection between equipment
        
        Args:
            from_equipment: Source equipment name
            to_equipment: Destination equipment name
            cable_type: Type of cable (Ethernet, Power, etc.)
            color: Cable color in hex
        """
        self.cable_routes.append({
            'from': from_equipment,
            'to': to_equipment,
            'type': cable_type,
            'color': color
        })
    
    def add_metadata(self, key: str, value: any):
        """Add metadata to diagram"""
        self.metadata[key] = value
    
    def get_equipment_by_name(self, name: str) -> Optional[Equipment]:
        """Find equipment by name"""
        for eq in self.equipment:
            if eq.name == name:
                return eq
        return None
    
    def validate_positions(self) -> List[str]:
        """
        Validate equipment positions are within vessel bounds
        
        Returns:
            List of validation warnings/errors
        """
        warnings = []
        for eq in self.equipment:
            x, y = eq.position
            w, h = eq.size
            
            # Check bounds
            if x - w/2 < 0 or x + w/2 > self.length:
                warnings.append(f"{eq.name}: X position exceeds vessel length")
            
            if y - h/2 < 0 or y + h/2 > self.beam:
                warnings.append(f"{eq.name}: Y position exceeds vessel beam")
        
        return warnings
    
    def save_svg(self, filepath: str, scale: float = 50.0):
        """
        Save diagram as SVG
        
        Args:
            filepath: Output file path
            scale: Scale factor (pixels per meter)
        """
        renderer = SVGRenderer(self, scale)
        renderer.render()
        renderer.save(filepath)
    
    def save_pdf(self, filepath: str, scale: float = 50.0):
        """
        Save diagram as PDF
        
        Args:
            filepath: Output file path
            scale: Scale factor (pixels per cm)
        """
        renderer = PDFRenderer(self, scale)
        renderer.render()
        renderer.save(filepath)
    
    def get_equipment_summary(self) -> str:
        """Get text summary of all equipment"""
        summary = f"Vessel: {self.vessel_name}\n"
        summary += f"Dimensions: {self.length}m (L) x {self.beam}m (B) x {self.draft}m (D)\n"
        summary += f"\nEquipment ({len(self.equipment)} items):\n"
        summary += "-" * 60 + "\n"
        
        for i, eq in enumerate(self.equipment, 1):
            summary += f"{i}. {eq.name}\n"
            summary += f"   Type: {eq.equipment_type.value}\n"
            summary += f"   Position: ({eq.position[0]:.2f}, {eq.position[1]:.2f})m\n"
            summary += f"   Size: {eq.size[0]:.2f} x {eq.size[1]:.2f}m\n"
            if eq.height_above_deck > 0:
                summary += f"   Height: {eq.height_above_deck:.2f}m above deck\n"
            if eq.notes:
                summary += f"   Notes: {eq.notes}\n"
            summary += "\n"
        
        return summary
    
    def __repr__(self) -> str:
        return f"VesselDiagram('{self.vessel_name}', {len(self.equipment)} equipment)"
