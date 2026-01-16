-- Ho bisogno di vedere i trend di vendita mensili per gli ultimi 12 mesi. Voglio capire se stiamo crescendo e identificare stagionalità

SELECT
strftime('%m', data_vendita) as mese_vendita,
COUNT(id_prodotto) AS numero_ordini,
sum(quantita) as totale_vendite,
sum(importo_totale) as totale_fatturato

FROM vendite

WHERE data_vendita > date('now', '-12 months')

GROUP BY
mese_vendita

ORDER BY
mese_vendita
ASC