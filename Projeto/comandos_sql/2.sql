SELECT nomeentidade
FROM (
	SELECT distinct numprocessosocorro, nomeentidade
	FROM acciona NATURAL JOIN eventoemergencia
	WHERE instantechamada BETWEEN '2018-06-21 00:00:00' AND '2018-09-23 23:59:59') as t1
GROUP BY nomeentidade
HAVING count(*) >= ALL (
	SELECT count(*)
	FROM (
		SELECT distinct numprocessosocorro, nomeentidade
		FROM acciona NATURAL JOIN eventoemergencia
		WHERE instantechamada BETWEEN '2018-06-21 00:00:00' AND '2018-09-23 23:59:59') as t2
	GROUP BY nomeentidade);