# Probabilistic Football Modeling Pipeline (Liga MX)

This project focuses on building a robust, interpretable, and football-aware data pipeline for probabilistic modeling using Liga MX match data.

Rather than predicting exact scores or deterministic outcomes, the goal is to design a clean and reusable **pre-match dataset** that supports probability estimation, calibration analysis, and decision-making under uncertainty.

The project treats **models as downstream consumers of the data pipeline**, not as the center of the system.

---

## 🎯 Project Goals

- Build a structured and reproducible **pre-match data pipeline**
- Design **football-informed features** (form, momentum, contextual signals)
- Ensure **temporal correctness** and strict pre-match availability
- Produce datasets suitable for **probabilistic evaluation**, not point prediction
- Emphasize **calibration, reliability, and interpretability**
- Establish a strong probabilistic baseline for comparison

---

## ⚙️ Scope & Data

- **Competition:** Liga MX  
- **Granularity:** One record per match (home vs away)  
- **Temporal structure:** Rolling, pre-match windows  
- **Feature availability:** Strictly pre-kickoff (no leakage)

While some exploratory notebooks focus on controlled seasonal subsets, the **pipeline and validation strategy are multi-season and temporally consistent by design**.

---

## 🧠 Feature Engineering (Pre-Match)

Each match is represented using **separate home and away signals**:

- `home_form`, `away_form`
- `home_momentum`, `away_momentum`
- weighted variants of form (recent performance emphasis)
- contextual features (e.g. home advantage)

Relative features are also included:

- `form_diff`
- `momentum_diff`
- `home_advantage_diff`

### Conceptual Roles

- **Form** captures recent performance level  
- **Momentum** captures direction and trend  
- **Contextual features** adjust expectations rather than dominate them  

All features are computed using **only information available before kickoff**, preventing leakage.

---

## 🎯 Target Definition

Current target:

- `home_win = 1` → home team wins  
- `home_win = 0` → draw or away win  

This binary setup is intentionally simple and extensible to:

- multi-class outcomes (W / D / L)
- goal-based probabilistic models
- Bayesian or hierarchical extensions

---

## 📊 Modeling Philosophy

Football is a **high-variance, low-signal system**.

Exact outcome prediction is neither realistic nor informative.

This project prioritizes:

- **probability estimation**
- **calibration and reliability**
- **zone-based interpretation**
- **temporal validity**

Accuracy alone is not treated as a sufficient metric.

---

## 🔬 Validation & Evaluation

Model outputs are evaluated using:

- **temporal cross-validation (expanding window)**
- **log loss and Brier score**
- **reliability curves**
- **probability bucket (zone) analysis**

A central finding of the project is that:

> Extreme probability regions (very low / very high) are consistently stable,  
> while **mid-probability regions (≈ 0.3–0.6)** are structurally volatile.

This behavior persists across feature variants and model families and is treated as a **property of the domain**, not merely a modeling flaw.

All evaluation logic and technical reasoning are documented in the **notebooks folder**, which serves as a traceable modeling record.

---

## 🌲 Beyond the Baseline

In addition to the calibrated logistic regression baseline, the project explores:

- **Decision Trees**
- **Random Forests**
- **Stacked models (logit + RF)**

These models are used to:

- probe **non-linear interactions**
- analyze **zone-specific behavior**
- test whether alternative learners can stabilize mid-probability regions

They are treated as **exploratory and complementary**, not as replacements for the probabilistic baseline.

---

## 🚧 Project Status

Work in progress.

Current focus areas:

- validating feature robustness across seasons
- understanding signal limits in mid-probability zones
- structured comparison of model families under identical evaluation rules

---

## 🔜 Next Steps

- targeted feature engineering for mid-probability refinement
- calibrated model comparison under a fixed protocol
- exploration of stacking and ensemble reliability
- extension toward richer probabilistic outputs

---

