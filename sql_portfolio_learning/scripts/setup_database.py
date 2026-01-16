#!/usr/bin/env python3
"""
Setup database per Portfolio SQL Business
Crea database SQLite con dati business realistici
"""

import sqlite3
import random
from datetime import datetime, timedelta

def create_database():
    """Crea database con tabelle business"""
    
    # Connessione al database
    conn = sqlite3.connect('../data/business_data.db')
    cursor = conn.cursor()
    
    print("Database collegato! Ora creiamo le tabelle...")


# TABELLA CLIENTI
    cursor.execute('''
    CREATE TABLE clienti (
        id_cliente INTEGER PRIMARY KEY,
        ragione_sociale TEXT NOT NULL,
        partita_iva TEXT UNIQUE,
        settore TEXT,
        citta TEXT,
        regione TEXT,
        data_registrazione DATE,
        fatturato_annuo DECIMAL(12,2),
        categoria TEXT
    )
    ''')
    
    print("✓ Tabella clienti creata")

# INSERIMENTO DATI CLIENTI
    clienti_data = [
        (1, 'Costruzioni Marinelli SpA', '12345678901', 'Costruzioni', 'Roma', 'Lazio', '2020-03-15', 2500000.00, 'GRANDE'),
        (2, 'Offshore Engineering Srl', '98765432109', 'Petrolio&Gas', 'Genova', 'Liguria', '2019-06-20', 8500000.00, 'ENTERPRISE'),
        (3, 'Infrastrutture Sud Srl', '11122334455', 'Infrastrutture', 'Napoli', 'Campania', '2021-01-10', 1200000.00, 'MEDIA'),
        (4, 'Ponti e Viadotti SpA', '55566677788', 'Costruzioni', 'Milano', 'Lombardia', '2018-11-05', 4200000.00, 'GRANDE'),
        (5, 'Servizi Portuali Livorno', '99988877766', 'Logistica', 'Livorno', 'Toscana', '2022-02-28', 800000.00, 'PICCOLA'),
        (6, 'Drilling Tech Solutions', '44433322211', 'Petrolio&Gas', 'Ravenna', 'Emilia-Romagna', '2020-09-12', 6800000.00, 'ENTERPRISE'),
        (7, 'Calcestruzzo Adriatico', '77788899900', 'Materiali', 'Pescara', 'Abruzzo', '2021-05-17', 950000.00, 'PICCOLA'),
        (8, 'Sistemi Offshore Italia', '33344455566', 'Petrolio&Gas', 'Trieste', 'Friuli-Venezia Giulia', '2019-08-23', 5200000.00, 'GRANDE'),
        (9, 'Tunnel Engineering Group', '66677788899', 'Infrastrutture', 'Torino', 'Piemonte', '2020-12-03', 3100000.00, 'GRANDE'),
        (10, 'Maritime Services SpA', '88899900011', 'Logistica', 'Palermo', 'Sicilia', '2021-07-14', 1400000.00, 'MEDIA')
    ]

    cursor.executemany('INSERT INTO clienti VALUES (?,?,?,?,?,?,?,?,?)', clienti_data)
    print("✓ Clienti di esempio inseriti")


# TABELLA PRODOTTI
    cursor.execute('''
    CREATE TABLE prodotti (
        id_prodotto INTEGER PRIMARY KEY,
        codice_prodotto TEXT UNIQUE NOT NULL,
        nome_prodotto TEXT NOT NULL,
        categoria TEXT,
        prezzo_unitario DECIMAL(10,2),
        costo_produzione DECIMAL(10,2),
        fornitore TEXT,
        stato TEXT DEFAULT 'ATTIVO'
    )
    ''')
    
    print("✓ Tabella prodotti creata")

