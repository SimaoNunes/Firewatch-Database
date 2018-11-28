SELECT distinct numprocessosocorro 
FROM (
	SELECT numprocessosocorro, nummeio, nomeentidade
	FROM acciona NATURAL JOIN eventoemergencia 
	WHERE moradalocal = 'Lisboa' AND instantechamada BETWEEN '2016-01-01 00:00:00' AND '2018-12-31 23:59:59') AS t1
WHERE NOT EXISTS (
	SELECT 1
	FROM audita
	WHERE numprocessosocorro = t1.numprocessosocorro AND nummeio = t1.nummeio AND nomeentidade = t1.nomeentidade)