import pandas as pd

def build_dataset (df: pd.DataFrame) -> pd.DataFrame:
    '''
    Build dataset for model training.
    '''

    df = df.copy()

    # Example feature engineering
    df['win'] = (df['goals_for'] > df['goals_against']).astype(int)
    
    dataset = df[['team', 'date', 'momentum', 'win']]

    return dataset