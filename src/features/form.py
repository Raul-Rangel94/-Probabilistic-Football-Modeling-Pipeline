import numpy as np
import pandas as pd

def compute_form(
    df: pd.DataFrame,
    window: int = 5
) -> pd.DataFrame:
    """
    Compute team form as normalized rolling average of points.
    """

    df = df.copy()
    df = df.sort_values(['team', 'date'])

    df['form'] = (
        df
        .groupby('team')['points']
        .transform(
            lambda x: x.rolling(window=window, min_periods=1).sum() / (3 * window)
        )
    )

    return df
