SELECT count(*)
FROM segmentovideo NATURAL JOIN video NATURAL JOIN vigia
WHERE duracao > 1 AND moradalocal = 'Monchique' AND datahorainicio BETWEEN '2018-08-01 00:00:00' AND '2018-08-31 23:59:59'