# INSERIMENTO DATI PRODOTTI
    prodotti_data = [
        (1, 'ENG-001', 'Software Progettazione Strutturale', 'Software', 12500.00, 3200.00, 'TechSoft Italia', 'ATTIVO'),
        (2, 'ENG-002', 'Sistema Monitoraggio Offshore', 'Hardware', 45000.00, 18000.00, 'Marine Tech', 'ATTIVO'),
        (3, 'ENG-003', 'Consulenza Ingegneria Civile', 'Servizi', 850.00, 420.00, 'Interno', 'ATTIVO'),
        (4, 'ENG-004', 'Certificazione Strutturale', 'Servizi', 2200.00, 800.00, 'Cert Italia', 'ATTIVO'),
        (5, 'ENG-005', 'Sensori Vibrazione Ponti', 'Hardware', 8500.00, 4200.00, 'SensorTech', 'ATTIVO'),
        (6, 'ENG-006', 'Software Analisi Petrolifere', 'Software', 28000.00, 8900.00, 'GeoSoft Pro', 'ATTIVO'),
        (7, 'ENG-007', 'Training Sicurezza Offshore', 'Formazione', 1200.00, 450.00, 'Safety Academy', 'ATTIVO'),
        (8, 'ENG-008', 'Kit Strumentazione Marina', 'Hardware', 15600.00, 7800.00, 'Nautical Instruments', 'ATTIVO'),
        (9, 'ENG-009', 'Audit Conformità Impianti', 'Servizi', 3500.00, 1200.00, 'Compliance Pro', 'ATTIVO'),
        (10, 'ENG-010', 'Software Simulazione Fluidi', 'Software', 18500.00, 6200.00, 'FluidDyn Systems', 'ATTIVO'),
    ]
    
    cursor.executemany('INSERT INTO prodotti VALUES (?,?,?,?,?,?,?,?)', prodotti_data)
    print("✓ Prodotti di esempio inseriti")


# TABELLA VENDITE
    cursor.execute('''
    CREATE TABLE vendite (
        id_vendita INTEGER PRIMARY KEY,
        id_cliente INTEGER,
        id_prodotto INTEGER,
        data_vendita DATE,
        quantita INTEGER,
        prezzo_vendita DECIMAL(10,2),
        sconto_percentuale DECIMAL(5,2) DEFAULT 0,
        importo_totale DECIMAL(12,2),
        canale_vendita TEXT,
        agente_vendita TEXT,
        FOREIGN KEY (id_cliente) REFERENCES clienti (id_cliente),
        FOREIGN KEY (id_prodotto) REFERENCES prodotti (id_prodotto)
    )
    ''')
    
    print("✓ Tabella vendite creata")

# GENERAZIONE VENDITE - VERSIONE SEMPLICE
    vendite_data = []
    vendita_id = 1
    
    # Generiamo 1500 vendite casuali
    for i in range(1500):
        id_cliente = random.randint(1, 10)
        id_prodotto = random.randint(1, 10)
        
        # Data casuale negli ultimi 2 anni
        giorni_fa = random.randint(1, 730)
        data_vendita = (datetime.now() - timedelta(days=giorni_fa)).strftime('%Y-%m-%d')
        
        quantita = random.randint(1, 5)
        
        # Prezzi fissi semplici
        prezzi = [12500, 45000, 850, 2200, 8500, 28000, 1200, 15600, 3500, 18500]
        prezzo = prezzi[id_prodotto - 1]
        
        # Sconto occasionale
        if random.random() < 0.3:  # 30% possibilità sconto
            sconto = random.choice([5, 10, 15])
            prezzo = prezzo * (1 - sconto/100)
        else:
            sconto = 0
        
        importo_totale = prezzo * quantita
        
        canale = random.choice(['DIRETTO', 'PARTNER', 'E-COMMERCE'])
        agente = random.choice(['Mario Rossi', 'Giulia Bianchi', 'Andrea Verdi'])

        vendite_data.append((vendita_id, id_cliente, id_prodotto, data_vendita, 
                        quantita, prezzo, sconto, importo_totale, canale, agente))
        vendita_id += 1


# Inserimento vendite nel database
    cursor.executemany('INSERT INTO vendite VALUES (?,?,?,?,?,?,?,?,?,?)', vendite_data)
    print("✓ Vendite generate e inserite")
    
    # Salvataggio e chiusura
    conn.commit()
    conn.close()
    
    print(f"✅ Database creato! Inserite {len(vendite_data)} vendite")

# Esecuzione principale
if __name__ == "__main__":
    create_database()
    