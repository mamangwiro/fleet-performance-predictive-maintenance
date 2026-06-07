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

The analysis reveals that vehicle utilisation (distance travelled, delivery workload and fuel consumption) together with maintenance indicators (service intervals and maintenance expenditure) are strongly associated with vehicle breakdown risk.

Two machine learning models were evaluated: Logistic Regression and Random Forest.

Both models achieved comparable predictive performance, indicating that the operational and maintenance variables contain strong predictive signals. Random Forest achieved marginally higher accuracy and F1-score, while Logistic Regression provided a more interpretable view of the factors influencing breakdown risk.

---

## Portfolio Highlights

This project demonstrates the end-to-end delivery of a predictive maintenance analytics solution, from data preparation and feature engineering through machine learning model development and business intelligence reporting.

The project showcases practical skills relevant to Data Analyst, Business Analyst, Fleet Analyst and Supply Chain Analytics roles, including:

- Data Cleaning and Transformation
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Predictive Modelling
- Model Evaluation
- Power BI Dashboard Development
- Business Insight Generation
- Git Version Control

---

## 📊 Dashboard Preview

### Executive Fleet Risk Command Centre

**Business Problem**
Fleet managers often react to vehicle breakdowns after they occur, resulting in unplanned downtime, service disruptions and increased maintenance costs.

**Objective**

Provide a single executive dashboard that identifies high-risk vehicles, estimates operational exposure and supports preventative maintenance planning.

**Key Features**

- Fleet-wide breakdown risk visibility
- Risk distribution by vehicle category
- Breakdown trend monitoring
- Operational cost exposure analysis
- High-risk vehicle prioritisation

**Tools & Techniques Used**

- Python
- Pandas
- Logistic Regression
- Random Forest
- Power BI
- DAX Measures

**Business Value Delivered**

- Supports proactive maintenance scheduling
- Reduces unexpected breakdowns
- Improves fleet availability
- Enables data-driven maintenance decisions

![Executive Fleet Risk Command Centre](images/01_Executive%20Dashboard%20Preview.png)


### Maintenance Cost & Failure Analysis

**Business Problem**

Maintenance expenditure is often reviewed retrospectively, making it difficult to identify cost drivers and prioritise interventions.

**Objective**

Analyse maintenance costs alongside predicted breakdown events to identify areas of financial exposure and maintenance inefficiencies.

**Key Features**

- Breakdown cost estimation
- Failure trend analysis
- Cost concentration monitoring
- Vehicle-level maintenance exposure
- Preventative maintenance opportunity identification

**Tools & Techniques Used**

- Python
- Feature Engineering
- Predictive Analytics
- Power BI
- DAX Measures

**Business Value Delivered**

- Improves maintenance budget planning
- Identifies cost reduction opportunities
- Supports preventative maintenance strategies
- Improves asset lifecycle management

![Maintenance Cost & Failure Analysis](images/02_Maintenance%20and%20Cost%20Analysis%20Report.png)

### Predictive Risk Driver Explorer

**Business Problem**

Knowing which vehicles are likely to fail is useful, but understanding *why* they are likely to fail enables more effective intervention planning.

**Objective**

Identify and visualise the operational and maintenance factors that most strongly influence vehicle breakdown risk.

**Key Features**

- Feature importance analysis
- Risk driver visualisation
- Breakdown probability exploration
- Vehicle utilisation impact assessment
- Maintenance behaviour analysis

**Tools & Techniques Used**

- Logistic Regression Coefficients
- Random Forest Feature Importance
- Feature Engineering
- Correlation Analysis
- Power BI

**Business Value Delivered**

- Improves maintenance prioritisation
- Identifies root causes of breakdown risk
- Supports targeted intervention strategies
- Enhances decision-making transparency

![Predictive Risk Driver Explorer](images/03_Predictive%20Risk%20Driver%20Explorer.png)

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

- Random Forest achieved marginally higher predictive performance across Accuracy, Precision, Recall and F1 Score.
- Logistic Regression remained highly competitive while offering superior interpretability.
- Operational and maintenance variables demonstrated measurable influence on vehicle breakdown probability.
- Breakdown risk can be estimated before failure events occur.

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

## 2. Project Scope

| Metric | Value |
|----------|----------|
| Operational & Maintenance Records | 2,000 |
| Fleet Vehicles Modelled | 50 |
| Drivers Analysed | 80 |
| Time Period | 90 Days (Simulated) |
| Machine Learning Models | 2 |
| Power BI Dashboards | 3 |

### Scope Clarification

This project analysed 2,000 operational and maintenance transaction records generated across a fleet of 50 vehicles and 80 drivers.

The dataset contains multiple records for the same vehicle and driver over time, representing maintenance events, operational performance, service intervals and breakdown outcomes.

