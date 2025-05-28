from src.data_loader import load_news_data
import pandas as pd

def test_data_loading():
    df = load_news_data()
    assert not df.empty, "Data failed to load"
    assert 'headline' in df.columns, "Missing headline column"