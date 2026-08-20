# REST API Reference: E-Commerce Intelligence

Base URL: `http://localhost:8000/api`

## Endpoints

### 1. `GET /api/overview`
Retrieves executive dashboard KPIs, sparklines, dynamic category splits, top products, and AI business insights.
- **Query Parameters**:
  - `date_range` (string, optional): `"Today" | "7D" | "30D" | "90D" | "12M"` (default `"30D"`)
  - `category` (string, optional): Filter by category (e.g. `"Electronics"`)
  - `region` (string, optional): Filter by country (e.g. `"United States"`)
  - `channel` (string, optional): Filter by channel
  - `status` (string, optional): Filter by status

### 2. `GET /api/sales`
Returns time-series revenue and volume velocity data with period-over-period comparison.

### 3. `GET /api/customers`
Returns customer analytics, including:
- Total customers, CLV, CAC, repeat rate, NPS.
- 7 RFM segment distributions (Champions, Loyal, Potential, New, At Risk, Cannot Lose, Lost).
- Monthly Cohort Retention Heatmap matrix ($M_0$ through $M_5+$).

### 4. `GET /api/products`
Returns SKU level rankings and the 2x2 Product Performance BCG Matrix (Stars, Volume Drivers, Niche, Review).

### 5. `GET /api/geography`
Returns international regional market share, country-level revenue, order volume, and AOV.

### 6. `GET /api/orders`
Paginated and searchable order transaction log.
- **Parameters**: `page` (int), `limit` (int), `search` (str), `status` (str)

### 7. `GET /api/insights`
Dynamically computed AI business insights with severity levels (`Positive`, `Warning`, `Critical`, `Opportunity`).

### 8. `GET /api/forecast`
Scikit-Learn Ridge regression time-series forecast with 95% statistical confidence bounds.
- **Parameters**: `days` (int, default `30`)

### 9. `GET /api/anomalies`
Real-time statistical anomaly detection output ($Z\text{-score} > 2.0$).

### 10. `GET /api/export`
Exports raw or filtered transaction logs to CSV.
