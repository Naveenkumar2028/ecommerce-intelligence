"""
Time Series Sales & Orders Forecasting Module
Uses Scikit-Learn regression with trend, day-of-week seasonality, and confidence intervals.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import Ridge

def generate_sales_forecast(orders_df: pd.DataFrame, days_ahead: int = 30) -> dict:
    """
    Fits daily revenue and orders time-series, producing forecasts with 95% confidence bands.
    """
    if orders_df.empty:
        return {"historical": [], "forecast": [], "summary": {}}

    # Group orders by day
    df = orders_df.groupby('date').agg(
        revenue=('total_amount', 'sum'),
        orders=('id', 'count'),
        profit=('profit', 'sum')
    ).reset_index()

    df['date_dt'] = pd.to_datetime(df['date'])
    df = df.sort_values('date_dt').reset_index(drop=True)

    # Feature Engineering
    min_date = df['date_dt'].min()
    df['day_idx'] = (df['date_dt'] - min_date).dt.days
    df['day_of_week'] = df['date_dt'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

    # One-hot encode day of week
    dow_dummies = pd.get_dummies(df['day_of_week'], prefix='dow', drop_first=True)
    X = pd.concat([df[['day_idx', 'is_weekend']], dow_dummies], axis=1)
    
    # Train Ridge models for Revenue and Orders
    model_rev = Ridge(alpha=1.0)
    model_rev.fit(X, df['revenue'])
    pred_train_rev = model_rev.predict(X)
    residual_std_rev = float(np.std(df['revenue'] - pred_train_rev))

    model_orders = Ridge(alpha=1.0)
    model_orders.fit(X, df['orders'])
    pred_train_orders = model_orders.predict(X)
    residual_std_orders = float(np.std(df['orders'] - pred_train_orders))

    # Generate Future Dates
    last_date = df['date_dt'].max()
    future_rows = []
    future_features = []

    for i in range(1, days_ahead + 1):
        f_date = last_date + timedelta(days=i)
        f_day_idx = (f_date - min_date).days
        f_dow = f_date.weekday()
        f_weekend = 1 if f_dow in [5, 6] else 0

        # One hot dummy array matching training set
        dummy_row = [1 if f_dow == col_dow else 0 for col_dow in range(1, 7)]
        row_feat = [f_day_idx, f_weekend] + dummy_row
        future_features.append(row_feat)
        future_rows.append(f_date)

    future_X = pd.DataFrame(future_features, columns=X.columns)
    pred_rev = model_rev.predict(future_X)
    pred_ord = model_orders.predict(future_X)

    forecast_results = []
    for idx, f_date in enumerate(future_rows):
        val_rev = max(0.0, float(pred_rev[idx]))
        val_ord = max(0, int(round(pred_ord[idx])))
        
        # 95% Confidence Interval (~1.96 * sigma) with variance increasing with forecast horizon
        horizon_penalty = 1.0 + (idx / days_ahead) * 0.4
        ci_rev_margin = 1.96 * residual_std_rev * horizon_penalty
        ci_ord_margin = 1.96 * residual_std_orders * horizon_penalty

        forecast_results.append({
            "date": f_date.strftime("%Y-%m-%d"),
            "predicted_revenue": round(val_rev, 2),
            "revenue_lower": max(0.0, round(val_rev - ci_rev_margin, 2)),
            "revenue_upper": round(val_rev + ci_rev_margin, 2),
            "predicted_orders": val_ord,
            "orders_lower": max(0, int(round(val_ord - ci_ord_margin))),
            "orders_upper": int(round(val_ord + ci_ord_margin)),
        })

    # Last 30 historical records for chart continuity
    hist_results = []
    for _, row in df.tail(30).iterrows():
        hist_results.append({
            "date": row['date'],
            "actual_revenue": round(float(row['revenue']), 2),
            "actual_orders": int(row['orders']),
            "profit": round(float(row['profit']), 2)
        })

    # Summary Metrics
    total_hist_rev = float(df['revenue'].tail(30).sum())
    total_forecast_rev = float(sum(r['predicted_revenue'] for r in forecast_results))
    projected_growth = round(((total_forecast_rev - total_hist_rev) / total_hist_rev) * 100, 2) if total_hist_rev > 0 else 0.0

    return {
        "historical": hist_results,
        "forecast": forecast_results,
        "summary": {
            "projected_revenue_30d": round(total_forecast_rev, 2),
            "projected_orders_30d": sum(r['predicted_orders'] for r in forecast_results),
            "projected_growth_pct": projected_growth,
            "confidence_level": "95% Statistical Confidence Band",
            "model_type": "Ridge Multi-variate Linear Time Series"
        }
    }
