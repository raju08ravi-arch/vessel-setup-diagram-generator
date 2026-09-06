# Vessel Setup Diagram Generator

Automated tool to generate vessel setup diagrams from hydrographic survey data, coordinates, and equipment positions.

## Features

- Generate vessel equipment layout diagrams
- Support for multiple sensor configurations
- Auto-create SVG/PDF diagrams from survey data
- Equipment positioning calculations
- Cable routing visualization

## Supported Equipment

### Navigation & Positioning
- Trimble MPS (Multi-band Positioning System)
- GPS Antennas (Primary & Secondary)
- Differential GNSS Antenna (Tide/Correction)
- Total Station mounts
- LiDAR positioning

### Survey Equipment
- Octans (Gyroscope/Attitude sensor)
- Multibeam Sonar
- Single Beam Sonar
- Side Scan Sonar
- Sub-bottom Profiler

### Support Systems
- Computer/Processing Unit
- Power Supply & UPS
- Network Equipment
- Data Storage

## Installation

```bash
git clone https://github.com/raju08ravi-arch/vessel-setup-diagram-generator
cd vessel-setup-diagram-generator
pip install -r requirements.txt
```

## Quick Start

```python
from vessel_diagram import VesselDiagram

# Create a diagram
diagram = VesselDiagram(vessel_name="Survey Vessel Alpha", beam=8, length=12)

# Add equipment
diagram.add_equipment("Octans", position=(2, 4), equipment_type="gyroscope")
diagram.add_equipment("Multibeam", position=(3, 3), equipment_type="sonar")
diagram.add_equipment("GPS Antenna 1", position=(1, 6), equipment_type="antenna")
diagram.add_equipment("GPS Antenna 2", position=(5, 6), equipment_type="antenna")
diagram.add_equipment("Tide Antenna", position=(3, 6.5), equipment_type="antenna")
diagram.add_equipment("Computer", position=(2, 2), equipment_type="computer")
diagram.add_equipment("Power Supply", position=(1, 1), equipment_type="power")

# Generate diagram
diagram.save("vessel_setup.svg")
```

## Documentation

See [docs/](docs/) for detailed documentation and examples.

## Project Structure

```
vessel-setup-diagram-generator/
├── README.md
├── requirements.txt
├── vessel_diagram/
│   ├── __init__.py
│   ├── diagram.py           # Main diagram generator
│   ├── equipment.py         # Equipment definitions
│   ├── renderer.py          # SVG/PDF rendering
│   └── calculations.py      # Positioning calculations
├── examples/
│   ├── basic_setup.py       # Basic vessel setup
│   └── advanced_setup.py    # Complex configurations
├── templates/
│   └── vessel_templates.json # Pre-built vessel configs
└── docs/
    ├── installation.md
    ├── usage.md
    └── equipment-reference.md
```

## License

MIT License - See LICENSE file for details

## Contributing

Contributions welcome! Please submit issues and pull requests.

## Author

Created for hydrographic survey automation
