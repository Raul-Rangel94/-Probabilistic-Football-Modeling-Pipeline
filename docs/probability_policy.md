# Probability Usage Policy

## 1. Purpose and Scope

This document defines the **official policy for using model-generated probabilities** in the Liga MX probabilistic modeling project.

Its purpose is to:
- Ensure **correct, consistent, and responsible** use of predicted probabilities
- Prevent misuse of uncertain predictions
- Explicitly encode learnings obtained during model evaluation and calibration

This policy applies to:
- All downstream analysis
- Any interpretation of model outputs
- Any decision-making process derived from model probabilities

This policy **does not** define betting strategies, financial decisions, or operational actions.

---

## 2. Models Covered

This policy applies to probabilities produced by:

- **Base models**
  - Logistic Regression (Logit)
  - Random Forest (RF)

- **Meta-model**
  - Stacked Logistic Regression (Logit + RF)

- **Calibrated variants**
  - Post-hoc Isotonic Regression

All probabilities referenced in this document correspond to **out-of-sample (OOS)** predictions evaluated using **temporal cross-validation**.

---

## 3. Why a Probability Policy Is Required

Empirical evaluation revealed the following:

- Systematic uncertainty in the mid-probability range (≈ 0.4–0.6)
- Feature engineering aimed at resolving this uncertainty increased variance
- Strong regularization in meta-models distorted sample distribution
- Post-hoc calibration (Isotonic Regression) improved:
  - Local and global Brier Score
  - Probability reliability
  - Stability in high-confidence regions

These results indicate that mid-range uncertainty is **structural**, not a modeling flaw.

---

## 4. Calibration Strategy

The adopted calibration policy is:

- **Isotonic Regression** is the preferred method
- Applied:
  - Post-hoc
  - Only to OOS predictions
- Objectives:
  - Improve probability reliability
  - Preserve ranking behavior

Calibration is **not** intended to:
- Eliminate uncertainty
- Increase coverage
- Correct weak-signal matches

---

## 5. Probability Buckets

Probabilities are categorized as follows:

| Probability Range | Interpretation | Status |
|------------------|----------------|--------|
| p ≥ 0.65 | High confidence | Actionable |
| 0.55 ≤ p < 0.65 | Moderate confidence | Conditionally usable |
| 0.45 ≤ p < 0.55 | Structural uncertainty | Non-actionable |
| 0.35 ≤ p < 0.45 | Moderate confidence (inverse) | Conditionally usable |
| p < 0.35 | High confidence (inverse) | Actionable |

The **0.45–0.55** interval is explicitly defined as **uncertain by design**.

---

## 6. Allowed and Forbidden Uses

### High Confidence Buckets (p ≥ 0.65 or p < 0.35)

**Allowed**
- Quantitative analysis
- Ranking and comparison
- Performance reporting

**Forbidden**
- Additional recalibration
- Feature-based probability correction

---

### Moderate Confidence Buckets (0.55–0.65, 0.35–0.45)

**Allowed**
- Conditional analysis
- Contextual filtering using auxiliary signals

**Forbidden**
- Direct interpretation without context

---

### Structural Uncertainty Bucket (0.45–0.55)

**Forbidden**
- Decision-making
- Probability-based ranking

**Allowed**
- Diagnostic analysis
- Model behavior inspection

---

## 7. Role of Auxiliary Signals

Auxiliary signals include:
- Model disagreement
- Signal strength
- Balanced match indicators
- Other meta-features

Policy rules:
- Auxiliary signals **do not modify probabilities**
- Auxiliary signals **do not recalibrate outputs**
- Auxiliary signals **provide contextual risk assessment**
- Auxiliary signals **support diagnostic analysis**

They are **diagnostic**, not corrective.

---

## 8. Accepted Trade-offs

This policy explicitly accepts:

- Reduced actionable sample size
- Persistence of ambiguous matches
- Lower coverage in exchange for reliability

The model **does not attempt** to eliminate inherent football uncertainty.

---

## 9. Conceptual Usage Flow

1. Generate OOS probabilities
2. Apply isotonic calibration
3. Assign probability bucket
4. Use probabilities only if bucket allows
5. Apply auxiliary signals only as context
6. Exclude uncertain matches from decision use

---

## 10. Final Notes

This policy reflects **empirical evidence**, not theoretical preference.

It exists to:
- Preserve model integrity
- Enforce disciplined probability usage
- Align outputs with real-world uncertainty

Future model iterations must be evaluated **against this policy**, not the inverse.
