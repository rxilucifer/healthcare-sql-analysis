# Healthcare SQL Analysis

Practice SQL queries on a fake hospital database, written to answer
real hospital questions like length of stay and admissions by department.

**All data is randomly generated. No real patients are involved.**

## How to run
1. `pip install -r requirements.txt`
2. `python make_data.py` (creates the fake database `hospital.db`)
3. `python run_query.py queries/01_admissions_by_department.sql`

## Queries so far
| File | Question |
|------|----------|
| `01_admissions_by_department.sql` | How many admissions does each department have? |
| `02_length_of_stay_by_diagnosis.sql` | What is the average stay for each diagnosis? |

## Tables
- `patients`: patient_id, sex, birth_year, city
- `admissions`: admission_id, patient_id, admit_date, discharge_date, department, diagnosis, outcome