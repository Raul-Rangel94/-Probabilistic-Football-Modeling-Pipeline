# Notebooks – Probabilistic Modeling (Liga MX)

This folder contains the core analytical notebooks used throughout the development of the Liga MX probabilistic modeling project.

The notebooks are intentionally structured to reflect the **conceptual evolution of the project**, from baseline modeling to advanced probabilistic evaluation and policy definition. They are not isolated experiments, but part of a **coherent modeling narrative**.

---

## 🧭 Notebook Overview

### 01_baseline_logistic_regression.ipynb  
**Probabilistic Baseline – Calibrated Logistic Regression**

This notebook establishes the **baseline probabilistic model** for the project.

**Purpose:**
- Define a strong, interpretable probabilistic reference
- Focus on probability quality rather than raw accuracy
- Serve as a benchmark for all subsequent models

**Key aspects:**
- Logistic Regression with strictly pre-match features
- Feature set intentionally limited to robust, interpretable signals:
  - Weighted form  
  - Momentum  
  - Home advantage  
- Probability calibration (Platt / isotonic when applicable)
- Reliability curves and sanity checks
- Interpretation aligned with football logic

This baseline is treated as a **non-negotiable reference point**.  
The pre-match feature engineering phase is intentionally closed at this stage to preserve temporal stability and interpretability.

---

### 02_exploration_tree.ipynb  
**Decision Trees – Exploratory Modeling**

This notebook explores tree-based models to evaluate:

- Non-linear decision boundaries
- Feature interaction effects
- Threshold behavior in mid-probability regions

**Focus:**
- Exploratory analysis
- Understanding model behavior
- Identifying where linear models reach their limits

This notebook is **not intended as a final production model**, but as a diagnostic tool to analyze the mid-probability (“gray”) zone.

---

### 03_exploratory_model_SVM.ipynb  
**Support Vector Machines – Exploratory Analysis**

This notebook evaluates SVMs as an alternative modeling approach.

**Focus:**
- Margin-based classification
- Sensitivity to feature scaling
- Stability across probability regions

The goal is **conceptual comparison**, not optimization or deployment.

---

### 04_evaluation_model.ipynb  
**Probabilistic Evaluation & Reliability Analysis**

This notebook focuses exclusively on **probability quality evaluation**.

**Key analyses:**
- Probability bins (bucket-based evaluation)
- Empirical win rate vs predicted probability
- Brier score and log loss by probability zone
- Identification of reliable vs unreliable regions

Special attention is given to the **mid-probability range (≈ 0.4–0.6)**, which is treated as a **natural area of uncertainty**, not a modeling defect.

This notebook consolidates the evaluation logic used throughout the project and serves as the **main validation artifact**.

---

### 05_non_linear_refinement.ipynb  
**Non-Linear Refinement & Signal Stress Testing**

This notebook explores whether non-linear modeling can meaningfully refine probabilistic predictions, particularly in uncertain regions.

**Objectives:**
- Test if additional non-linear structure stabilizes predictions
- Evaluate interaction effects missed by linear models
- Stress-test feature robustness across model families

The outcome of this notebook reinforces a key project finding:  
non-linear complexity does **not systematically resolve mid-probability uncertainty**, and may introduce additional variance.

---

### 06_stacking_model.ipynb  
**Stacked Models – Meta-Modeling Exploration**

This notebook implements and evaluates stacked models using:

- Logistic Regression
- Random Forest
- Meta-level Logistic Regression

**Focus:**
- Combining heterogeneous learners
- Analyzing disagreement between base models
- Evaluating whether stacking improves probabilistic stability

Stacked models are treated as **analytical instruments**, not guaranteed improvements.  
They are evaluated under the same strict temporal and probabilistic criteria as the baseline.

---

### 07_medium_zone_eval.ipynb  
**Mid-Probability Zone Evaluation & Calibration**

This notebook focuses explicitly on the **structurally uncertain probability range (≈ 0.4–0.6)**.

**Key analyses:**
- Identification and isolation of mid-probability matches
- Evaluation of error concentration and volatility
- Meta-model behavior within the conflict zone
- Application of **Isotonic Regression** to recalibrate stacked model outputs
- Local and global Brier score comparison before and after calibration

This notebook provides the **empirical basis** for the project’s probability usage policy and demonstrates that:
- Mid-range uncertainty is structural
- Calibration improves reliability but reduces coverage
- Uncertainty should be managed, not eliminated

---

## 📊 Modeling Philosophy (Notebook-Level)

Across all notebooks, the project follows these principles:

- Football is a high-variance system
- Exact result prediction is not the objective
- Well-calibrated probabilities are more valuable than accuracy
- Evaluation must be interpretable and football-aware
- Linear models define the probabilistic baseline
- Non-linear models are explored to **understand uncertainty**, not eliminate it
- Models are consumers of a robust data pipeline, not the center of the system

---

## 🚧 Notes on Structure

Some notebooks are exploratory by design. Others are closer to final, portfolio-ready artifacts.

This separation is intentional and reflects:
- Learning progression
- Hypothesis testing
- Professional modeling workflow

---

## 📐 Relationship to Probability Policy

Findings from these notebooks directly inform the project’s **Probability Usage Policy**, which defines how predicted probabilities may (and may not) be used.

📄 See: **`PROBABILITY_POLICY.md`**

This folder documents not only results, but the **reasoning, constraints, and trade-offs** behind them.
