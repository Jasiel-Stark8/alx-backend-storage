-- IMPORT AND SORT FANS

SELECT origin, SUM(fans) AS nbfans
FROM metal_bands
GROUP BY origin
ORDER BY nbfans DESC;
