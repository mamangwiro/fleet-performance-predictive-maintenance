import pandas as pd
from sklearn.metrics import classification_report

def print_model_results(model_name, y_test, y_pred):
    print(f"\n📊 {model_name} Performance:")
    print(classification_report(y_test, y_pred))

def save_predictions(model, X_test, filename="outputs/risk_predictions.csv"):
    predictions = model.predict(X_test)

    df = pd.DataFrame({
        "prediction": predictions
    })

    df.to_csv(filename, index=False)
    print(f"\n💾 Predictions saved to {filename}")