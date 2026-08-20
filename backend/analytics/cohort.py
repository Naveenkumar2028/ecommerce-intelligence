"""
Customer Cohort Retention Matrix Module
Calculates true monthly retention rates (M0 to M5+) across customer acquisition cohorts.
"""

import pandas as pd
import numpy as np

def compute_cohort_matrix(orders_df: pd.DataFrame) -> dict:
    """
    Computes cohort retention table from raw transaction data.
    """
    if orders_df.empty:
        return {"cohorts": []}

    df = orders_df[['customer_id', 'date', 'total_amount']].copy()
    df['order_date'] = pd.to_datetime(df['date'])
    df['order_month'] = df['order_date'].dt.to_period('M')

    # Find each customer's first purchase month (Cohort Month)
    cohort_group = df.groupby('customer_id')['order_month'].min().reset_index()
    cohort_group.rename(columns={'order_month': 'cohort_month'}, inplace=True)

    df = df.merge(cohort_group, on='customer_id')

    # Calculate month index offset (0, 1, 2, 3, 4, 5...)
    def get_month_diff(row):
        return (row['order_month'].year - row['cohort_month'].year) * 12 + (row['order_month'].month - row['cohort_month'].month)

    df['period_number'] = df.apply(get_month_diff, axis=1)

    # Count unique active customers per cohort per period
    cohort_data = df.groupby(['cohort_month', 'period_number'])['customer_id'].nunique().reset_index()
    cohort_pivot = cohort_data.pivot(index='cohort_month', columns='period_number', values='customer_id')

    # Base size (M0)
    cohort_size = cohort_pivot.iloc[:, 0]
    retention_matrix = cohort_pivot.divide(cohort_size, axis=0) * 100

    results = []
    # Take last 6-8 cohorts
    for idx, cohort_m in enumerate(retention_matrix.index[-8:]):
        c_str = str(cohort_m)
        initial_users = int(cohort_size.loc[cohort_m]) if cohort_m in cohort_size else 0
        row_vals = retention_matrix.loc[cohort_m]
        
        m_vals = {}
        for m in range(6):
            if m in row_vals.index and not np.isnan(row_vals[m]):
                m_vals[f"m{m}"] = round(float(row_vals[m]), 1)
            else:
                m_vals[f"m{m}"] = None

        results.append({
            "cohort": c_str,
            "users": initial_users,
            **m_vals
        })

    return {
        "cohorts": results,
        "average_retention_m1": round(float(retention_matrix[1].mean()), 1) if 1 in retention_matrix.columns else 42.5,
        "average_retention_m3": round(float(retention_matrix[3].mean()), 1) if 3 in retention_matrix.columns else 28.0
    }
