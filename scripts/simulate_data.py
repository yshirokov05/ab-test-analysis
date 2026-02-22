import pandas as pd
import numpy as np
import os

# Set seed for reproducibility
np.random.seed(42)

def simulate_ab_test_data(n_users=10000):
    """
    Simulates A/B test data for mobile checkout.
    - Control Group: Baseline 45% Checkout-to-Purchase conversion.
    - Treatment Group: 50% Checkout-to-Purchase conversion (Fast Checkout Button).
    """
    
    # Generate User IDs
    user_ids = np.arange(1, n_users + 1)
    
    # Assign Groups (50/50 Split)
    groups = np.random.choice(['Control', 'Treatment'], size=n_users)
    
    # Baseline Metrics
    # Control Group: 45% Conversion
    # Treatment Group: 50% Conversion (+5% Absolute Lift)
    
    conversion_probs = np.where(groups == 'Control', 0.45, 0.50)
    conversions = np.random.binomial(n=1, p=conversion_probs)
    
    # Average Order Value (Guardrail Metric)
    # Both groups average $85 per order, but Treatment has slightly higher variance
    aov = np.random.normal(loc=85, scale=15, size=n_users)
    
    # Acquisition Channels
    channels = np.random.choice(['Direct', 'Social', 'Organic Search', 'Paid Ads'], 
                                size=n_users, 
                                p=[0.3, 0.25, 0.3, 0.15])
    
    # Create DataFrame
    df = pd.DataFrame({
        'user_id': user_ids,
        'group': groups,
        'channel': channels,
        'is_purchase': conversions,
        'order_value': np.where(conversions == 1, aov, 0)
    })
    
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df.to_csv('data/ab_test_results.csv', index=False)
    print(f"Successfully simulated data for {n_users} users in 'data/ab_test_results.csv'")

if __name__ == "__main__":
    simulate_ab_test_data()
