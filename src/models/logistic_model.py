import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_logistic_model(df: pd.DataFrame):
    '''
    Train a logistic regression model using momentum as feature.
    '''
    X = df[['momentum']]
    y = df['win']

    model = LogisticRegression()
    model.fit(X, y)

    return model