The objective was not to analyse 2,000 individual vehicles, but rather to use 2,000 historical observations to identify patterns associated with vehicle breakdown risk.
## 3. Tools and Technologies

### Data Processing & Modelling
- **Python** (pandas, numpy)
- **Machine Learning** (scikit-learn: Logistic Regression, Random Forest)
- **Model Evaluation** (accuracy, precision, recall, confusion matrix)

### Development Environment
- **Jupyter Notebook**

### Visualisation & Reporting
- **Power BI**

---

## 3. Dataset Overview

### Project Scope

This project uses a synthetic fleet operations dataset designed to simulate a real-world predictive maintenance environment.

The dataset contains:

- 2,000 operational records
- 50 fleet vehicles
- 80 drivers
- 90-day operational period

Each record represents a vehicle operational event rather than a unique vehicle.

### Dataset Structure

The dataset consists of 11 variables covering vehicle utilisation, maintenance history and operational performance.

| Category | Variables |
|-----------|-----------|
| Asset Identification | vehicle_id |
| Driver Identification | driver_id |
| Operational Context | date, route_type |
| Vehicle Utilisation | distance_km, total_stops, delivery_time_hours |
| Fuel Consumption | fuel_used_l |
| Maintenance Indicators | last_service_days, maintenance_cost |
| Target Variable | breakdown |

### Analytical Scope

The analysis combines:

- Vehicle utilisation patterns
- Maintenance history indicators
- Operational workload metrics
- Fuel consumption behaviour
- Historical breakdown events

These variables were used to:

- Identify factors associated with vehicle breakdowns
- Quantify predictive risk drivers
- Develop machine learning models for breakdown prediction
- Support proactive maintenance planning decisions

### Target Variable

The predictive models were trained to estimate:

- **breakdown = 1** → Vehicle experienced a breakdown
- **breakdown = 0** → Vehicle did not experience a breakdown

This binary target variable forms the basis of the predictive maintenance modelling process.---

## 5. Data Preparation

- Verified data completeness and structure  
- Removed non-predictive identifiers (`vehicle_id`, `driver_id`)  
- Handled infinite values and ensured clean dataset  
- Validated consistency across operational metrics  

---

## 6. Exploratory Data Analysis

Key insights:

- Breakdown risk increases with longer service intervals  
- High mileage and delivery load contribute to failures  
- Poor delivery performance correlates with breakdowns  
- Operational stress is a major driver of vehicle reliability  

---

## 7. Model Development

Two models were implemented:
- Logistic Regression  
- Random Forest  

---

## 8. Model Performance Summary

| Metric    | Logistic Regression | Random Forest |
| --------- | ------------------- | ------------- |
| Accuracy  | 0.77                | 0.78          |
| Precision | 0.81                | 0.82          |
| Recall    | 0.78                | 0.79          |
| F1 Score  | 0.80                | 0.81          |

---

## 9. Model Comparison & Interpretation

Both models delivered strong predictive performance on the synthetic fleet dataset.

Random Forest achieved marginally higher Accuracy, Precision, Recall and F1 Score, indicating a slightly stronger ability to identify vehicle breakdown risk.

Logistic Regression remained highly competitive while offering superior interpretability through model coefficients, making it easier to explain the influence of operational and maintenance variables.

### Key Takeaway

For maximum predictive performance, Random Forest would be selected.

For situations where model explainability and transparency are priorities, Logistic Regression remains a valuable alternative.

---

## 10. Power BI Operationalisation

## . Executive Fleet Risk Command Centre

[Executive Dashboard](images/01_Executive%20Dashboard%20Preview.png)
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
- Maintenance expenditure, service delays and route characteristics were identified as significant contributors to breakdown risk.
- Logistic Regression coefficients provided interpretable directional insight into the operational factors influencing vehicle failures.
- Random Forest feature importance highlighted non-linear relationships between maintenance history and breakdown probability.
- Correlation analysis revealed measurable relationships between operational stress indicators and vehicle reliability outcomes.

### Business Impact

- Supports proactive maintenance scheduling using predicted breakdown risk.
- Helps prioritise limited maintenance resources towards high-risk assets.
- Reduces operational downtime and unplanned repair expenditure.
- Improves fleet availability, service reliability and customer satisfaction.

---

### Strategic Insight:
While Random Forest delivered the highest predictive performance, Logistic Regression offered greater interpretability, enabling fleet managers to understand not only which vehicles were at risk, but also why they were at risk.

## 12. Full Analysis Notebook

👉 [Open Notebook](notebooks/fleet_analysis.ipynb)


Local environment tested succesfully!

This is a test update made on the Feature-update-readme branch.
