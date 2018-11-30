SELECT *
FROM meiocombate
EXCEPT
SELECT nummeio, nomeentidade
FROM meioapoio NATURAL JOIN acciona;