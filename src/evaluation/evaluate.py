import numpy as np
from sklearn.metrics import log_loss

def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained classification model.
    """
    #Accuracy (Correct decisions)
    accuracy = model.score(X_test, y_test)

    # Predict probabilities
    y_prob = model.predict_proba(X_test)[:, 1]

    # Log Loss (Quality of probabilities)
    loss = log_loss(y_test, y_prob)
    
    return {
        'accuracy': accuracy,
        'log_loss': loss
    }

def evaluate_baseline(baseline_prob, y_test):    
    y_test_np = y_test.to_numpy()  # conversión explícita

    baseline_preds = np.full(
        shape=y_test_np.shape,
        fill_value=baseline_prob,
        dtype=float
    )

    loss = log_loss(y_test_np, baseline_preds)
    return loss