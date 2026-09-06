# 🛒 E-Commerce Intelligence

An analytics dashboard that turns e-commerce data into useful business insights.

## 🚀 Features

- Revenue and sales analysis
- Customer analysis
- Product and category analysis
- RFM customer segmentation
- Cohort retention analysis
- Sales forecasting
- Anomaly detection
- Geographic analysis
- KPI dashboard

## 🛠️ Tech Stack

- **Frontend:** HTML, JavaScript, Tailwind CSS
- **Backend:** Python, FastAPI
- **Database:** SQLite
- **Analytics:** RFM, Cohort Analysis, Forecasting, Anomaly Detection

## 🏗️ How It Works

```text
E-Commerce Data → SQLite → FastAPI → Analytics → Dashboard → Insights
```

The frontend sends requests to the FastAPI backend. The backend processes the data, runs the required analytics, and returns JSON data to the dashboard.

## 📊 Main Analytics

### RFM Analysis

- **Recency** – How recently a customer purchased
- **Frequency** – How often they purchased
- **Monetary** – How much they spent

### Cohort Analysis

Tracks customer retention over time based on their first purchase period.

### Forecasting

Uses historical sales data to estimate future sales trends.

### Anomaly Detection

Finds unusual changes or patterns in sales activity.

## 🔌 API Endpoints

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

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Naveenkumar2028/ecommerce-intelligence.git
cd ecommerce-intelligence
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Start the backend

```bash
uvicorn backend.main:app --reload --port 8000
```

- API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

## 📁 Project Structure

```text
ecommerce-intelligence/
├── backend/
│   ├── analytics/
│   │   ├── anomaly.py
│   │   ├── cohort.py
│   │   ├── forecasting.py
│   │   └── rfm.py
│   ├── app/
│   ├── main.py
│   └── requirements.txt
├── frontend/
├── ecommerce.db
├── .env.example
├── .gitignore
└── README.md
```

## 🌐 Live Demo

[Open Dashboard](https://naveenkumar2028.github.io/ecommerce-intelligence/)

## 🎯 Purpose

This project demonstrates a complete analytics workflow:

**Data → Processing → Analytics → API → Dashboard → Insights**

It combines Python, SQL, data analytics, APIs, and frontend development in one project.

## 🚀 Future Improvements

- JWT authentication
- PostgreSQL database
- Cloud deployment
- Automated ETL pipeline
- Scheduled data updates
- Advanced forecasting
- Power BI integration

## 👨‍💻 Author

**M Naveenkumar**  
CSE Student | Python | SQL | Data Analytics | Business Intelligence

[GitHub](https://github.com/Naveenkumar2028) · [LinkedIn](https://www.linkedin.com/in/m-naveenkumar-aa1b923b4)
