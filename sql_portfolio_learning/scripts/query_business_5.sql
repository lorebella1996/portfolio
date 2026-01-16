-- Voglio analizzare l'efficacia del nostro team vendita e dei diversi canali. Chi sono i nostri migliori performer? Quale canale funziona meglio?

SELECT
agente_vendita,
canale_vendita,
sum(quantita) AS quantità_totali_vendute,
count(canale_vendita) AS numero_ordini_venduti,
avg(quantita) AS media_quantità_x_ordine,
avg(prezzo_vendita) AS media_prezzo_x_ordine,
sum(importo_totale) AS totale_incasso

FROM
vendite

GROUP BY
canale_vendita,
agente_vendita

ORDER BY
totale_incasso DESC