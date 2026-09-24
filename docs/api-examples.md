# API Examples

This page provides small `curl` examples for the main E-Commerce Intelligence endpoints.

Start the backend locally first:

```bash
uvicorn backend.main:app --reload --port 8000
```

The examples assume the API is available at `http://localhost:8000`.

## Health check

```bash
curl http://localhost:8000/health
```

## Dashboard overview

```bash
curl http://localhost:8000/api/overview
```

## Sales data

```bash
curl "http://localhost:8000/api/sales"
```

## Filtered orders

Pass query parameters when you want a narrower view of the order data:

```bash
curl "http://localhost:8000/api/orders?category=Electronics"
```

## Customers and products

```bash
curl http://localhost:8000/api/customers
curl http://localhost:8000/api/products
```

## Forecasts and anomalies

```bash
curl http://localhost:8000/api/forecast
curl http://localhost:8000/api/anomalies
```

## Export data

```bash
curl -OJ http://localhost:8000/api/export
```

## Interactive documentation

FastAPI also exposes interactive documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

Use the interactive docs to inspect response schemas and try requests without writing a command manually.

> The exact response fields can change as the analytics services evolve. Treat the OpenAPI schema in `/docs` as the source of truth when integrating a client.
