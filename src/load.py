import sqlite3

def load(df, db_path="sales.db"):
    """Chargement des données transformées dans SQLite"""
    conn = sqlite3.connect(db_path)
    df.to_sql('sales', conn, if_exists='replace', index=False)
    conn.close()
