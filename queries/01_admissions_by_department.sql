-- How many admissions does each department have?
SELECT department,
       COUNT(*) AS admissions
FROM admissions
GROUP BY department
ORDER BY admissions DESC;