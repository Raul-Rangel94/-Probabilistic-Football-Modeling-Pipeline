import numpy as np
import pandas as pd

def compute_form(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Compute team offensive form using log transformation.
    '''

    df.copy()

    df ['form'] = np.log1p(df['goals_for'])
    return df
