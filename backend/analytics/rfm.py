"""
RFM (Recency, Frequency, Monetary) Customer Segmentation Module
Computes true RFM quintiles and segment classifications.
"""

import pandas as pd
import numpy as np
from datetime import datetime

def compute_rfm_segments(orders_df: pd.DataFrame, reference_date: datetime = None) -> dict:
    """
    Given orders dataframe with ['customer_id', 'customer_name', 'date', 'total_amount'],
    computes RFM metrics and assigns standardized segment labels.
    """
    if orders_df.empty:
        return {"segments": [], "summary": {}}

    orders_df['date_dt'] = pd.to_datetime(orders_df['date'])
    if reference_date is None:
        reference_date = orders_df['date_dt'].max() + pd.Timedelta(days=1)

    # 1. Aggregate per customer
    rfm = orders_df.groupby('customer_id').agg(
        recency=('date_dt', lambda x: (reference_date - x.max()).days),
        frequency=('id', 'count'),
        monetary=('total_amount', 'sum'),
        customer_name=('customer_name', 'first'),
        country=('country', 'first')
    ).reset_index()

    # 2. Compute Quintile Scores (1 to 5)
    # Higher score = better. For Recency, lower days = higher score.
    try:
        rfm['R_score'] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1], duplicates='drop').astype(int)
    except Exception:
        rfm['R_score'] = pd.cut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1]).astype(int)

    try:
        rfm['F_score'] = pd.qcut(rfm['frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    except Exception:
        rfm['F_score'] = 3

    try:
        rfm['M_score'] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop').astype(int)
    except Exception:
        rfm['M_score'] = 3

    rfm['RFM_Score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)

    # 3. Segment mapping rules
    def assign_segment(row):
        r, f, m = row['R_score'], row['F_score'], row['M_score']
        if r >= 4 and f >= 4 and m >= 4:
            return "Champions"
        elif r >= 3 and f >= 3:
            return "Loyal Customers"
        elif r >= 3 and f < 3 and m >= 3:
            return "Potential Loyalists"
        elif r >= 4 and f == 1:
            return "New Customers"
        elif r <= 2 and f >= 3:
            return "At Risk"
        elif r == 1 and f >= 4 and m >= 4:
            return "Cannot Lose Them"
        else:
            return "Lost Customers"

    rfm['segment'] = rfm.apply(assign_segment, axis=1)

    # 4. Segment Summary
    total_customers = len(rfm)
    segment_summary = []
    
    segment_colors = {
        "Champions": "#10b981",
        "Loyal Customers": "#3b82f6",
        "Potential Loyalists": "#8b5cf6",
        "New Customers": "#06b6d4",
        "At Risk": "#f59e0b",
        "Cannot Lose Them": "#ec4899",
        "Lost Customers": "#ef4444"
    }

    for seg_name in ["Champions", "Loyal Customers", "Potential Loyalists", "New Customers", "At Risk", "Cannot Lose Them", "Lost Customers"]:
        seg_df = rfm[rfm['segment'] == seg_name]
        count = len(seg_df)
        pct = round((count / total_customers) * 100, 1) if total_customers > 0 else 0
        rev = round(seg_df['monetary'].sum(), 2)
        avg_spend = round(seg_df['monetary'].mean(), 2) if count > 0 else 0.0
        avg_rec = round(seg_df['recency'].mean(), 1) if count > 0 else 0.0

        segment_summary.append({
            "name": seg_name,
            "count": count,
            "percentage": pct,
            "revenue": rev,
            "avg_spend": avg_spend,
            "avg_recency_days": avg_rec,
            "color": segment_colors.get(seg_name, "#6b7280")
        })

    return {
        "segments": segment_summary,
        "total_analyzed_customers": total_customers,
        "sample_customers": rfm.head(50).to_dict(orient="records")
    }
