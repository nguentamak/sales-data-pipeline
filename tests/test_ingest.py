from src.ingest import ingest

def test_ingest():
    df = ingest("data/sample_sales.csv")
    assert not df.empty
    assert "product" in df.columns
