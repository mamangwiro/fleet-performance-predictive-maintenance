from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


def train_model(df):

    # Features and target
    X = df[['distance_km', 'total_stops', 'delivery_time_hours',
            'fuel_used_l', 'last_service_days']]
    y = df['breakdown']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 🔹 Logistic Regression
    lr = LogisticRegression(max_iter=1000, class_weight='balanced')
    lr.fit(X_train, y_train)

    # 🔹 Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    print("✅ Models trained successfully!")

    return lr, rf, X_test, y_test