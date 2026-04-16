# Assumptions and Limitations

## 📌 Overview
This project is based on a simulated fleet dataset and a controlled modelling environment. While the results are meaningful for demonstration purposes, certain assumptions and limitations should be considered when interpreting the findings.

---

## 🔍 Key Assumptions

### 1. Synthetic Data Representation
- The dataset was artificially generated to simulate real-world fleet operations
- Assumes that the relationships between variables reflect realistic logistics scenarios

---

### 2. Breakdown Definition
- Breakdown events are defined based on predefined conditions within the dataset
- Assumes consistent criteria for what constitutes a vehicle failure

---

### 3. Feature Relevance
- Selected variables (e.g., fuel usage, delivery time, maintenance cost) are assumed to be key drivers of breakdown risk
- Other potential factors were not included

---

### 4. Static Data Environment
- The model assumes a static dataset rather than continuously updating real-time data
- Does not account for dynamic operational changes

---

## ⚠️ Limitations

### 1. Lack of Real-World Data
- The model has not been trained on actual fleet data
- Performance may differ in real operational environments

---

### 2. Limited Feature Scope
- Important variables not included:
  - Vehicle age
  - Driver behaviour
  - Environmental conditions
  - Telematics/sensor data

---

### 3. Model Generalisation
- Model performance may not generalise across:
  - Different fleet types
  - Geographic regions
  - Operational conditions

---

### 4. Binary Classification Simplification
- Breakdown risk is treated as a binary outcome (breakdown vs no breakdown)
- Does not capture varying levels of severity or types of failures

---

### 5. No Real-Time Integration
- The model is not integrated with live systems
- Predictions are based on historical/static data only

---

## 🚀 Opportunities for Improvement

- Integrate real fleet data from operational systems
- Incorporate IoT/telematics data for real-time monitoring
- Expand feature set to include behavioural and environmental factors
- Deploy model into a live dashboard environment for continuous updates

---

## ✅ Conclusion

While the model provides a strong foundation for predictive maintenance, its full value would be realised through integration with real-world data and operational systems. The current implementation serves as a proof of concept for data-driven fleet management.