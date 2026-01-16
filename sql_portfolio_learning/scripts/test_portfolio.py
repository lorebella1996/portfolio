#!/usr/bin/env python3
"""
Portfolio SQL Business
Esegue tutte le query SQL nella cartella scripts
Mostra risultati e descrizione (commenti SQL)
"""

import os
import sqlite3
import pandas as pd

# Utility
def estrai_commenti(sql_text):
    """
    Estrae i commenti SQL (--) e la query vera.
    """
    commenti = []
    query_lines = []

    for line in sql_text.splitlines():
        if line.strip().startswith("--"):
            commenti.append(line.strip().replace("--", "").strip())
        else:
            query_lines.append(line)

    return commenti, "\n".join(query_lines)

# Configurazione path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "data", "business_data.db")
QUERIES_DIR = BASE_DIR

# Main
def main():
    print("Database:", DB_PATH)
    print("Queries dir:", QUERIES_DIR)

    conn = sqlite3.connect(DB_PATH)

    try:
        sql_files = sorted(
            file for file in os.listdir(QUERIES_DIR)
            if file.endswith(".sql")
        )

        for file in sql_files:
            print(f"\n=== {file} ===")

            file_path = os.path.join(QUERIES_DIR, file)

            with open(file_path, "r", encoding="utf-8") as f:
                sql_text = f.read()

            commenti, query = estrai_commenti(sql_text)

            if commenti:
                print("Descrizione:")
                for c in commenti:
                    print(f"  • {c}")

            try:
                df = pd.read_sql_query(query, conn)
                print("\nRisultato:")
                print(df)

            except Exception as e:
                print(f"\nErrore query: {e}")

    finally:
        conn.close()
        print("\nConnessione al database chiusa.")

def carica_query_da_file(file_path):
    """
    Legge un file SQL e restituisce (commenti, query)
    """
    with open(file_path, "r", encoding="utf-8") as f:
        sql_text = f.read()

    return estrai_commenti(sql_text)


# Entry point
if __name__ == "__main__":
    main()
