from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class FilterParams(BaseModel):
    date_range: Optional[str] = "30D" # Today, 7D, 30D, 90D, 12M, custom
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    category: Optional[str] = "All"
    region: Optional[str] = "All"
    channel: Optional[str] = "All"
    status: Optional[str] = "All"
    search: Optional[str] = None

class KPIMetric(BaseModel):
    value: str
    numeric_value: float
    change_pct: float
    is_positive: bool
    sparkline: List[float] = []

class OverviewKPIs(BaseModel):
    revenue: KPIMetric
    orders: KPIMetric
    aov: KPIMetric
    customers: KPIMetric
    conversion_rate: KPIMetric
    net_profit: KPIMetric

class CategoryShare(BaseModel):
    name: str
    revenue: float
    orders: int
    profit: float
    percentage: float
    color: str

class TopProduct(BaseModel):
    id: int
    name: str
    category: str
    revenue: float
    units_sold: int
    orders_count: int
    margin: float
    profit: float
    trend: str

class AIInsight(BaseModel):
    id: str
    type: str # positive, warning, critical, opportunity
    title: str
    description: str
    primary_driver: str
    recommendation: str
    badge: str

class OrderSummary(BaseModel):
    id: str
    order_number: int
    customer_id: int
    customer_name: str
    date: str
    total_amount: float
    profit: float
    status: str
    payment_method: str
    channel: str
    country: str
    state: str
    items_count: int
