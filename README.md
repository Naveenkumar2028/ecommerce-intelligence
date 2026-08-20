# ⚡ E-Commerce Intelligence Platform

> **Turn your e-commerce data into actionable decisions.**

A portfolio-grade, full-stack **E-Commerce Intelligence & Data Analytics Platform** featuring **FastAPI**, **Pandas**, **NumPy**, **Scikit-Learn**, and a modern **React 18 SaaS Dashboard** inspired by Linear, Stripe, and Vercel design principles.

---

## 🌟 Key Capabilities & Features

- **Executive Overview Dashboard**: 6 core KPIs (Total Revenue, Orders, AOV, Active Customers, Conversion Rate, Net Profit) with sparklines, interactive period-over-period comparison charts, and category volume splits.
- **RFM Customer Segmentation**: True Recency, Frequency, and Monetary quintile calculations (1–5) grouping customers into 7 actionable cohorts (*Champions, Loyal Customers, Potential Loyalists, New Customers, At Risk, Cannot Lose Them, Lost Customers*).
- **Customer Retention Cohort Heatmap**: Tracks retention decay from Month 0 through Month 5+ across monthly acquisition cohorts.
- **Scikit-Learn Time Series Forecasting**: Multi-variate Ridge regression models with 95% statistical confidence bounds and an interactive scenario simulator (ad spend multiplier & promo discount).
- **Statistical Anomaly Detection**: Real-time Z-score & IQR deviation analysis detecting revenue dips, order spikes, and refund abnormalities.
- **Product Performance 2x2 Matrix**: BCG-style classification matrix segmenting products into *Stars*, *Volume Drivers*, *Niche Opportunities*, and *Phased Out items*.
- **Geographic Analytics**: Country-level revenue distribution across US, UK, Germany, Canada, India, and Australia.
- **Order Operations**: Searchable, sortable, paginated order book with interactive slide-over transaction invoice drawer.
- **AI-Style Business Insights**: Dynamic recommendations categorized by severity (*Positive, Warning, Critical, Opportunity*) with root causes and execution strategies.
- **Spotlight Command Palette (`Ctrl + K`)**: Keyboard-driven quick search for products, customers, and navigation routes.
- **Data Export & Reporting**: Instant CSV export and printable executive performance reports.
- **Theme Support**: Seamless Dark & Light themes with persistent state.

---

## 🏗️ Architecture

```
ecommerce-intelligence/
├── backend/
│   ├── app/
│   │   ├── api/router.py          # FastAPI REST endpoints
│   │   ├── core/config.py         # Config & CORS settings
│   │   ├── models/database.py     # SQLAlchemy models & SQLite/Postgres connection
│   │   ├── schemas/analytics.py   # Pydantic V2 response models
│   │   └── services/data_service.py # Analytics aggregation service
│   ├── analytics/
│   │   ├── rfm.py                 # RFM quintile segmentation engine
│   │   ├── cohort.py              # Cohort retention matrix calculator
│   │   ├── forecasting.py         # Scikit-learn Ridge forecast model
│   │   └── anomaly.py             # Z-score anomaly detector
│   ├── main.py                    # Server entry point
│   └── requirements.txt
├── data/
│   ├── dataset_generator.py       # High-speed synthetic generator (50k+ orders)
│   └── schema.sql                 # SQL DDL schemas
├── frontend/
│   └── index.html                 # Production React 18 SPA dashboard
├── docs/
│   ├── ARCHITECTURE.md            # Technical architecture specification
│   ├── API_REFERENCE.md           # API endpoints documentation
│   └── PORTFOLIO_GUIDE.md         # Interview & talking points guide
├── .env.example
├── .gitignore
└── README.md
```

---

## 🚀 Quickstart & Running Locally

### 1. Prerequisites
- Python 3.10+ installed

### 2. Install Dependencies
```bash
pip install -r backend/requirements.txt
```

### 3. Generate 50,000+ Orders Dataset (Takes ~2 seconds)
```bash
python data/dataset_generator.py
```

### 4. Start the Application Server
```bash
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

Open your browser at:
**[http://localhost:8000](http://localhost:8000)** (or `http://127.0.0.1:8000`)

---

## 📊 Tech Stack

- **Backend**: Python, FastAPI, Uvicorn, SQLAlchemy, Pydantic
- **Data & ML**: Pandas, NumPy, Scikit-Learn (Ridge regression, Z-score models)
- **Database**: SQLite (built-in) / PostgreSQL (production ready)
- **Frontend**: React 18, Tailwind CSS, Chart.js, Lucide Icons, Modern CSS variables
- **Design System**: Dark Modern SaaS theme + Light theme support, accessible typography (Plus Jakarta Sans)
