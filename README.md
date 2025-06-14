# Hospital Readmission Risk Pipeline

This project simulates a production-grade healthcare data engineering pipeline for predicting 30-day hospital readmission risk. The pipeline is designed to demonstrate best practices for handling sensitive healthcare data, building scalable ETL workflows, modeling patient data, and visualizing key outcomes.

**Key Features:**
- End-to-end ETL pipeline using synthetic HIPAA-safe electronic health records (EHR) data (generated via [Synthea](https://synthetichealth.github.io/synthea/))
- Data orchestration with Apache Airflow (Extract → Transform → Load)
- Data modeling with Python and PostgreSQL (star schema)
- Machine learning model for readmission risk (logistic regression / random forest)
- Interactive BI dashboard in Tableau Public
- Simulated HIPAA-safe data transfer pipeline (encrypted raw files → staged → warehouse)

**Tech Stack:**
- Python (Pandas, SQLAlchemy, Scikit-learn)
- Apache Airflow
- PostgreSQL
- Tableau Public
- Synthea (synthetic EHR data)

**Why This Project?**
Hospital readmission is a key quality metric in healthcare, with significant financial and clinical implications. Building a predictive pipeline for readmission risk is a realistic, in-demand use case for healthcare data engineers.

**Disclaimer:**  
All data used in this project is fully synthetic and HIPAA-safe, generated by Synthea.

---

## Project Structure

hospital-readmission-risk-pipeline/
├── README.md
├── data/ # raw and processed data
├── dags/ # Airflow DAGs
├── src/ # Python ETL scripts
├── models/ # ML models and notebooks
├── dashboards/ # Tableau workbook and assets
├── requirements.txt
└── .gitignore

---

## Next Steps
- Generate first synthetic EHR dataset
- Design data model and schema
- Build initial ETL flow with Airflow
- Develop predictive ML model
- Publish interactive dashboard to Tableau Public

---
