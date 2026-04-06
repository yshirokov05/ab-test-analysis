# A/B Test Design & Analysis: Mobile Checkout Optimization

End-to-end statistical experiment design for an e-commerce checkout optimization — from power analysis and hypothesis definition through Z-tests, confidence intervals, and guardrail metric validation. This is the natural follow-on to the [Product Analytics Case Study](https://github.com/yshirokov05/product-analytics-case-study), which identified a 15% drop-off at mobile checkout.

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python)](https://python.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Statistics-8CAAE6?style=flat-square&logo=scipy)](https://scipy.org/)
[![Statsmodels](https://img.shields.io/badge/Statsmodels-Power%20Analysis-FF6F61?style=flat-square)](https://www.statsmodels.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter)](https://jupyter.org/)

---

## Experiment Design

**The finding:** The product analytics funnel analysis found a 15% absolute drop-off between Add-to-Cart and Purchase for mobile users.

**The hypothesis:** A "One-Click Fast Checkout" button on product pages — bypassing the multi-step cart flow — will increase the mobile Checkout-to-Purchase conversion rate by at least 5 percentage points (absolute).

### Metrics

| Type | Metric | Why |
|---|---|---|
| Primary | Checkout-to-Purchase conversion rate | Directly measures the friction being removed |
| Guardrail | Average Order Value (AOV) | Ensures fast checkout doesn't cannibalize cross-sell |
| Secondary | Page load time | New button must not degrade mobile performance |

### Parameters

| Parameter | Value |
|---|---|
| Target audience | 100% of mobile web users |
| Randomization | 50/50 Control / Treatment |
| Minimum detectable effect | 5% absolute lift |
| Statistical power | 80% |
| Significance level | α = 0.05 |
| Required sample size | Calculated via power analysis |

---

## Methodology

### 1. Power Analysis
Pre-experiment sample size calculation using `statsmodels.stats.proportion.proportion_effectsize` and `NormalIndPower`. Determines the minimum number of users needed before running the test — prevents stopping early on noise.

### 2. Hypothesis Testing
Two-proportion Z-test on Checkout-to-Purchase conversion rates:
- H₀: conversion_treatment = conversion_control
- H₁: conversion_treatment > conversion_control

### 3. Confidence Intervals
95% CI on the observed lift, computed both analytically and bootstrapped — to quantify the range of plausible treatment effects, not just the point estimate.

### 4. Guardrail Validation
Independent t-test on AOV between groups. A statistically significant AOV drop in Treatment would indicate that fast checkout is cannibalizing order quality even while improving conversion rate.

### 5. Segment Analysis
Conversion lift broken out by acquisition channel (Direct, Social, Organic Search, Paid Ads) to check for heterogeneous treatment effects — a consistent lift across channels increases confidence the result generalizes.

---

## Simulated Results

The experiment is simulated with a controlled synthetic dataset (`scripts/simulate_data.py`):
- **Control:** 45% baseline Checkout-to-Purchase rate
- **Treatment:** 50% conversion (true +5% absolute lift)
- **n = 10,000 users** (50/50 split)
- **AOV:** ~$85 mean, equal across groups

This setup lets you verify the statistical machinery produces the correct answer on known ground truth before applying it to real data.

---

## Project Structure

```
ab-test-analysis/
├── scripts/
│   └── simulate_data.py        # Generate synthetic 10k-user experiment dataset
├── data/
│   └── ab_test_results.csv     # Simulated experiment output
└── notebooks/
    └── ab_test_analysis.ipynb  # Full analysis: power analysis → Z-test → CI → segments
```

---

## How to Run

```bash
git clone https://github.com/yshirokov05/ab-test-analysis.git
cd ab-test-analysis

pip install pandas numpy scipy statsmodels jupyter

# Generate the dataset
python scripts/simulate_data.py

# Open the analysis notebook
jupyter notebook notebooks/ab_test_analysis.ipynb
```

---

## What I Learned

**Decide your stopping rule before you start.** Running a test until it "looks significant" inflates Type I error substantially. The power analysis sets the sample size in advance — once you hit it, you read the result, regardless of what it says.

**Point estimates without confidence intervals are incomplete.** A 5% lift with a 95% CI of [0.1%, 9.9%] tells a very different story than a 5% lift with a CI of [4.1%, 5.9%]. The width of the interval is what tells you whether you need more data.

**Guardrail metrics prevent Goodhart's Law.** Optimizing exclusively on conversion rate can hurt business outcomes if fast checkout reduces cross-sell. The AOV guardrail catches the case where you "won" the primary metric but lost the business goal.

**Segmentation is how you find out if the result is real.** A consistent lift across four independent acquisition channels is much stronger evidence of a causal effect than an aggregate number, because the channels have independent noise sources.

---

**Part of a two-project series:**
- [Product Analytics Case Study](https://github.com/yshirokov05/product-analytics-case-study) — funnel analysis that motivated this experiment
- **A/B Test Analysis** ← you are here

**Author:** Yury Shirokov | UC Berkeley Economics + Data Science
