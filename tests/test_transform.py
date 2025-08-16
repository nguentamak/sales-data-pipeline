import pandas as pd
from src.transform import transform

def test_transform():
    df = pd.DataFrame({"quantity":[2], "price":[10]})
    df_transformed = transform(df)
    assert "total" in df_transformed.columns
    assert df_transformed["total"].iloc[0] == 20
