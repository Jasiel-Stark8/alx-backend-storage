-- IMPORT AND SORT FANS

SELECT origin, SUM(fans) AS nbfans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC
