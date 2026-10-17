-- How many admissions are there in each age group?
-- Age = year of admission minus birth year.
WITH admission_ages AS (
    SELECT a.admission_id,
           CAST(strftime('%Y', a.admit_date) AS INTEGER) - p.birth_year AS age
    FROM admissions a
    JOIN patients p ON a.patient_id = p.patient_id
)
SELECT CASE
           WHEN age < 18 THEN '0-17'
           WHEN age < 40 THEN '18-39'
           WHEN age < 65 THEN '40-64'
           ELSE '65+'
       END AS age_group,
       COUNT(*) AS admissions
FROM admission_ages
GROUP BY age_group
ORDER BY MIN(age);