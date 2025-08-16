import os
import pandas as pd
from src.load import load

def test_load():
    df = pd.DataFrame({"quantity":[2], "price":[10], "total":[20]})
    db_path = "test_sales.db"
    load(df, db_path)
    assert os.path.exists(db_path)
    os.remove(db_path)
