"""
Creates a fake hospital database (hospital.db).
All data is randomly generated. No real patients are involved.
"""
import random
import sqlite3
from datetime import date, timedelta

random.seed(42)  # same random data every time

conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS admissions;
DROP TABLE IF EXISTS patients;

CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    sex TEXT,
    birth_year INTEGER,
    city TEXT
);

CREATE TABLE admissions (
    admission_id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    admit_date TEXT,
    discharge_date TEXT,
    department TEXT,
    diagnosis TEXT,
    outcome TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
""")

cities = ["Delhi", "Mumbai", "Bengaluru", "Chennai", "Kolkata"]
patients = [
    (pid, random.choice(["F", "M"]), random.randint(1940, 2015), random.choice(cities))
    for pid in range(1, 501)
]
cur.executemany("INSERT INTO patients VALUES (?, ?, ?, ?)", patients)

dept_diagnoses = {
    "Cardiology": ["Heart failure", "Hypertension", "Myocardial infarction"],
    "Endocrinology": ["Type 2 diabetes", "Thyroid disorder"],
    "Respiratory": ["Pneumonia", "COPD", "Asthma"],
    "Gastroenterology": ["Gastroenteritis", "Liver disease"],
    "Neurology": ["Stroke", "Epilepsy"],
}
typical_stay = {
    "Heart failure": 6, "Hypertension": 3, "Myocardial infarction": 7,
    "Type 2 diabetes": 4, "Thyroid disorder": 3,
    "Pneumonia": 6, "COPD": 5, "Asthma": 3,
    "Gastroenteritis": 3, "Liver disease": 7,
    "Stroke": 9, "Epilepsy": 4,
}

admissions = []
admission_id = 1
for pid in range(1, 501):
    for _ in range(random.choice([1, 1, 1, 2, 2, 3])):
        dept = random.choice(list(dept_diagnoses))
        diagnosis = random.choice(dept_diagnoses[dept])
        admit = date(2024, 1, 1) + timedelta(days=random.randint(0, 700))
        stay = max(1, int(random.gauss(typical_stay[diagnosis], 2)))
        discharge = admit + timedelta(days=stay)
        outcome = random.choices(
            ["Recovered", "Transferred", "Died"], weights=[90, 7, 3]
        )[0]
        admissions.append((admission_id, pid, admit.isoformat(),
                           discharge.isoformat(), dept, diagnosis, outcome))
        admission_id += 1

cur.executemany("INSERT INTO admissions VALUES (?, ?, ?, ?, ?, ?, ?)", admissions)
conn.commit()

print(f"Created {len(patients)} patients and {len(admissions)} admissions.")
conn.close()