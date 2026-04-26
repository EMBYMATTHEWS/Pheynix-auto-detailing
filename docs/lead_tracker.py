#!/usr/bin/env python3
"""
Quick lead tracker for Pheynix Auto Detailing
"""
import json
from datetime import datetime

def add_lead(name, contact_type, phone="", email=""):
    """Add a new lead"""
    try:
        with open('docs/leads.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"leads": []}
    
    lead = {
        "id": len(data["leads"]) + 1,
        "name": name,
        "contact_type": contact_type,
        "phone": phone,
        "email": email,
        "date": datetime.now().strftime('%Y-%m-%d'),
        "status": "New"
    }
    
    data["leads"].append(lead)
    
    with open('docs/leads.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Added lead: {name}")

if __name__ == "__main__":
    print("=== PHEYNIX LEAD TRACKER ===\n")
    print("Add leads using:")
    print("  python3 scripts/lead_tracker.py")
    print("\nAvailable contact types:")
    print("  - Dealership")
    print("  - Rental Company")
    print("  - Luxury Owner")
    print("  - Ride Share Driver")
    print("  - Fleet Owner")
