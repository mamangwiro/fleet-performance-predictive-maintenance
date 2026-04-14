from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def train_model(df):

    # Features and target
    X = df[['distance_km', 'total_stops', 'delivery_time_hours',
            'fuel_used_l', 'last_service_days']]
    y = df['breakdown']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Build pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(max_iter=1000, class_weight='balanced'))
    ])

    # Train model
    pipeline.fit(X_train, y_train)

    # Predictions
    y_prob = pipeline.predict_proba(X_test)[:, 1]

    # Risk classification
    def classify_risk(prob):
        if prob < 0.3:
            return "Low"
        elif prob < 0.6:
            return "Medium"
        else:
            return "High"

    X_test = X_test.copy()
    X_test['breakdown_probability'] = y_prob
    X_test['risk_category'] = X_test['breakdown_probability'].apply(classify_risk)

    print("\n🚗 RISK DISTRIBUTION:")
    print(X_test['risk_category'].value_counts())

    X_test.to_csv("outputs/risk_predictions.csv", index=False)
    return pipeline, X_test, y_test