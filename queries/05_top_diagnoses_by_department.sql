-- Top 2 diagnoses in each department, by number of admissions
WITH diagnosis_counts AS (
    SELECT department,
           diagnosis,
           COUNT(*) AS admissions
    FROM admissions
    GROUP BY department, diagnosis
),
ranked AS (
    SELECT department,
           diagnosis,
           admissions,
           RANK() OVER (
               PARTITION BY department
               ORDER BY admissions DESC
           ) AS rank_in_department
    FROM diagnosis_counts
)
SELECT department,
       diagnosis,
       admissions,
       rank_in_department
FROM ranked
WHERE rank_in_department <= 2
ORDER BY department, rank_in_department;