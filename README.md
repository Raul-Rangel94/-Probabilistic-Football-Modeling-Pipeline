# Probabilistic Football Modeling Pipeline (Liga MX)

This project focuses on building a **robust, interpretable, and football-aware data pipeline** for probabilistic modeling using Liga MX match data.

Rather than predicting exact scores or deterministic outcomes, the goal is to design a **clean and reusable pre-match dataset** that supports probability estimation, calibration analysis, and disciplined decision-making under uncertainty.

The project treats **models as downstream consumers of the data pipeline**, not as the center of the system.

---

## 🎯 Project Goals

- Build a structured and reproducible pre-match data pipeline  
- Design football-informed features (form, momentum, contextual signals)  
- Ensure temporal correctness and strict pre-match availability  
- Produce datasets suitable for **probabilistic evaluation**, not point prediction  
- Emphasize calibration, reliability, and interpretability  
- Establish a strong probabilistic baseline for comparison  

---

## ⚙️ Scope & Data

- **Competition:** Liga MX  
- **Granularity:** One record per match (home vs away)  
- **Temporal structure:** Rolling, pre-match windows  
- **Feature availability:** Strictly pre-kickoff (no leakage)  

While some exploratory notebooks focus on controlled seasonal subsets, the pipeline and validation strategy are **multi-season and temporally consistent by design**.

---

## 🧠 Feature Engineering (Pre-Match)

Each match is represented using separate home and away signals:

- `home_form`, `away_form`  
- `home_momentum`, `away_momentum`  
- Weighted variants of form (recent performance emphasis)  
- Contextual features (e.g. home advantage)  

Relative features are also included:

- `form_diff`  
- `momentum_diff`  
- `home_advantage_diff`  

### Conceptual Roles

- **Form** captures recent performance level  
- **Momentum** captures direction and trend  
- **Contextual features** adjust expectations rather than dominate them  

All features are computed using **only information available before kickoff**, preventing leakage by construction.

---

## 🎯 Target Definition

Current target:

- `home_win = 1` → home team wins  
- `home_win = 0` → draw or away win  

This binary setup is intentionally simple and extensible to:

- Multi-class outcomes (W / D / L)  
- Goal-based probabilistic models  
- Bayesian or hierarchical extensions  

---

## 📊 Modeling Philosophy

Football is a **high-variance, low-signal system**.

Exact outcome prediction is neither realistic nor informative.

This project prioritizes:

- Probability estimation  
- Calibration and reliability  
- Zone-based interpretation  
- Temporal validity  

Accuracy alone is **not treated as a sufficient metric**.

---

## 🔬 Validation & Evaluation

Model outputs are evaluated using:

- Temporal cross-validation (expanding window)  
- Log loss and Brier score  
- Reliability curves  
- Probability bucket (zone) analysis  

A central empirical finding of the project is that:

> Extreme probability regions (very low / very high) are consistently stable,  
> while mid-probability regions (≈ 0.4–0.6) are structurally volatile.

This behavior persists across feature variants and model families and is treated as a **property of the domain**, not merely a modeling flaw.

All evaluation logic and technical reasoning are documented in the `notebooks/` folder, which serves as a **traceable modeling record**.

---

## 📐 Probability Usage Policy

Predicted probabilities are **not used uniformly**.

Based on empirical evaluation and calibration analysis, the project adopts a **formal probability usage policy** that defines:

- Which probability ranges are actionable  
- How mid-range uncertainty is handled  
- The role and limits of auxiliary signals  
- When calibrated probabilities may be used  

📄 See: **[`PROBABILITY_POLICY.md`](docs/probability_policy.md)**

This policy acts as a **technical contract** governing all downstream interpretation and ensures disciplined, reproducible probability usage.

---

## 🌲 Beyond the Baseline

In addition to the calibrated logistic regression baseline, the project explores:

- Decision Trees  
- Random Forests  
- Stacked models (Logit + RF)  

These models are used to:

- Probe non-linear interactions  
- Analyze zone-specific behavior  
- Test whether alternative learners can stabilize mid-probability regions  

They are treated as **exploratory and complementary**, not as replacements for the probabilistic baseline.

---

## 🚧 Project Status

Work in progress.

Current focus areas:

- Validating feature robustness across seasons  
- Understanding signal limits in mid-probability zones  
- Structured comparison of model families under identical evaluation rules  

---

## 🔜 Next Steps

With the probabilistic baseline, calibration strategy, and probability usage policy now established, the next phase of the project focuses on **extension and generalization**, not core validation.

Planned directions include:

- Extension of the target space:
  - Multi-class outcomes (Win / Draw / Loss)
  - Goal-based probabilistic formulations
- Exploration of richer probabilistic models:
  - Hierarchical or Bayesian approaches
  - Distributional modeling of match outcomes
- Robustness analysis:
  - Stress-testing probability buckets across longer temporal spans
  - Cross-competition generalization experiments
- Pipeline hardening:
  - Further modularization and configuration management
  - Clear separation between data generation, modeling, and evaluation layers

Future work will continue to respect the established **Probability Usage Policy** and temporal evaluation framework.
