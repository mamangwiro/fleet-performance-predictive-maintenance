# Model Performance

## 📌 Overview
This section evaluates the performance of the machine learning models used to predict vehicle breakdown risk. Two classification models were implemented and compared:
- Logistic Regression
- Random Forest

---

## 📊 Model Results

### 🔹 Logistic Regression
- Accuracy: **77%**
- Precision (Breakdown = 1): **81%**
- Recall (Breakdown = 1): **78%**
- F1-Score: **80%**

### 🔹 Random Forest
- Accuracy: **78%**
- Precision (Breakdown = 1): **82%**
- Recall (Breakdown = 1): **79%**
- F1-Score: **81%**

---

## ⚖️ Model Comparison

| Metric        | Logistic Regression | Random Forest |
|--------------|-------------------|--------------|
| Accuracy     | 77%               | 78%          |
| Precision    | 81%               | 82%          |
| Recall       | 78%               | 79%          |
| F1-Score     | 80%               | 81%          |

---

## 🧠 Key Insights

- The **Random Forest model outperformed Logistic Regression** across all evaluation metrics.
- It demonstrated **better recall**, making it more effective at identifying potential breakdown events.
- Logistic Regression provided strong baseline performance but is less capable of capturing complex relationships in the data.

---

## ✅ Model Selection

The **Random Forest model** was selected as the preferred model due to:
- Higher overall accuracy
- Better balance between precision and recall
- Improved ability to detect breakdown risk early

---

## ⚠️ Limitations

- The dataset used is **synthetic**, which may not fully represent real-world fleet behaviour.
- Model performance could improve with:
  - Real operational data
  - Larger dataset
  - Additional features (e.g., sensor data, driver behaviour)

---

## 📌 Conclusion

The Random Forest model provides a reliable and practical solution for predicting vehicle breakdown risk. Its performance supports its use in real-world logistics environments for proactive maintenance and risk management.