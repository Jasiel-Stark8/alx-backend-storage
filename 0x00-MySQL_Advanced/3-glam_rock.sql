-- Script to list and rank Glam rock bands by longevity

SELECT band_name,
    CASE
        WHEN split = '0' THEN 20022 - formed
        ELSE split - formed
    END AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
