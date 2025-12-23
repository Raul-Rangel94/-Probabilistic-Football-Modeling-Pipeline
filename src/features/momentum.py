import pandas as pd

def compute_momentum(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Compute team momentum as discrete derivative of form.
    '''

    df = df.copy()

    df['momentum'] = (
        df
        .groupby('team')['form']
        .diff()
        .fillna(0)
    )

    return df