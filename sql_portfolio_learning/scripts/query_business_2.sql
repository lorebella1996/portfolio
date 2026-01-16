-- Vorrei capire quali prodotti performano meglio. Mi serve un'analisi di performance e marginalità per decidere su cosa puntare

SELECT
vendite.id_prodotto,
prodotti.nome_prodotto,
vendite.prezzo_vendita,
(prodotti.prezzo_unitario - prodotti.costo_produzione) as margine_prodotto,
avg(100*(prodotti.prezzo_unitario - prodotti.costo_produzione)/prodotti.prezzo_unitario) as percentuale_margine,
sum(vendite.quantita) as somma_ordini,
avg(vendite.sconto_percentuale) as sconto_medio,
sum((prodotti.prezzo_unitario - prodotti.costo_produzione) * vendite.quantita * (1 - (vendite.sconto_percentuale / 100.0))) as margine_totale

FROM vendite

INNER JOIN
prodotti
on
vendite.id_prodotto = prodotti.id_prodotto

GROUP BY vendite.id_prodotto
ORDER BY percentuale_margine DESC
