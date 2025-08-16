import pandas as pd

def ingest(file_path: str) -> pd.DataFrame:
    """Lecture d'un fichier CSV et retour sous forme de DataFrame"""
    return pd.read_csv(file_path)
