from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from ..models.database import get_db, Order, Product, Customer
from ..services.data_service import AnalyticsDataService
import io
import csv

api_router = APIRouter()

@api_router.get("/overview")
def get_overview(
    date_range: str = Query("30D", description="Today, 7D, 30D, 90D, 12M"),
    category: str = Query("All"),
    region: str = Query("All"),
    channel: str = Query("All"),
    status: str = Query("All"),
    db: Session = Depends(get_db)
):
    service = AnalyticsDataService(db)
    return service.get_overview_data(
        date_range=date_range,
        category=category,
        region=region,
        channel=channel,
        status=status
    )

@api_router.get("/sales")
def get_sales_analytics(
    date_range: str = Query("30D"),
    category: str = Query("All"),
    region: str = Query("All"),
    db: Session = Depends(get_db)
):
    service = AnalyticsDataService(db)
    overview = service.get_overview_data(date_range=date_range, category=category, region=region)
    return {
        "time_series": overview["time_series"],
        "categories": overview["categories"],
        "kpi": overview["kpi"],
        "channels": [
            {"channel": "Direct Web", "sales": "$485,000", "orders": 1240, "growth": "+14.2%", "conversion": "3.8%"},
            {"channel": "Organic Search", "sales": "$392,000", "orders": 980, "growth": "+18.5%", "conversion": "4.2%"},
            {"channel": "Paid Social (IG/FB)", "sales": "$275,000", "orders": 740, "growth": "+8.1%", "conversion": "2.9%"},
            {"channel": "Google Ads", "sales": "$310,000", "orders": 810, "growth": "+11.4%", "conversion": "3.5%"},
            {"channel": "Affiliate Partners", "sales": "$185,000", "orders": 490, "growth": "+5.7%", "conversion": "2.1%"}
        ]
    }

@api_router.get("/customers")
def get_customer_analytics(db: Session = Depends(get_db)):
    service = AnalyticsDataService(db)
    return service.get_customer_analytics()

@api_router.get("/products")
def get_product_analytics(db: Session = Depends(get_db)):
    service = AnalyticsDataService(db)
    return service.get_product_analytics()

@api_router.get("/geography")
def get_geographic_analytics(db: Session = Depends(get_db)):
    service = AnalyticsDataService(db)
    return service.get_geographic_analytics()

@api_router.get("/orders")
def get_orders(
    page: int = Query(1, ge=1),
    limit: int = Query(25, ge=1, le=100),
    search: str = Query(None),
    status: str = Query("All"),
    category: str = Query("All"),
    db: Session = Depends(get_db)
):
    query = db.query(Order)
    if status and status != "All":
        query = query.filter(Order.status == status)
    if search:
        search_fmt = f"%{search}%"
        query = query.filter(
            (Order.id.ilike(search_fmt)) |
            (Order.customer_name.ilike(search_fmt)) |
            (Order.country.ilike(search_fmt))
        )
    
    total = query.count()
    orders = query.order_by(Order.date.desc()).offset((page - 1) * limit).limit(limit).all()
    
    return {
        "total": total,
        "page": page,
        "limit": limit,
        "total_pages": (total + limit - 1) // limit,
        "orders": orders
    }

@api_router.get("/insights")
def get_insights(db: Session = Depends(get_db)):
    service = AnalyticsDataService(db)
    overview = service.get_overview_data()
    return {
        "insights": overview["insights"],
        "generated_at": "Live Data Calculation"
    }

@api_router.get("/forecast")
def get_forecast(days: int = Query(30, ge=7, le=90), db: Session = Depends(get_db)):
    service = AnalyticsDataService(db)
    return service.get_forecast_data(days=days)

@api_router.get("/anomalies")
def get_anomalies(db: Session = Depends(get_db)):
    service = AnalyticsDataService(db)
    return service.get_anomalies_data()

@api_router.get("/export")
def export_orders_csv(db: Session = Depends(get_db)):
    orders = db.query(Order).limit(1000).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Order ID", "Customer Name", "Country", "Date", "Total Amount ($)", "Profit ($)", "Channel", "Payment Method", "Status"])
    
    for o in orders:
        writer.writerow([o.id, o.customer_name, o.country, o.date, o.total_amount, o.profit, o.channel, o.payment_method, o.status])
    
    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=ecommerce_orders_export.csv"}
    )
