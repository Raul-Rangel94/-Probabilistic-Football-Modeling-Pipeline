import pandas as pd

def baseline_win_rate(df: pd.DataFrame) -> float:
    """
    Compute a baseline win rate based on simple momentum thresholding.
    """
    
    return df['win'].mean()
