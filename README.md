# 🛒 E-Commerce Intelligence

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
  <img src="https://img.shields.io/badge/Tailwind_CSS-UI-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white"/>
</p>

<p align="center">
  <h1 align="center">Turn E-Commerce Data Into Business Decisions.</h1>
</p>

<p align="center">
  An end-to-end analytics platform for understanding revenue, customers, products,
  retention, trends, anomalies, and future sales.
</p>

<p align="center">
  <a href="https://naveenkumar2028.github.io/ecommerce-intelligence/">
    <img src="https://img.shields.io/badge/🚀_LIVE_DEMO-Open_Dashboard-22c55e?style=for-the-badge"/>
  </a>
  <a href="https://github.com/Naveenkumar2028/ecommerce-intelligence">
    <img src="https://img.shields.io/badge/💻_SOURCE_CODE-GitHub-181717?style=for-the-badge&logo=github"/>
  </a>
</p>

<p align="center">
  <a href="https://github.com/Naveenkumar2028/ecommerce-intelligence/stargazers">
    <img src="https://img.shields.io/github/stars/Naveenkumar2028/ecommerce-intelligence?style=for-the-badge&logo=github&label=Stars"/>
  </a>
  <a href="https://github.com/Naveenkumar2028/ecommerce-intelligence/network/members">
    <img src="https://img.shields.io/github/forks/Naveenkumar2028/ecommerce-intelligence?style=for-the-badge&logo=github&label=Forks"/>
  </a>
</p>

> ⭐ **If you find this project useful or interesting, consider giving it a star.** It helps the project reach other developers and data-analytics learners.

---

## 🎯 The Business Problem

E-commerce businesses generate large volumes of transactional data, but raw transactions do not directly answer the questions decision-makers care about:

- Are sales growing or declining?
- Which products and categories drive revenue?
- Who are the highest-value customers?
- Are customers returning after their first purchase?
- Which customer groups need attention?
- Are there unusual changes in sales activity?
- What could sales look like in the future?

**E-Commerce Intelligence** turns those questions into an interactive analytics workflow.

---

## 💡 What This Project Does

The platform combines descriptive, diagnostic, customer, and predictive analytics in one application.

| Area | What it answers |
|---|---|
| 💰 Revenue Analytics | How is the business performing? |
| 📦 Product Analytics | Which products/categories matter most? |
| 👥 Customer Analytics | Who are the valuable customers? |
| 🎯 RFM Segmentation | Which customers need retention or engagement? |
| 🔄 Cohort Analysis | How does customer retention change over time? |
| 📈 Forecasting | What could future sales look like? |
| 🚨 Anomaly Detection | Where are unusual patterns occurring? |
| 🌍 Geography | Where is business activity concentrated? |
| 📊 KPI Monitoring | What are the key performance indicators? |

---

## 🧠 Analytics Pipeline

```text
                    RAW E-COMMERCE DATA
                             │
                             ▼
                    DATA PROCESSING
                             │
                             ▼
                      SQL / DATABASE
                             │
                             ▼
                 EXPLORATORY ANALYSIS
                             │
             ┌───────────────┼───────────────┐
             ▼               ▼               ▼
            RFM           COHORT         PRODUCT
       SEGMENTATION       ANALYSIS       ANALYTICS
             │               │               │
             └───────────────┼───────────────┘
                             ▼
                  FORECASTING + ANOMALIES
                             │
                             ▼
                    BUSINESS INSIGHTS
                             │
                             ▼
                    RECOMMENDATIONS
```

---

# 🏗️ System Architecture

```text
┌───────────────────────────────────────────────┐
│                  FRONTEND                     │
│       JavaScript + Tailwind CSS UI            │
└──────────────────────┬────────────────────────┘
                       │ HTTP / JSON
                       ▼
┌───────────────────────────────────────────────┐
│                 FASTAPI API                   │
│                                               │
│ /overview  /sales  /customers  /products     │
│ /geography /orders /forecast /anomalies      │
│ /insights  /export                            │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│              ANALYTICS SERVICES               │
│                                               │
│ RFM • Cohort • Forecasting • Anomaly          │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────┐
│                    SQLite                     │
│              Transactional Data               │
└───────────────────────────────────────────────┘
```

The FastAPI application exposes the analytics API under `/api`, serves the frontend when available, and provides a `/health` endpoint for service monitoring.

---

# 🔌 API Layer

