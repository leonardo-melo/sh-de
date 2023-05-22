WITH classified_scores AS (
    SELECT
        RANK() OVER (PARTITION BY patient_id, TO_CHAR(date, 'Month') ORDER BY date DESC) ordered_reviews,
        CASE WHEN (scores->'satisfaction')::INTEGER >= 8 THEN 'promoter' ELSE 'detractor' END as classification,
        TO_CHAR(date, 'Month') AS month
    FROM scores
)
SELECT 
    month,
    ROUND(
        (
            (SUM(CASE WHEN classification = 'promoter' THEN 1 ELSE 0 END) - SUM(CASE WHEN classification = 'detractor' THEN 1 ELSE 0 END)) 
            / count(1)::DECIMAL
        ) * 100
    , 0) as "NPS"
FROM classified_scores
WHERE ordered_reviews = 1
GROUP BY month;
