-- How many admissions come from each city?
-- Needs a JOIN because city is in the patients table.
SELECT p.city,
       COUNT(*) AS admissions
FROM admissions a
JOIN patients p ON a.patient_id = p.patient_id
GROUP BY p.city
ORDER BY admissions DESC;