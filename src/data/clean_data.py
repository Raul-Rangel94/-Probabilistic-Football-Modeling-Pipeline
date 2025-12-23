import pandas as pd

def clean_matches(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean Liga MX match data.
    
    Steps:
    - Parse dates
    - Ensure numeric goal columns
    - Drop rows with missing critical data
    - Sort matches chronologically
    """

    df = df.copy()

    #Convert date column
    df["date"] = pd.to_datetime(df["date"], errors='coerce')
    
    #Create goal columns from result
    df[['home_goals', 'away_goals']] = df['result'].str.split('-', expand=True)

    # Convert goal columns to numeric, forcing errors to NaN
    df["home_goals"] = pd.to_numeric(df["home_goals"], errors='coerce')
    df["away_goals"] = pd.to_numeric(df["away_goals"], errors='coerce')

    # Drop rows with missing critical data
    df = df.dropna(subset=["date", "home_goals", "away_goals"])

    # Sort by date
    df = df.sort_values(by="date").reset_index(drop=True)
    
    return df