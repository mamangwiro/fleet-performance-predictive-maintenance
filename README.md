# 🚛 Fleet Performance & Predictive Maintenance Analysis

## 🎯 Recruiter Quick View

### Business Problem

Fleet operators face unexpected vehicle breakdowns that increase maintenance costs, create operational disruptions, and reduce service reliability.

### Solution

Developed an end-to-end predictive maintenance analytics solution using Python, Machine Learning and Power BI to identify high-risk vehicles before breakdowns occur.

### Key Results

- Identified the main operational drivers of vehicle breakdowns
- Developed predictive models using Logistic Regression and Random Forest
- Built executive Power BI dashboards for decision support
- Created vehicle risk scoring methodology
- Demonstrated proactive maintenance planning capability

### Skills Demonstrated

- Data Analytics
- Machine Learning
- Feature Engineering
- Power BI Dashboard Development
- Business Analysis
- Fleet Operations Analytics

### Relevant Roles

- Data Analyst
- Business Analyst
- Supply Chain Analyst
- Fleet Performance Analyst
- Operations Analyst
- Transport Manager

## 📌 Executive Summary

This project analyzes fleet operational data to identify key drivers of vehicle breakdowns and evaluate predictive models for maintenance planning.

The analysis reveals that operational stress (distance, delivery load), maintenance delays, and performance inefficiencies significantly influence breakdown risk.

Two models were tested — Logistic Regression and Random Forest — with Logistic Regression outperforming due to the relatively linear relationships in the data.

The findings support proactive maintenance strategies to reduce downtime and improve fleet reliability.

---

## 📊 Dashboard Preview

### Executive Fleet Risk Command Centre

![Executive Dashboard](images/01_Executive%20Dashboard%20Preview.png)

### Maintenance Cost Analysis

![Maintenance Dashboard](images/02_Maintenance%20and%20Cost%20Analysis%20Report.png)

### Predictive Risk Driver Explorer

![Risk Driver Dashboard](images/03_Predictive%20Risk%20Driver%20Explorer.png)


---

## 🛠 Key Skills Demonstrated

### Data Analytics

- Data Cleaning
- Data Transformation
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Data Visualisation

### Machine Learning

- Logistic Regression
- Random Forest Modelling
- Feature Engineering
- Model Evaluation
- Predictive Risk Scoring

### Power BI

- Dashboard Development
- KPI Design
- DAX Measures
- Interactive Reporting
- Executive Decision Support

### Business Analysis

- Problem Definition
- Root Cause Analysis
- Business Impact Assessment
- Requirements Interpretation
- Decision Support Analytics

### Fleet & Operations Analytics

- Predictive Maintenance
- Vehicle Breakdown Analysis
- Maintenance Cost Analysis
- Operational Performance Monitoring
- Fleet Risk Assessment

---
## Business Impact

This project demonstrates how predictive analytics can support proactive fleet maintenance and operational decision-making.

### Operational Benefits

- Early identification of high-risk vehicles
- Reduced unexpected breakdowns
- Improved fleet reliability
- Better maintenance scheduling
- Improved operational visibility

### Financial Benefits

- Reduced maintenance expenditure
- Lower downtime costs
- Reduced service disruptions
- Improved resource utilisation

### Strategic Benefits

- Data-driven maintenance planning
- Improved risk management
- Enhanced decision-making capability
- Improved operational resilience

---

## 📊 Project Outcomes

The analysis identified several operational factors that significantly influence vehicle breakdown risk.

### Key Predictive Drivers

- Vehicle mileage accumulation
- Maintenance delays
- Delivery workload
- Operational stress factors
- Vehicle utilisation patterns

### Model Findings

- Logistic Regression achieved the strongest overall performance
- Operational variables demonstrated measurable influence on breakdown probability
- Breakdown risk can be estimated before failure events occur

### Management Actions Supported

- Prioritised preventative maintenance
- Fleet risk monitoring
- Resource allocation decisions
- Maintenance budget planning

---

## 🏗️ Solution Architecture

