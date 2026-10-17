-- Average hospital stay (in days) for each diagnosis
SELECT diagnosis,
       COUNT(*) AS admissions,
       ROUND(AVG(julianday(discharge_date) - julianday(admit_date)), 1) AS avg_stay_days
FROM admissions
GROUP BY diagnosis
ORDER BY avg_stay_days DESC;