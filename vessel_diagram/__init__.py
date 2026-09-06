"""
Vessel Setup Diagram Generator
Automated tool to generate vessel equipment layout diagrams from survey data
"""

from .diagram import VesselDiagram
from .equipment import Equipment, EquipmentType

__version__ = "0.1.0"
__author__ = "Survey Automation Team"

__all__ = [
    'VesselDiagram',
    'Equipment',
    'EquipmentType'
]
