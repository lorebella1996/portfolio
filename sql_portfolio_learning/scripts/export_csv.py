#!/usr/bin/env python3
"""
Portfolio SQL Business - Export CSV
Esegue tutte le query e salva i risultati in file CSV separati
"""

import os
import sqlite3
import pandas as pd

# Import dal tuo script principale
from test_portfolio import estrai_commenti, carica_query_da_file

# Config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "..", "data", "business_data.db")
QUERIES_DIR = BASE_DIR
RESULTS_DIR = os.path.join(BASE_DIR, "..", "results")

# Main
def main():
    print("Database:", DB_PATH)
    print("Queries dir:", QUERIES_DIR)
    print("Results dir:", RESULTS_DIR)

    # Creo la cartella results se non esiste
    os.makedirs(RESULTS_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    try:
        sql_files = sorted(
            file for file in os.listdir(QUERIES_DIR)
            if file.endswith(".sql")
        )

        for file in sql_files:
            print(f"\n=== Export {file} ===")

            file_path = os.path.join(QUERIES_DIR, file)
            commenti, query = carica_query_da_file(file_path)

            try:
                df = pd.read_sql_query(query, conn)

                output_name = file.replace(".sql", ".csv")
                output_path = os.path.join(RESULTS_DIR, output_name)

                # Scrivo i commenti come header
                with open(output_path, "w", encoding="utf-8") as f:
                    for c in commenti:
                        f.write(f"# {c}\n")

                df.to_csv(output_path, mode="a", index=False)

                print(f"Salvato: {output_name} ({len(df)} righe)")

            except Exception as e:
                print(f"Errore in {file}: {e}")

    finally:
        conn.close()
        print("\nConnessione al database chiusa.")

# Entry point
if __name__ == "__main__":
    main()