The backend is organized around business-oriented API endpoints rather than exposing database operations directly.

```text
GET /api/overview
GET /api/sales
GET /api/customers
GET /api/products
GET /api/geography
GET /api/orders
GET /api/insights
GET /api/forecast
GET /api/anomalies
GET /api/export
```

A typical request follows:

```text
Dashboard
   ↓
HTTP Request
   ↓
FastAPI Router
   ↓
Analytics Service
   ↓
Database
   ↓
JSON Response
   ↓
Dashboard Visualization
```

---

# 📊 Key Analytical Techniques

## 🎯 RFM Customer Segmentation

Customers are evaluated using:

- **Recency** — how recently they purchased
- **Frequency** — how often they purchased
- **Monetary** — how much they spent

This helps identify customer groups such as high-value, loyal, at-risk, and low-engagement customers.

## 🔄 Cohort Analysis

Customers are grouped by their acquisition/purchase period and tracked over subsequent periods to understand retention behavior.

## 📈 Sales Forecasting

Historical sales trends are analyzed to estimate future demand and support planning.

## 🚨 Anomaly Detection

The system identifies unusual changes in business activity that may require investigation.

---

# 🌐 Live Demo

### 🚀 [Open the Dashboard](https://naveenkumar2028.github.io/ecommerce-intelligence/)

> **Deployment note:** The current live frontend is hosted on GitHub Pages. The FastAPI backend is designed to run separately as an API service, so the live static dashboard and local/API execution are distinct deployment paths.

---

# 🖥️ Running Locally

## 1. Clone the repository

```bash
git clone https://github.com/Naveenkumar2028/ecommerce-intelligence.git
cd ecommerce-intelligence
```

## 2. Create and activate a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

## 4. Start the API

```bash
uvicorn backend.main:app --reload --port 8000
```

The backend will be available at:

```text
http://localhost:8000
```

FastAPI automatically exposes interactive API documentation at:

```text
http://localhost:8000/docs
```

and the health endpoint is:

```text
http://localhost:8000/health
```

---

# 📁 Project Structure

```text
ecommerce-intelligence/
│
├── backend/
│   ├── analytics/
│   │   ├── anomaly.py
│   │   ├── cohort.py
│   │   ├── forecasting.py
│   │   └── rfm.py
│   │
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   └── services/
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
├── ecommerce.db
├── .env.example
├── .gitignore
└── README.md
```

---

# 🔐 Configuration & Security Note

Database configuration can be supplied through environment variables rather than hard-coding deployment-specific settings.

The current project is primarily a **demo/portfolio analytics application**. It does **not currently implement user login, JWT/OAuth authentication, or role-based access control**. API endpoints should therefore be considered unauthenticated in the current version.

For a production deployment, the next security layer would include:

```text
User Login
    ↓
Password Hashing
    ↓
Authentication
    ↓
Access / Refresh Token
    ↓
API Authorization
    ↓
Role / Permission Checks
```

---

# 📌 Why I Built This

This project was built to demonstrate that data analytics can go beyond isolated notebooks and charts.

The goal was to connect the complete workflow:

**Business Problem → Data → Analytics → API → Dashboard → Insight → Decision**

It combines analytical thinking with practical software development to create a reusable business intelligence application.

---

# 🎯 Business Value

The platform can help an e-commerce team:

- Monitor revenue and sales performance
- Identify valuable and at-risk customers
- Understand retention patterns
- Evaluate product performance
- Detect unusual business activity
- Explore geographic trends
- Use forecasts for planning
- Turn analytics into actionable decisions

---

# 🚀 Future Improvements

- [ ] User authentication with JWT
- [ ] Role-based access control
- [ ] PostgreSQL production database
- [ ] Cloud deployment for the FastAPI backend
- [ ] Automated ETL pipeline
- [ ] Scheduled data refresh
- [ ] More advanced forecasting models
- [ ] Automated business insight generation
- [ ] Power BI integration

---

# 👨‍💻 Author

**M Naveenkumar**

CSE Student | Aspiring Data Analyst | Python | SQL | Business Intelligence

🔗 [GitHub](https://github.com/Naveenkumar2028)

🔗 [LinkedIn](https://www.linkedin.com/in/m-naveenkumar-aa1b923b4)

---

<p align="center">

### 📊 Raw Data → Analysis → Insight → Action

**Built to turn e-commerce data into better decisions.** 🚀

</p>
