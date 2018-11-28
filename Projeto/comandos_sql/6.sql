SELECT nomeentidade
FROM meiocombate NATURAL JOIN acciona
GROUP BY nomeentidade
HAVING count(distinct numprocessosocorro) = (
	SELECT count(distinct numprocessosocorro)
	FROM meiocombate NATURAL JOIN acciona)