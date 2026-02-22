# A/B Test Design & Analysis: Optimizing Mobile Checkout

## Overview
This project follows our [Product Analytics Case Study](https://github.com/yshirokov05/product-analytics-case-study) which identified a **15% drop-off bottleneck** in the mobile checkout funnel. 

To address this, we designed an experiment testing a **"One-Click Fast Checkout"** button for mobile users. This repository covers the end-to-end experimental lifecycle: from power analysis and hypothesis definition to statistical significance testing and post-test segmentation.

## 1. Experiment Design
### **The Hypothesis**
*   **Problem:** High friction in the multi-step mobile checkout flow.
*   **Proposed Solution:** A "Fast Checkout" button on product pages that skips the cart and goes directly to the payment screen.
*   **Hypothesis:** Implementing the "Fast Checkout" button will increase the **Checkout-to-Purchase conversion rate** by at least **5% (absolute)** for mobile users.

### **Key Metrics**
*   **Primary Metric:** Checkout-to-Purchase Conversion Rate.
*   **Guardrail Metric:** Average Order Value (AOV) — ensuring fast checkout doesn't reduce cross-selling.
*   **Secondary Metric:** Page Load Time (ensuring the new button doesn't slow down the mobile experience).

## 2. Experimental Parameters
*   **Targeting:** 100% of Mobile Web Users.
*   **Randomization:** 50/50 split (Control vs. Treatment).
*   **Sample Size:** Determined via Power Analysis (80% Power, 0.05 Significance).

## 3. Methodology
- **Power Analysis:** Pre-calculating required sample size.
- **Hypothesis Testing:** Using Z-tests for conversion proportions.
- **Confidence Intervals:** Calculating the 95% CI for the lift.
- **Segment Analysis:** Checking impact across different acquisition channels.

## 4. How to Reproduce
1.  Run `python scripts/simulate_data.py` to generate the experiment dataset.
2.  Open `notebooks/ab_test_analysis.ipynb` to view the full statistical analysis and results.
