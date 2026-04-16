import sys
import os

# Fix path so Python can find src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_generation import generate_fleet_data
from src.feature_engineering import create_features
from src.model import train_model
from src.utils import print_model_results, save_predictions

print("Step 1: Generating data...")
df = generate_fleet_data()


print("Step 2: Feature engineering...")
df = create_features(df)

print("Step 3: Training model...")
lr, rf, X_test, y_test = train_model(df)

# 🔥 Evaluation (this was missing)
lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)

print_model_results("Logistic Regression", y_test, lr_pred)
print_model_results("Random Forest", y_test, rf_pred)

# 💾 Save predictions
save_predictions(rf, X_test)

print("✅ Pipeline completed successfully!")