# 🚛 Fleet Performance & Predictive Maintenance Analysis

## 📌 Executive Summary

This project analyzes fleet operational data to identify key drivers of vehicle breakdowns and evaluate predictive models for maintenance planning.

The analysis reveals that operational stress (distance, delivery load), maintenance delays, and performance inefficiencies significantly influence breakdown risk.

Two models were tested — Logistic Regression and Random Forest — with Logistic Regression outperforming due to the relatively linear relationships in the data.

The findings support proactive maintenance strategies to reduce downtime and improve fleet reliability.

---

## 📑 Table of Contents

- [Business Problem](#business-problem)
- [Tools and Technologies](#tools-and-technologies)
- [Dataset Overview](#dataset-overview)
- [Data Preparation](#data-preparation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Development](#model-development)
- [Model Comparison](#model-comparison)
- [Business Impact](#business-impact)
- [Full Analysis Notebook](#full-analysis-notebook)
---

## 1. Business Problem

Fleet breakdowns disrupt operations, increase costs, and reduce service reliability.

Objective:
To predict vehicle breakdown risk using operational and maintenance data, enabling proactive decision-making.

---
## 2. Tools and Technologies

### Data Processing & Modelling
- **Python** (pandas, numpy)
- **Machine Learning** (scikit-learn: Logistic Regression, Random Forest)
- **Model Evaluation** (accuracy, precision, recall, confusion matrix)

### Development Environment
- **Jupyter Notebook**

### Visualisation & Reporting
- **Power BI**
## 3. Dataset Overview

The dataset consists of simulated fleet operational data reflecting real-world logistics conditions.

### Key Variables:

**Operational Metrics**
- distance_km  
- total_stops  
- delivery_time_hours  
- fuel_used_l  

**Maintenance Indicators**
- last_service_days  
- maintenance_cost  

**Performance Metrics**
- late_deliveries  
- delivery_success_rate  

**Target Variable**
- breakdown (1 = breakdown, 0 = no breakdown)

---

## 4. Data Preparation

- Verified data completeness and structure  
- Removed non-predictive identifiers (`vehicle_id`, `driver_id`)  
- Handled infinite values and ensured clean dataset  
- Validated consistency across operational metrics  

---

## 5. Exploratory Data Analysis

Key insights:

- Breakdown risk increases with longer service intervals  
- High mileage and delivery load contribute to failures  
- Poor delivery performance correlates with breakdowns  
- Operational stress is a major driver of vehicle reliability  

---

## 6. Model Development

Two models were implemented:
- Logistic Regression  
- Random Forest  

---

## 7. Model Comparison

| Model | Insight |
|------|--------|
| Logistic Regression | Better breakdown detection |
| Random Forest | No significant improvement |

### Key Finding:
Simpler models performed better, indicating linear relationships in the data.

---

## 8. Business Impact

- Enables proactive maintenance planning  
- Reduces downtime and repair costs  
- Improves fleet availability and efficiency  

### Strategic Insight:
Interpretability is critical in operations — Logistic Regression provides both performance and transparency.

---

## 9. Full Analysis Notebook

👉 [Open Notebook](notebooks/fleet_analysis.ipynb)
