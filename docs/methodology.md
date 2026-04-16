# Methodology

## 📌 Overview
This project follows a structured data analytics and machine learning workflow to analyse fleet performance and predict vehicle breakdown risk. The approach ensures data quality, meaningful feature creation, and reliable model evaluation.

---

## 📊 Data Source
A synthetic fleet dataset was generated to simulate real-world logistics operations. The dataset includes variables such as:
- Vehicle usage (distance, fuel consumption)
- Delivery performance (on-time vs late deliveries)
- Maintenance indicators (last service days, maintenance cost)
- Operational attributes (route type, delivery time)

---

## 🧹 Data Cleaning
The dataset was cleaned to ensure consistency and usability:
- Checked for missing values (none found)
- Removed duplicate records
- Dropped non-predictive identifiers such as:
  - `vehicle_id`
  - `driver_id`
- Ensured correct data types for numerical analysis

---

## ⚙️ Feature Engineering
Additional processing steps were applied to prepare the data for modelling:
- Converted categorical variables (e.g., `route_type`) into numerical format using one-hot encoding
- Removed irrelevant features (e.g., date field)
- Structured dataset into:
  - **Features (X)** → input variables
  - **Target (y)** → breakdown occurrence

---

## 🤖 Model Development
Two classification models were implemented:

### 1. Logistic Regression
- Baseline model for binary classification
- Provides interpretability of relationships between variables

### 2. Random Forest
- Ensemble learning method
- Captures non-linear relationships
- More robust for complex datasets

---

## 📏 Model Evaluation
Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score

A train-test split (80/20) was used to ensure fair performance assessment.

---

## 📊 Visualisation
A Power BI dashboard was developed to:
- Present fleet risk distribution
- Highlight high-risk vehicles
- Enable interactive analysis for decision-making

---

## ✅ Summary
The methodology combines data preparation, machine learning, and visual analytics to deliver a practical predictive maintenance solution for logistics operations.