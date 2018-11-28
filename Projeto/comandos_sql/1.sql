SELECT numprocessosocorro
FROM acciona
GROUP BY numprocessosocorro
HAVING count(*) >= ALL (
    SELECT count(*)
    FROM acciona
    GROUP BY numprocessosocorro
)