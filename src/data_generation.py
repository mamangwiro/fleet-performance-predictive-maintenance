import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_fleet_data(num_records=2000):
    np.random.seed(42)

    num_vehicles = 50
    num_drivers = 80

    vehicle_ids = [f"V{str(i).zfill(3)}" for i in np.random.randint(1, num_vehicles+1, num_records)]
    driver_ids = [f"D{str(i).zfill(3)}" for i in np.random.randint(1, num_drivers+1, num_records)]

    start_date = datetime(2025, 1, 1)
    dates = [start_date + timedelta(days=int(x)) for x in np.random.randint(0, 90, num_records)]

    route_types = np.random.choice(['Urban', 'Suburban', 'Rural'], num_records, p=[0.5, 0.3, 0.2])

    total_stops = np.random.randint(80, 180, num_records)
    distance_km = total_stops * np.random.uniform(0.6, 1.2, num_records)
    delivery_time_hours = distance_km / np.random.uniform(25, 40, num_records)
    fuel_used = distance_km / np.random.uniform(8, 12, num_records)

    last_service_days = np.random.randint(1, 60, num_records)

    breakdown_prob = (
        (distance_km / distance_km.max()) * 0.15 +
        (last_service_days / 60) * 0.25
    )

    breakdown = np.random.binomial(1, breakdown_prob)

    maintenance_cost = np.random.uniform(30, 120, num_records) + breakdown * np.random.uniform(150, 600, num_records)

    df = pd.DataFrame({
        'vehicle_id': vehicle_ids,
        'driver_id': driver_ids,
        'date': dates,
        'route_type': route_types,
        'total_stops': total_stops,
        'distance_km': distance_km,
        'delivery_time_hours': delivery_time_hours,
        'fuel_used_l': fuel_used,
        'last_service_days': last_service_days,
        'breakdown': breakdown,
        'maintenance_cost': maintenance_cost
    })

    return df