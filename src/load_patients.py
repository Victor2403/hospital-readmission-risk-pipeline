# Author: Victor Garcia
# Created: 6/11/2025

import pandas as pd
from sqlalchemy import create_engine, text

# CONFIG → adjust these to your setup
db_user = "postgres"
db_password = "password"  # you chose this
db_host = "localhost"
db_port = "5433"          # your server port
db_name = "synthea_healthcare"

# Postgres connection string
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Read patients.csv
patients_df = pd.read_csv('./data/raw/patients.csv')

# Select and rename columns for dim_patient
dim_patient_df = patients_df[[
    'Id',
    'BIRTHDATE',
    'DEATHDATE',
    'RACE',
    'ETHNICITY',
    'GENDER',
    'MARITAL',
    'STATE'
]].rename(columns={
    'Id': 'patient_id',
    'BIRTHDATE': 'birthdate',
    'DEATHDATE': 'deathdate',
    'RACE': 'race',
    'ETHNICITY': 'ethnicity',
    'GENDER': 'gender',
    'MARITAL': 'marital_status',
    'STATE': 'state'
})

# Optional → Convert date columns
dim_patient_df['birthdate'] = pd.to_datetime(dim_patient_df['birthdate'])
dim_patient_df['deathdate'] = pd.to_datetime(dim_patient_df['deathdate'], errors='coerce')

# Create dim_patient table
with engine.connect() as conn:
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS dim_patient (
        patient_id VARCHAR PRIMARY KEY,
        birthdate DATE,
        deathdate DATE,
        race VARCHAR,
        ethnicity VARCHAR,
        gender VARCHAR,
        marital_status VARCHAR,
        state VARCHAR
    );
    """
    conn.execute(text(create_table_sql))
    conn.commit()

# Load data into dim_patient (replace existing data for now)
dim_patient_df.to_sql('dim_patient', engine, if_exists='replace', index=False)

print("✅ dim_patient table loaded successfully.")