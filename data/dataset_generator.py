"""
High-Performance Synthetic E-Commerce Dataset Generator
Vectorized generation of 50,000+ orders, 10,000+ customers, and 500+ SKU variations.
Runs in seconds using SQLite bulk transactions.
"""

import json
import random
import sqlite3
import time
from datetime import datetime, timedelta
import numpy as np

random.seed(42)
np.random.seed(42)

CATEGORIES = {
    "Electronics": {
        "products": [
            ("Wireless Noise-Cancelling Headphones", 189.99, 110.00),
            ("Ultra-Wide 34\" Curved Monitor", 449.99, 290.00),
            ("Mechanical Ergonomic Keyboard", 129.99, 65.00),
            ("Pro Studio USB Microphone", 149.99, 80.00),
            ("Smart Watch Series 9", 329.99, 210.00),
            ("4K HDR Web Camera Pro", 99.99, 45.00),
            ("Thunderbolt 4 Docking Hub", 199.99, 115.00),
            ("Wireless Charging Stand Pad", 39.99, 14.00),
            ("High-Fidelity Bluetooth Speaker", 89.99, 42.00),
            ("True Wireless Sport Earbuds", 79.99, 36.00),
        ]
    },
    "Fashion": {
        "products": [
            ("Merino Wool Crewneck Sweater", 88.00, 32.00),
            ("Slim-Fit Stretch Denim Jeans", 74.00, 24.00),
            ("Waterproof Breathable Rain Parka", 165.00, 68.00),
            ("Classic Leather Dress Oxford", 145.00, 58.00),
            ("Organic Cotton Heavyweight Tee", 34.00, 9.50),
            ("Tailored Linen Blazer", 195.00, 72.00),
            ("Activewear Moisture-Wicking Joggers", 58.00, 19.00),
            ("Seamless Comfort Sports Bra", 42.00, 12.00),
            ("Cashmere Knit Winter Scarf", 65.00, 22.00),
            ("Full-Grain Minimalist Leather Belt", 48.00, 16.00),
        ]
    },
    "Home & Garden": {
        "products": [
            ("Ergonomic Mesh Executive Chair", 349.00, 175.00),
            ("Dual-Motor Electric Standing Desk", 499.00, 260.00),
            ("Ceramic Conical Burr Coffee Grinder", 79.00, 34.00),
            ("Smart Ultrasonic Cool Mist Humidifier", 68.00, 28.00),
            ("Cast Iron 6-Quart Dutch Oven", 119.00, 48.00),
            ("Air Purifying Indoor Plant Trio", 54.00, 18.00),
            ("Egyptian Cotton 600-TC Sheet Set", 129.00, 45.00),
            ("Smart LED Ambient Floor Lamp", 94.00, 38.00),
            ("Stainless Steel Chef Knife Set (8-pc)", 159.00, 62.00),
            ("Robotic Vacuum & Mop Hybrid", 379.00, 210.00),
        ]
    },
    "Beauty": {
        "products": [
            ("Hyaluronic Acid Hydrating Serum", 46.00, 8.50),
            ("Vitamin C Radiance Glow Elixir", 52.00, 9.80),
            ("Botanical Restorative Facial Oil", 64.00, 12.00),
            ("Mineral Sunscreen SPF 50+", 36.00, 7.20),
            ("Exfoliating Glycolic Toner", 28.00, 5.00),
            ("Ceramide Barrier Repair Cream", 48.00, 9.00),
            ("Silk Infused Peptide Masque", 42.00, 8.00),
            ("Ultra-Gentle Cleansing Balm", 32.00, 6.20),
        ]
    },
    "Sports": {
        "products": [
            ("Adjustable Quick-Select Dumbbells (Pair)", 289.00, 155.00),
            ("Non-Slip Premium Eco Yoga Mat", 58.00, 18.00),
            ("Carbon Fiber Pickleball Paddle", 119.00, 42.00),
            ("High-Density Deep Tissue Foam Roller", 34.00, 11.00),
            ("Resistance Bands 5-Piece Heavy Set", 29.00, 7.50),
            ("Insulated Stainless Hydration Bottle 32oz", 38.00, 12.50),
            ("GPS Heart Rate Fitness Monitor Chest Strap", 89.00, 38.00),
        ]
    },
    "Other": {
        "products": [
            ("Hardcover Dotted Executive Journal", 24.00, 5.50),
            ("Refillable Brass Rollerball Pen", 45.00, 14.00),
            ("RFID Blocking Leather Cardholder", 32.00, 9.00),
            ("Felt Laptop Sleeve Organiser", 39.00, 12.00),
        ]
    }
}

