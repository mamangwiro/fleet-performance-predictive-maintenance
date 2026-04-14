import sys
import os

# Fix path so Python can find src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_generation import generate_fleet_data
from src.preprocessing import create_features
from src.model import train_model

print("Step 1: Generating data...")
df = generate_fleet_data()

print("Step 2: Saving data...")
df.to_csv("data/raw/fleet_data.csv", index=False)

print("Step 3: Creating features...")
df = create_features(df)

print("Step 4: Training model...")
model, X_test, y_test = train_model(df)

print("✅ Model trained successfully!")