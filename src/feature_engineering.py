def create_features(df):

    # Example feature engineering
    df['avg_speed'] = df['distance_km'] / df['delivery_time_hours']
    df['fuel_efficiency'] = df['distance_km'] / df['fuel_used_l']

    # Fill any potential missing values
    df.replace([float('inf'), -float('inf')], 0, inplace=True)

    return df