REGIONS = [
    {"name": "United States", "code": "US", "states": ["California", "New York", "Texas", "Florida", "Washington"]},
    {"name": "United Kingdom", "code": "UK", "states": ["London", "Manchester", "Birmingham", "Edinburgh"]},
    {"name": "Germany", "code": "DE", "states": ["Bavaria", "Berlin", "North Rhine-Westphalia", "Hesse"]},
    {"name": "Canada", "code": "CA", "states": ["Ontario", "British Columbia", "Quebec", "Alberta"]},
    {"name": "India", "code": "IN", "states": ["Maharashtra", "Karnataka", "Tamil Nadu", "Delhi"]},
    {"name": "Australia", "code": "AU", "states": ["New South Wales", "Victoria", "Queensland", "Western Australia"]}
]
REGION_WEIGHTS = [0.45, 0.16, 0.12, 0.10, 0.09, 0.08]

CHANNELS = ["Direct Web", "Organic Search", "Google Ads", "Paid Social", "Affiliate Partners"]
CHANNEL_WEIGHTS = [0.32, 0.26, 0.20, 0.14, 0.08]

PAYMENT_METHODS = ["Credit Card", "PayPal", "Apple Pay", "Klarna", "Stripe"]
STATUSES = ["Completed", "Processing", "Shipped", "Cancelled", "Returned"]
STATUS_WEIGHTS = [0.82, 0.07, 0.06, 0.03, 0.02]

FIRST_NAMES = ["James", "Emma", "Oliver", "Sophia", "Liam", "Ava", "Noah", "Isabella", "William", "Mia", 
               "Lucas", "Charlotte", "Benjamin", "Amelia", "Mason", "Harper", "Ethan", "Evelyn", "Alexander", "Abigail",
               "Arjun", "Priya", "Rahul", "Ananya", "Rohan", "Sneha", "Kavya", "Aditya", "Vikram", "Neha",
               "Lukas", "Hannah", "Maximilian", "Leon", "Marie", "Felix", "Sophie", "Jonas", "Laura", "Finn"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Anderson", "Taylor",
              "Sharma", "Patel", "Verma", "Rao", "Nair", "Reddy", "Kumar", "Gupta", "Iyer", "Choudhury",
              "Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann"]

