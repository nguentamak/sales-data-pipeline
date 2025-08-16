def transform(df):
    """Nettoyage et calcul du chiffre d'affaires total"""
    df = df.dropna()
    df['total'] = df['quantity'] * df['price']
    return df
