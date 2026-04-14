
def create_features(df):
    df['cost_per_km'] = df['maintenance_cost'] / df['distance_km']
    df['fuel_efficiency'] = df['distance_km'] / df['fuel_used_l']
    return df