# Hospital Performance Analytics Dashboard

## Overview

The Hospital Performance Analytics Dashboard is a healthcare analytics project designed to analyze patient records, treatment costs, readmission patterns, patient satisfaction, and hospital performance metrics. The project combines Python-based data analysis with an interactive Tableau dashboard to generate actionable healthcare insights.

This project demonstrates data cleaning, exploratory data analysis (EDA), KPI tracking, and business intelligence visualization techniques commonly used in healthcare analytics.

---

## Project Objectives

* Analyze patient demographics and treatment data.
* Track healthcare KPIs such as treatment cost, readmission rate, and length of stay.
* Identify high-cost medical conditions and procedure trends.
* Evaluate patient satisfaction and healthcare outcomes.
* Build an interactive dashboard for data-driven decision making.

---

## Dataset

The dataset contains **984 patient records** with the following attributes:

* Patient ID
* Age
* Gender
* Medical Condition
* Procedure
* Treatment Cost
* Length of Stay
* Readmission Status
* Outcome
* Patient Satisfaction

---

## Tech Stack

### Data Analysis

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

### Business Intelligence

* Tableau Public

### Development Tools

* VS Code
* Git
* GitHub

---

## Key Performance Indicators (KPIs)

The dashboard tracks:

* Total Patients
* Average Patient Age
* Average Treatment Cost
* Average Length of Stay
* Readmission Rate

### KPI Summary

| Metric                 | Value       |
| ---------------------- | ----------- |
| Total Patients         | 984         |
| Average Age            | 53.75 Years |
| Average Treatment Cost | $8,367      |
| Average Length of Stay | 37.66 Days  |
| Readmission Rate       | 26.83%      |

---

## Exploratory Data Analysis

The following analyses were performed using Python:

* Gender Distribution Analysis
* Condition Distribution Analysis
* Procedure Distribution Analysis
* Cost Analysis by Condition
* Readmission Analysis
* Patient Satisfaction Analysis
* Length of Stay Analysis

Generated visualizations are stored in the `images/` directory.

---

## Tableau Dashboard Features

### Interactive Visualizations

* Condition Distribution
* Average Cost by Condition
* Readmission Analysis
* Patient Satisfaction Analysis
* Gender Distribution
* Length of Stay Analysis

### Interactive Filters

* Gender
* Condition
* Procedure
* Outcome
* Readmission Status

---

## Dashboard Preview

Tableau Public Dashboard:

**Live Dashboard:**
https://public.tableau.com/app/profile/rohan.pagadala/viz/HospitalPerformanceAnalyticsDashboard/HospitalPerformanceAnalyticsDashboard

---

## Project Structure

```text
Hospital-Performance-Dashboard

├── data
│   ├── hospital_data.csv
│   └── hospital_cleaned.csv

├── scripts
│   └── hospital_analysis.py

├── images
│   ├── condition_distribution.png
│   ├── cost_by_condition.png
│   ├── gender_distribution.png
│   ├── length_of_stay.png
│   ├── procedure_distribution.png
│   └── satisfaction.png

├── dashboard
│   └── HospitalDashboard.twbx

├── README.md

└── requirements.txt
```

---

## Key Insights

* The average patient age is 53.75 years.
* The average treatment cost is approximately $8,367 per patient.
* The readmission rate is 26.83%, indicating opportunities for improving post-discharge care.
* Certain medical conditions contribute significantly to overall healthcare costs.
* Patient satisfaction metrics provide insights into healthcare service quality.

---

## Future Improvements

* Predictive modeling for readmission risk.
* Cost forecasting using machine learning.
* Real-time healthcare monitoring dashboards.
* Advanced patient outcome analysis.
* Integration with SQL databases and cloud data sources.

---

## Author

**Rohan Pagadala**

---

This project was developed as part of a healthcare analytics and business intelligence portfolio to demonstrate data analysis, visualization, and decision-support capabilities.
