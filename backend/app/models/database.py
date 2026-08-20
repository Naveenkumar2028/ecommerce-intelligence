from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from ..core.config import settings

engine = create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    country = Column(String(100))
    country_code = Column(String(10))
    state = Column(String(100))
    created_at = Column(String(50))
    loyalty_tier = Column(String(50), default="Standard")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    category = Column(String(100), nullable=False, index=True)
    price = Column(Float, nullable=False)
    cost = Column(Float, nullable=False)
    margin = Column(Float, nullable=False)
    rating = Column(Float, default=4.5)
    stock = Column(Integer, default=100)

class Order(Base):
    __tablename__ = "orders"
    id = Column(String(50), primary_key=True, index=True)
    order_number = Column(Integer, unique=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), index=True)
    customer_name = Column(String(150))
    country = Column(String(100))
    state = Column(String(100))
    created_at = Column(String(50))
    date = Column(String(20), index=True)
    subtotal = Column(Float, nullable=False)
    tax = Column(Float, default=0.0)
    shipping = Column(Float, default=0.0)
    total_amount = Column(Float, nullable=False)
    profit = Column(Float, nullable=False)
    channel = Column(String(100), default="Direct Web", index=True)
    payment_method = Column(String(50), default="Credit Card")
    status = Column(String(50), default="Completed", index=True)
    items_count = Column(Integer, default=1)

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String(50), ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    product_name = Column(String(200))
    category = Column(String(100), index=True)
    quantity = Column(Integer, default=1)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    profit = Column(Float, nullable=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
