-- IMPORT AND SORT FANS
-- non unique fans

SELECT origin, SUM(fans) AS nbfans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
