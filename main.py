import pandas as pd
from sklearn.model_selection import train_test_split

# Data
from src.data.load_data import load_matches
from src.data.clean_data import clean_matches
from src.data.team_view import build_team_view
from src.features.build_features import build_dataset
from src.features.momentum import compute_momentum
from src.features.form import compute_form

# Models
from src.models.baseline import baseline_win_rate
from src.models.logistic_model import train_logistic_model

# Evaluation
from src.evaluation.evaluate import evaluate_model, evaluate_baseline

'''
def main():
    # 1️⃣ Load raw data
    df_matches = load_matches("data/raw/2024mx1.csv")
    df_matches = clean_matches(df_matches)
    df_matches = build_team_view(df_matches)

    # 2️⃣ Build ML dataset (features + target)
    df_matches = compute_form(df_matches)
    df_matches = compute_momentum(df_matches)
    df_dataset = build_dataset(df_matches)

    # Features and target
    X = df_dataset[["momentum"]]
    y = df_dataset["win"]

    # 3️⃣ Train / Test split

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
    )

    # 4️⃣ Baseline (computed ONLY on train)
    baseline_prob = float(y_train.mean())

    # 5️⃣ Train logistic regression
    model = train_logistic_model(
        pd.concat([X_train, y_train], axis=1)
    )

    # 6️⃣ Evaluate model
    model_results = evaluate_model(model, X_test, y_test)
    baseline_loss = evaluate_baseline(baseline_prob, y_test)

    # 7️⃣ Print results
    print("=== MODEL EVALUATION ===")
    print(f"Accuracy: {model_results['accuracy']:.3f}")
    print(f"Log-loss: {model_results['log_loss']:.3f}")
    print(f"Baseline log-loss: {baseline_loss:.3f}")

    if model_results["log_loss"] < baseline_loss:
        print("✅ Model improves over baseline")
    else:
        print("❌ Model does NOT improve over baseline")


if __name__ == "__main__":
    main()
'''
'''
def build_dataset(raw_matches_df):
    team_view = build_team_view(...)
    features = build_features(team_view)
    X, y = split_target(features)
    return X, y
    '''