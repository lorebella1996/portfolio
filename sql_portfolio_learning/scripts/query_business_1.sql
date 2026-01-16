-- Quali sono i nostri TOP 5 clienti per fatturato negli ultimi 12 mesi?

SELECT
vendite.id_cliente,
clienti.ragione_sociale,
sum(vendite.importo_totale) as totale_vendite

FROM vendite

INNER JOIN
clienti ON vendite.id_cliente = clienti.id_cliente

WHERE vendite.data_vendita > date('now', '-12 months')

group by
vendite.id_cliente,
clienti.ragione_sociale
ORDER BY totale_vendite desc
LIMIT 5