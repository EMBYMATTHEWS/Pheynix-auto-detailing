#!/usr/bin/env python3
"""
Pheynix Lead Tracker
Track car wash service leads and conversion
"""
import json
from datetime import datetime

def add_lead(name, type, contact, status="New"):
    """Add a new lead to the tracking system"""
    with open('../docs/leads.json', 'r') as f:
        leads = json.load(f)
    
    lead = {
        "name": name,
        "type": type,
        "contact": contact,
        "status": status,
        "date_added": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "notes": ""
    }
    
    leads["leads"].append(lead)
    
    with open('../docs/leads.json', 'w') as f:
        json.dump(leads, f, indent=2)
    
    return lead

if __name__ == "__main__":
    # Sample leads
    print("=== PHEYNIX LEAD TRACKER ===\n")
    
    # Show available categories
    print("LEAD CATEGORIES:")
    print("1. Car Dealerships")
    print("2. Rental Companies")  
    print("3. Luxury Car Owners")
    print("4. Ride Share Drivers")
    print("5. Fleet Owners")
    print("\nAdd leads to your tracking system!")
