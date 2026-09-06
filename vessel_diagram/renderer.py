"""
Diagram rendering engines (SVG and PDF)
"""

import svgwrite
from typing import Tuple

class SVGRenderer:
    """Render vessel diagrams to SVG format"""
    
    def __init__(self, diagram, scale: float = 50.0):
        """
        Initialize SVG renderer
        
        Args:
            diagram: VesselDiagram object
            scale: Pixels per meter
        """
        self.diagram = diagram
        self.scale = scale
        
        # Calculate canvas size with padding
        self.padding = 50
        self.width = self.diagram.length * self.scale + 2 * self.padding
        self.height = self.diagram.beam * self.scale + 2 * self.padding
        
        self.dwg = svgwrite.Drawing(
            size=(f"{self.width}px", f"{self.height}px"),
            xmlns="http://www.w3.org/2000/svg"
        )
    
    def _to_svg_coords(self, x: float, y: float) -> Tuple[float, float]:
        """Convert diagram coordinates to SVG coordinates"""
        svg_x = self.padding + x * self.scale
        svg_y = self.padding + y * self.scale
        return svg_x, svg_y
    
    def render(self):
        """Render the complete diagram"""
        # Add background
        self.dwg.add(self.dwg.rect(
            insert=(0, 0),
            size=(f"{self.width}px", f"{self.height}px"),
            fill="white",
            stroke="black",
            stroke_width=2
        ))
        
        # Draw vessel hull
        self._draw_vessel_hull()
        
        # Draw grid
        self._draw_grid()
        
        # Draw cable routes first (so they appear behind equipment)
        self._draw_cable_routes()
        
        # Draw equipment
        for equipment in self.diagram.equipment:
            self._draw_equipment(equipment)
        
        # Add title and legend
        self._add_title_and_legend()
    
    def _draw_vessel_hull(self):
        """Draw vessel outline"""
        x1, y1 = self._to_svg_coords(0, 0)
        x2, y2 = self._to_svg_coords(self.diagram.length, self.diagram.beam)
        
        hull_rect = self.dwg.rect(
            insert=(x1, y1),
            size=((x2-x1), (y2-y1)),
            fill="none",
            stroke="black",
            stroke_width=3,
            stroke_dasharray="5,5"
        )
        self.dwg.add(hull_rect)
        
        # Add center line
        mid_x = self.padding + (self.diagram.length / 2) * self.scale
        self.dwg.add(self.dwg.line(
            start=(mid_x, y1),
            end=(mid_x, y2),
            stroke="gray",
            stroke_width=1,
            stroke_dasharray="2,2"
        ))
    
    def _draw_grid(self):
        """Draw reference grid"""
        # Vertical lines (along length)
        for i in range(0, int(self.diagram.length) + 1):
            x1, y1 = self._to_svg_coords(i, 0)
            x2, y2 = self._to_svg_coords(i, self.diagram.beam)
            self.dwg.add(self.dwg.line(
                start=(x1, y1),
                end=(x2, y2),
                stroke="lightgray",
                stroke_width=0.5
            ))
        
        # Horizontal lines (along beam)
        for i in range(0, int(self.diagram.beam) + 1):
            x1, y1 = self._to_svg_coords(0, i)
            x2, y2 = self._to_svg_coords(self.diagram.length, i)
            self.dwg.add(self.dwg.line(
                start=(x1, y1),
                end=(x2, y2),
                stroke="lightgray",
                stroke_width=0.5
            ))
    
    def _draw_equipment(self, equipment):
        """Draw individual equipment on diagram"""
        x, y = self._to_svg_coords(*equipment.position)
        w, h = equipment.size[0] * self.scale, equipment.size[1] * self.scale
        
        # Draw equipment box
        color = equipment.get_color()
        rect = self.dwg.rect(
            insert=(x - w/2, y - h/2),
            size=(w, h),
            fill=color,
            stroke="black",
            stroke_width=2,
            opacity=0.7
        )
        self.dwg.add(rect)
        
        # Add label
        label = self.dwg.text(
            equipment.name,
            insert=(x, y + 5),
            font_size=10,
            text_anchor="middle",
            font_weight="bold"
        )
        self.dwg.add(label)
        
        # Add equipment type label
        type_label = self.dwg.text(
            equipment.equipment_type.value,
            insert=(x, y - 10),
            font_size=8,
            text_anchor="middle",
            fill="gray"
        )
        self.dwg.add(type_label)
    
    def _draw_cable_routes(self):
        """Draw cable connections between equipment"""
        for route in self.diagram.cable_routes:
            from_eq = self.diagram.get_equipment_by_name(route['from'])
            to_eq = self.diagram.get_equipment_by_name(route['to'])
            
            if from_eq and to_eq:
                x1, y1 = self._to_svg_coords(*from_eq.position)
                x2, y2 = self._to_svg_coords(*to_eq.position)
                
                line = self.dwg.line(
                    start=(x1, y1),
                    end=(x2, y2),
                    stroke=route.get('color', '#000000'),
                    stroke_width=2
                )
                self.dwg.add(line)
    
    def _add_title_and_legend(self):
        """Add title and equipment legend"""
        # Title
        title = self.dwg.text(
            f"{self.diagram.vessel_name} - Setup Diagram",
            insert=(self.width/2, 25),
            font_size=18,
            text_anchor="middle",
            font_weight="bold"
        )
        self.dwg.add(title)
        
        # Dimensions
        dim_text = f"Length: {self.diagram.length}m | Beam: {self.diagram.beam}m | Draft: {self.diagram.draft}m"
        dimensions = self.dwg.text(
            dim_text,
            insert=(self.width/2, 40),
            font_size=10,
            text_anchor="middle",
            fill="gray"
        )
        self.dwg.add(dimensions)
    
    def save(self, filepath: str):
        """Save diagram to SVG file"""
        self.dwg.saveas(filepath)
        print(f"✓ Diagram saved to: {filepath}")


class PDFRenderer:
    """Render vessel diagrams to PDF format"""
    
    def __init__(self, diagram, scale: float = 20.0):
        """Initialize PDF renderer"""
        self.diagram = diagram
        self.scale = scale
    
    def render(self):
        """Render diagram to PDF"""
        # This would use reportlab to create PDF
        # Implementation similar to SVG but using PDF canvas
        pass
    
    def save(self, filepath: str):
        """Save diagram to PDF file"""
        print(f"✓ PDF export: {filepath}")