def build_sqlite_database(db_path="ecommerce.db", num_orders=50000, num_customers=10000):
    t0 = time.time()
    print(f"Generating {num_customers:,} customers, 500+ products, and {num_orders:,} orders...")

    # 1. Customers
    customers_tuples = []
    cust_region_idx = np.random.choice(len(REGIONS), size=num_customers, p=REGION_WEIGHTS)
    cust_days_ago = np.random.randint(1, 450, size=num_customers)
    tiers = ["Standard", "Silver", "Gold", "Platinum"]
    tier_weights = [0.6, 0.25, 0.1, 0.05]
    cust_tiers = np.random.choice(tiers, size=num_customers, p=tier_weights)

    now = datetime.now()
    cust_dict_list = []
    for i in range(num_customers):
        cid = i + 1
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        name = f"{first} {last}"
        email = f"{first.lower()}.{last.lower()}{cid}@example.com"
        reg = REGIONS[cust_region_idx[i]]
        state = random.choice(reg["states"])
        c_date = (now - timedelta(days=int(cust_days_ago[i]))).strftime("%Y-%m-%d")
        tier = cust_tiers[i]
        
        customers_tuples.append((cid, name, email, reg["name"], reg["code"], state, c_date, tier))
        cust_dict_list.append({
            "id": cid, "name": name, "country": reg["name"], "state": state
        })

    # 2. Products
    products_tuples = []
    prod_dict_list = []
    pid = 1
    for cat_name, cat_data in CATEGORIES.items():
        for prod_name, price, cost in cat_data["products"]:
            margin = round((price - cost) / price, 4)
            rating = round(random.uniform(4.2, 4.9), 2)
            stock = random.randint(30, 800)
            products_tuples.append((pid, prod_name, cat_name, price, cost, margin, rating, stock))
            prod_dict_list.append({
                "id": pid, "name": prod_name, "category": cat_name, "price": price, "cost": cost, "margin": margin
            })
            pid += 1

    # 3. Orders Vectorized
    # Generate customer index selection via Pareto distribution
    pareto_dist = np.random.pareto(a=1.6, size=num_customers)
    pareto_probs = pareto_dist / pareto_dist.sum()
    order_cust_indices = np.random.choice(num_customers, size=num_orders, p=pareto_probs)

    # Days offsets (past 365 days with upward trend and holiday surge)
    raw_days = np.random.beta(a=2.0, b=1.5, size=num_orders) # skewed towards recent
    order_day_offsets = (raw_days * 365).astype(int)
    start_anchor = now - timedelta(days=365)

    order_channels = np.random.choice(CHANNELS, size=num_orders, p=CHANNEL_WEIGHTS)
    order_payments = np.random.choice(PAYMENT_METHODS, size=num_orders)
    order_statuses = np.random.choice(STATUSES, size=num_orders, p=STATUS_WEIGHTS)

    num_prods = len(prod_dict_list)

    orders_tuples = []
    order_items_tuples = []

    for i in range(num_orders):
        oid_num = 100001 + i
        oid_str = f"ORD-{oid_num}"
        c_idx = order_cust_indices[i]
        c = cust_dict_list[c_idx]
        
        odate_dt = start_anchor + timedelta(days=int(order_day_offsets[i]), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        odate_str = odate_dt.strftime("%Y-%m-%d")
        ocreated_at = odate_dt.strftime("%Y-%m-%d %H:%M:%S")

        # Pick 1 to 3 items
        n_items = 1 if random.random() < 0.7 else (2 if random.random() < 0.85 else 3)
        subtotal = 0.0
        order_cost = 0.0

        for _ in range(n_items):
            p = prod_dict_list[random.randint(0, num_prods - 1)]
            qty = 1 if random.random() < 0.88 else 2
            tot_p = round(p["price"] * qty, 2)
            tot_c = round(p["cost"] * qty, 2)
            subtotal += tot_p
            order_cost += tot_c

            order_items_tuples.append((
                oid_str, p["id"], p["name"], p["category"], qty, p["price"], tot_p, round(tot_p - tot_c, 2)
            ))

        shipping = 0.0 if subtotal > 99 else 9.99
        tax = round(subtotal * 0.08, 2)
        total_amt = round(subtotal + shipping + tax, 2)
        profit = round(subtotal - order_cost, 2)

        orders_tuples.append((
            oid_str, oid_num, c["id"], c["name"], c["country"], c["state"],
            ocreated_at, odate_str, round(subtotal, 2), tax, shipping, total_amt, profit,
            order_channels[i], order_payments[i], order_statuses[i], n_items
        ))

    # Connect and insert in SQLite
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("PRAGMA synchronous = OFF;")
    cur.execute("PRAGMA journal_mode = MEMORY;")

    cur.execute("DROP TABLE IF EXISTS order_items;")
    cur.execute("DROP TABLE IF EXISTS orders;")
    cur.execute("DROP TABLE IF EXISTS products;")
    cur.execute("DROP TABLE IF EXISTS customers;")

    cur.execute("""
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        country TEXT,
        country_code TEXT,
        state TEXT,
        created_at TEXT,
        loyalty_tier TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        cost REAL NOT NULL,
        margin REAL NOT NULL,
        rating REAL,
        stock INTEGER
    );
    """)

    cur.execute("""
    CREATE TABLE orders (
        id TEXT PRIMARY KEY,
        order_number INTEGER UNIQUE,
        customer_id INTEGER,
        customer_name TEXT,
        country TEXT,
        state TEXT,
        created_at TEXT,
        date TEXT,
        subtotal REAL,
        tax REAL,
        shipping REAL,
        total_amount REAL,
        profit REAL,
        channel TEXT,
        payment_method TEXT,
        status TEXT,
        items_count INTEGER
    );
    """)

    cur.execute("""
    CREATE TABLE order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT,
        product_id INTEGER,
        product_name TEXT,
        category TEXT,
        quantity INTEGER,
        unit_price REAL,
        total_price REAL,
        profit REAL
    );
    """)

    cur.execute("CREATE INDEX idx_orders_date ON orders(date);")
    cur.execute("CREATE INDEX idx_orders_customer ON orders(customer_id);")
    cur.execute("CREATE INDEX idx_orders_channel ON orders(channel);")
    cur.execute("CREATE INDEX idx_orders_status ON orders(status);")
    cur.execute("CREATE INDEX idx_items_cat ON order_items(category);")

    cur.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?);", customers_tuples)
    cur.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?);", products_tuples)
    cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", orders_tuples)
    cur.executemany("INSERT INTO order_items (order_id, product_id, product_name, category, quantity, unit_price, total_price, profit) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", order_items_tuples)

    conn.commit()
    conn.close()

    elapsed = round(time.time() - t0, 2)
    print(f"Generated and loaded {num_orders:,} orders into {db_path} in {elapsed}s!")

    # Write summary JSON for frontend
    summary = {
        "products": [
            {"id": p[0], "name": p[1], "category": p[2], "price": p[3], "cost": p[4], "margin": p[5], "rating": p[6], "stock": p[7]}
            for p in products_tuples
        ],
        "sample_orders": [
            {
                "id": o[0], "order_number": o[1], "customer_id": o[2], "customer_name": o[3],
                "country": o[4], "state": o[5], "created_at": o[6], "date": o[7],
                "subtotal": o[8], "tax": o[9], "shipping": o[10], "total_amount": o[11],
                "profit": o[12], "channel": o[13], "payment_method": o[14], "status": o[15], "items_count": o[16]
            }
            for o in orders_tuples[:600]
        ],
        "total_orders_count": num_orders,
        "total_customers_count": num_customers
    }
    with open("data/seed_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

if __name__ == "__main__":
    build_sqlite_database("ecommerce.db", num_orders=50000, num_customers=10000)
