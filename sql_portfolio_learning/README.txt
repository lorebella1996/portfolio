PORTFOLIO SQL BUSINESS - DATA SPECIALIST
========================================

OVERVIEW
--------
Progetto SQL per portfolio Junior Data Specialist.
Database business con clienti engineering/offshore e 5 query operative.

CONTENUTO
---------
- data/business_data.db          -> Database SQLite con dati business
- scripts/setup_database.py      -> Crea database e popola dati
- scripts/query_business_*.sql   -> 5 query SQL business-oriented  
- scripts/test_portfolio.py      -> Esegue query e mostra risultati
- scripts/export_csv.py          -> Esporta risultati in CSV
- results/query_business_*.csv   -> Output query per analisi

UTILIZZO
--------
1. Setup database:
   python scripts/setup_database.py

2. Test query interattivo:
   python scripts/test_portfolio.py

3. Export CSV per presentazioni:
   python scripts/export_csv.py

QUERY BUSINESS
--------------
1. Top 5 clienti per fatturato
2. Analisi prodotti e marginalità  
3. Trend vendite mensili
4. Clienti a rischio churn
5. Performance agenti e canali

DATI
----
- 10 clienti settore engineering/offshore
- 10 prodotti (software/hardware/servizi)
- 1500+ vendite ultimi 24 mesi