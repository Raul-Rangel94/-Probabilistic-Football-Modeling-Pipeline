# Probabilistic Football Modeling Pipeline (Liga MX)

This project focuses on building a **robust and interpretable data pipeline** for probabilistic football modeling using Liga MX match data.

The objective is **not** to predict exact scores, but to design a clean, reusable, and football-aware dataset that can support **probabilistic analysis and decision-making**.

---

## 🎯 Project Goals

- Build a structured **pre-match data pipeline**
- Design football-informed features (form, momentum, relative strength)
- Ensure data consistency and interpretability
- Produce datasets suitable for **probabilistic models**, not just point predictions

Models are treated as **downstream consumers** of the data pipeline.

---

## ⚙️ Current Scope

- **Competition:** Liga MX  
- **Season:** Clausura 2024  
- **Granularity:** One record per match (home vs away)  
- **Time window:** Last 5 matches (rolling)

Using a single season helps reduce structural noise caused by major changes in squads, coaches, and context.

---

## 🧠 Feature Engineering (Pre-Match)

Each match is represented with separate features for home and away teams:

- `home_form`, `away_form`  
- `home_momentum`, `away_momentum`

Relative features are also included:

- `form_diff`  
- `momentum_diff`

**Form** captures recent performance level, while  
**Momentum** captures the direction of recent performance (trend).

All features are computed strictly using **pre-match information**.

---

## 🎯 Target Definition

Current target:

- `home_win = 1` → home team wins  
- `home_win = 0` → draw or away win  

This setup is intentionally simple and scalable to:
- multi-class outcomes (W / D / L)
- goal-based probabilistic models
- Bayesian or hierarchical approaches

---

## 📊 Modeling Philosophy

Football is a high-variance sport.  
Predicting exact results is neither realistic nor professional.

This project focuses on:
- **probability estimation**
- **calibration and reliability**
- **zone-based and ranking-based interpretations**

Accuracy alone is not treated as a sufficient metric.

---

## 🔬 Validation & Analysis

Features and model outputs are validated through:
- distribution analysis
- sanity checks with football logic
- probability bins and reliability curves

This ensures the model’s probabilities are **meaningful**, not just numerically correct.

---

## 🚧 Project Status

Work in progress.

Current focus areas:
- feature validation and robustness
- probability calibration
- zone-based interpretation of predictions

---

## 🔜 Next Steps

- Compare probabilistic models (logistic regression, trees, SVM)
- Extend to multi-output modeling:
  - match outcome probability
  - match intensity (active vs low-tempo games)
- Introduce historical and contextual adjustments