```text
Raw Fleet Data
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning Models
(Logistic Regression & Random Forest)
      │
      ▼
Vehicle Risk Scoring
      │
      ▼
Power BI Dashboards
      │
      ▼
Management Decision Support
```

---

## 📑 Table of Contents
- [Business Problem](#-business-problem)
- [Tools and Technologies](#-tools-and-technologies)
- [Dataset Overview](#-dataset-overview)
- [Data Preparation](#-data-preparation)
- [Exploratory Data Analysis](#-exploratory-data-analysis)
- [Model Development](#-model-development)
- [Model Comparison](#-model-comparison)
- [Power BI Operationalisation](#-power-bi-operationalisation)
- [Business Impact](#-business-impact)
- [Full Analysis Notebook](#-full-analysis-notebook)
---

## 1. Business Context

Fleet operators depend on reliable vehicle availability to maintain service levels, control operating costs, and meet customer commitments. Unexpected vehicle breakdowns can result in:

- Increased maintenance and repair expenditure
- Missed deliveries and service disruptions
- Reduced fleet utilisation
- Higher operational risk
- Negative customer experience

Traditional maintenance approaches are often reactive, addressing issues only after failures occur. This can lead to avoidable downtime and unnecessary costs.

To support a more proactive maintenance strategy, this project applies predictive analytics and machine learning techniques to operational fleet data. By identifying the factors most strongly associated with breakdown events, fleet managers can prioritise maintenance activities before failures occur.

The project simulates a real-world fleet environment by combining vehicle utilisation, maintenance history, driver behaviour and operational workload indicators to predict breakdown risk.

### Project Objectives

The primary objectives were to:

- Predict the likelihood of vehicle breakdowns
- Identify key operational and maintenance risk drivers
- Compare machine learning approaches for predictive performance
- Translate analytical outputs into actionable business insights
- Develop interactive Power BI dashboards for decision support

### Business Questions Addressed

This project seeks to answer the following questions:

1. Which vehicles are most likely to experience breakdowns?
2. Which operational factors contribute most to failure risk?
3. How can maintenance resources be prioritised effectively?
4. What financial exposure is associated with high-risk vehicles?
5. How can predictive analytics support fleet management decision-making?

### Expected Business Value

By implementing predictive maintenance strategies informed by this analysis, fleet operators can potentially achieve:

- Reduced vehicle downtime
- Improved fleet reliability
- Better maintenance planning
- Lower repair costs
- Enhanced operational visibility
- More informed management decisions

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
## 8. Power BI Operationalisation

## . Executive Fleet Risk Command Centre

![Executive Dashboard](dashboards/screenshots/01_executive_fleet_risk_command_centre.png)

### Key Insights
- Fleet risk exposure remains concentrated in low-to-medium risk vehicles
- High-risk vehicles require immediate preventive maintenance intervention
- Operational cost exposure is rising with delivery intensity

---

## . Maintenance Cost & Failure Analysis

![Maintenance Dashboard](dashboards/screenshots/02_maintenance_cost_failure_analysis.png)

### Key Insights
- Urban routes demonstrate the highest breakdown frequency
- Maintenance costs are disproportionately concentrated in certain assets
- Service delays strongly correlate with breakdown probability

---

## . Predictive Risk Driver Explorer

![Predictive Dashboard](dashboards/screenshots/03_predictive_risk_driver_explorer.png)

### Key Insights
- Maintenance cost is the strongest predictive risk driver
- Logistic regression coefficients provide directional interpretability
- Correlation analysis reveals operational stress relationships


## 9. Business Impact

- Enables proactive maintenance planning  
- Reduces downtime and repair costs  
- Improves fleet availability and efficiency  

### Strategic Insight:
Interpretability is critical in operations — Logistic Regression provides both performance and transparency.

---

## 10. Full Analysis Notebook

👉 [Open Notebook](notebooks/fleet_analysis.ipynb)


Local environment tested succesfully!

This is a test update made on the Feature-update-readme branch.
