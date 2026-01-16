-- Voglio identificare i clienti a rischio churn. Chi non ci compra da più tempo? Dobbiamo attivarci per recuperarli

SELECT
vendite.id_cliente,
clienti.ragione_sociale,
max(vendite.data_vendita) AS ultima_vendita,
(julianday('now') - julianday(max(vendite.data_vendita))) AS giorni_ultima_vendita,
CASE
WHEN (julianday('now') - julianday(max(vendite.data_vendita))) < 7 THEN 'zero rischio'
WHEN (julianday('now') - julianday(max(vendite.data_vendita))) BETWEEN 7 AND 14 THEN 'basso rischio'
WHEN (julianday('now') - julianday(max(vendite.data_vendita))) BETWEEN 14 AND 21 THEN 'medio rischio'
WHEN (julianday('now') - julianday(max(vendite.data_vendita))) > 21 THEN 'alto rischio'
END AS rischio_churn

FROM
vendite

INNER JOIN clienti
ON clienti.id_cliente = vendite.id_cliente

GROUP BY vendite.id_cliente

ORDER BY giorni_ultima_vendita DESC