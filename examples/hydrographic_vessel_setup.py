"""
Example: Hydrographic Survey Vessel Setup
Octans, Multibeam, Trimble MPS, Dual GPS Antennas, Tide Antenna, Computer, Power Supply
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from vessel_diagram import VesselDiagram

def create_hydrographic_vessel():
    """Create a typical hydrographic survey vessel setup"""
    
    # Initialize vessel (typical survey vessel dimensions)
    vessel = VesselDiagram(
        vessel_name="Research Vessel SURVEYOR-1",
        length=12.0,  # 12 meters LOA
        beam=4.5,     # 4.5 meters beam
        draft=1.2     # 1.2 meters draft
    )
    
    print("=" * 70)
    print("HYDROGRAPHIC SURVEY VESSEL - SETUP CONFIGURATION")
    print("=" * 70)
    print(f"\nVessel: {vessel.vessel_name}")
    print(f"Dimensions: {vessel.length}m (L) × {vessel.beam}m (B) × {vessel.draft}m (D)")
    print("\n" + "=" * 70)
    print("EQUIPMENT POSITIONING")
    print("=" * 70)
    
    # ==========================================
    # POSITIONING SYSTEM - Top of Vessel
    # ==========================================
    print("\n📍 POSITIONING SYSTEM (GPS/GNSS)")
    print("-" * 70)
    
    # Primary GPS Antenna (Starboard)
    gps1 = vessel.add_equipment(
        name="GPS Antenna 1 (Port)",
        position=(1.5, 0.3),  # Port side, forward
        equipment_type="antenna",
        size=(0.25, 0.25),
        height_above_deck=1.8,
        notes="Primary GPS - RTK enabled"
    )
    print(f"✓ GPS Antenna 1: Position ({gps1.position[0]}, {gps1.position[1]}) | Height: {gps1.height_above_deck}m")
    
    # Secondary GPS Antenna (Starboard)
    gps2 = vessel.add_equipment(
        name="GPS Antenna 2 (Starboard)",
        position=(1.5, 4.2),  # Starboard side, forward
        equipment_type="antenna",
        size=(0.25, 0.25),
        height_above_deck=1.8,
        notes="Secondary GPS - Redundancy/Heading"
    )
    print(f"✓ GPS Antenna 2: Position ({gps2.position[0]}, {gps2.position[1]}) | Height: {gps2.height_above_deck}m")
    
    # Trimble MPS (Multi-band Positioning System)
    trimble = vessel.add_equipment(
        name="Trimble MPS",
        position=(2.0, 2.25),  # Center, forward
        equipment_type="antenna",
        size=(0.3, 0.3),
        height_above_deck=1.5,
        notes="Multi-band GNSS receiver"
    )
    print(f"✓ Trimble MPS: Position ({trimble.position[0]}, {trimble.position[1]}) | Height: {trimble.height_above_deck}m")
    
    # Tide/RTK Antenna
    tide = vessel.add_equipment(
        name="Differential GNSS Antenna (Tide/RTK)",
        position=(2.5, 2.25),  # Center, aft of Trimble
        equipment_type="antenna",
        size=(0.2, 0.2),
        height_above_deck=1.5,
        notes="Tide reference & RTK correction"
    )
    print(f"✓ Tide Antenna: Position ({tide.position[0]}, {tide.position[1]}) | Height: {tide.height_above_deck}m")
    
    # ==========================================
    # ATTITUDE SENSOR - Mast Top
    # ==========================================
    print("\n🧭 ATTITUDE & HEADING SENSOR")
    print("-" * 70)
    
    octans = vessel.add_equipment(
        name="Octans Gyroscope",
        position=(3.0, 2.25),  # Center mast
        equipment_type="gyroscope",
        size=(0.4, 0.4),
        height_above_deck=2.0,
        notes="Attitude/Heading sensor - measures heave, pitch, roll"
    )
    print(f"✓ Octans: Position ({octans.position[0]}, {octans.position[1]}) | Height: {octans.height_above_deck}m")
    
    # ==========================================
    # SONAR TRANSDUCERS - Hull
    # ==========================================
    print("\n🌊 SONAR SYSTEMS")
    print("-" * 70)
    
    multibeam = vessel.add_equipment(
        name="Multibeam Sonar (EM2040P)",
        position=(4.5, 2.25),  # Mid-ship
        equipment_type="sonar",
        size=(0.6, 0.8),
        height_above_deck=-0.5,  # Below waterline
        notes="Multi-beam echo sounder - full water column"
    )
    print(f"✓ Multibeam: Position ({multibeam.position[0]}, {multibeam.position[1]}) | Depth: {multibeam.height_above_deck}m below deck")
    
    # ==========================================
    # ELECTRONICS & POWER - Cabin
    # ==========================================
    print("\n💻 ELECTRONICS & POWER SYSTEMS")
    print("-" * 70)
    
    computer = vessel.add_equipment(
        name="Survey Computer (Data Acquisition)",
        position=(7.0, 1.5),  # Cabin area
        equipment_type="computer",
        size=(0.4, 0.3),
        height_above_deck=0.7,  # On desk
        notes="Main data acquisition & processing unit"
    )
    print(f"✓ Computer: Position ({computer.position[0]}, {computer.position[1]})")
    
    power = vessel.add_equipment(
        name="Power Supply & UPS",
        position=(7.0, 3.0),  # Cabin area
        equipment_type="power",
        size=(0.5, 0.4),
        height_above_deck=0.0,  # On floor
        notes="120V AC + UPS backup"
    )
    print(f"✓ Power Supply: Position ({power.position[0]}, {power.position[1]})")
    
    network = vessel.add_equipment(
        name="Network Switch & Router",
        position=(7.5, 2.25),  # Cabin
        equipment_type="network",
        size=(0.3, 0.3),
        height_above_deck=0.5,
        notes="Ethernet hub for all systems"
    )
    print(f"✓ Network Switch: Position ({network.position[0]}, {network.position[1]})")
    
    storage = vessel.add_equipment(
        name="External Data Storage (NAS)",
        position=(8.0, 2.25),  # Cabin
        equipment_type="storage",
        size=(0.3, 0.4),
        height_above_deck=0.3,
        notes="SSD/HDD data backup"
    )
    print(f"✓ Storage: Position ({storage.position[0]}, {storage.position[1]})")
    
    # ==========================================
    # CABLE ROUTING
    # ==========================================
    print("\n🔌 CABLE CONNECTIONS")
    print("-" * 70)
    
    # Antennas to computer
    vessel.add_cable_route("GPS Antenna 1 (Port)", "Network Switch & Router", 
                          cable_type="GPS/GNSS", color="#FF6B6B")
    vessel.add_cable_route("GPS Antenna 2 (Starboard)", "Network Switch & Router", 
                          cable_type="GPS/GNSS", color="#FF6B6B")
    vessel.add_cable_route("Trimble MPS", "Network Switch & Router", 
                          cable_type="Ethernet", color="#4ECDC4")
    vessel.add_cable_route("Differential GNSS Antenna (Tide/RTK)", "Network Switch & Router", 
                          cable_type="Antenna Cable", color="#FFA500")
    
    # Attitude sensor to computer
    vessel.add_cable_route("Octans Gyroscope", "Network Switch & Router", 
                          cable_type="Ethernet", color="#4ECDC4")
    
    # Sonar to computer
    vessel.add_cable_route("Multibeam Sonar (EM2040P)", "Network Switch & Router", 
                          cable_type="Ethernet", color="#4ECDC4")
    
    # Network to computer
    vessel.add_cable_route("Network Switch & Router", "Survey Computer (Data Acquisition)", 
                          cable_type="Ethernet", color="#4ECDC4")
    
    # Power connections
    vessel.add_cable_route("Power Supply & UPS", "Survey Computer (Data Acquisition)", 
                          cable_type="Power", color="#9B59B6")
    vessel.add_cable_route("Power Supply & UPS", "Network Switch & Router", 
                          cable_type="Power", color="#9B59B6")
    vessel.add_cable_route("Power Supply & UPS", "Multibeam Sonar (EM2040P)", 
                          cable_type="Power", color="#9B59B6")
    
    print("✓ GPS Antenna 1 → Network Switch")
    print("✓ GPS Antenna 2 → Network Switch")
    print("✓ Trimble MPS → Network Switch")
    print("✓ Tide Antenna → Network Switch")
    print("✓ Octans → Network Switch")
    print("✓ Multibeam → Network Switch")
    print("✓ Network Switch → Computer")
    print("✓ Power Supply → Computer, Network, Multibeam")
    
    # ==========================================
    # METADATA
    # ==========================================
    print("\n📋 METADATA")
    print("-" * 70)
    
    vessel.add_metadata("survey_type", "Hydrographic")
    vessel.add_metadata("accuracy_class", "IHO Special Order")
    vessel.add_metadata("max_depth", "300 meters")
    vessel.add_metadata("grid_resolution", "2 meters")
    vessel.add_metadata("operating_frequency_multibeam", "200-400 kHz")
    
    print("✓ Survey Type: Hydrographic")
    print("✓ Accuracy Class: IHO Special Order")
    print("✓ Max Operating Depth: 300 meters")
    print("✓ Grid Resolution: 2 meters")
    
    # ==========================================
    # VALIDATION & OUTPUT
    # ==========================================
    print("\n✅ VALIDATION")
    print("-" * 70)
    
    warnings = vessel.validate_positions()
    if warnings:
        for warning in warnings:
            print(f"⚠ {warning}")
    else:
        print("✓ All equipment positions validated successfully")
    
    print("\n" + "=" * 70)
    return vessel


def main():
    """Main execution"""
    # Create vessel setup
    vessel = create_hydrographic_vessel()
    
    # Print summary
    print("\n" + vessel.get_equipment_summary())
    
    # Generate diagrams
    print("\n" + "=" * 70)
    print("GENERATING DIAGRAMS")
    print("=" * 70)
    
    try:
        vessel.save_svg("vessel_setup_diagram.svg", scale=60)
        print("✓ SVG diagram created: vessel_setup_diagram.svg")
    except Exception as e:
        print(f"✗ SVG generation failed: {e}")
    
    # Save configuration as JSON for reference
    import json
    config = {
        "vessel": {
            "name": vessel.vessel_name,
            "length_m": vessel.length,
            "beam_m": vessel.beam,
            "draft_m": vessel.draft,
        },
        "equipment": [
            {
                "name": eq.name,
                "type": eq.equipment_type.value,
                "position": eq.position,
                "size": eq.size,
                "height_above_deck_m": eq.height_above_deck,
                "notes": eq.notes
            }
            for eq in vessel.equipment
        ],
        "cable_routes": vessel.cable_routes,
        "metadata": vessel.metadata
    }
    
    with open("vessel_config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    print("✓ Configuration saved: vessel_config.json")
    print("\n" + "=" * 70)
    print("SETUP COMPLETE!")
    print("=" * 70)


if __name__ == "__main__":
    main()
