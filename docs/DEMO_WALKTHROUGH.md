# Demo Walkthrough

Use this walkthrough to validate the main analytics flow after starting the FastAPI backend locally.

## 1. Confirm the service is running

Open `http://localhost:8000/health` and verify that the response contains:

- `status: healthy`
- the expected service name
- the configured application version

If this check fails, fix the backend startup issue before debugging the dashboard.

## 2. Open the API documentation

Visit `http://localhost:8000/docs` to inspect the available endpoints and try a few requests from the interactive Swagger UI.

Recommended first checks:

1. `/api/overview` for headline KPIs
2. `/api/sales` for time-based sales data
3. `/api/products` for product performance
4. `/api/customers` for customer-level metrics

The exact response fields can be reviewed in [`API_REFERENCE.md`](./API_REFERENCE.md).

## 3. Review the dashboard in business order

When presenting the project, follow this sequence:

1. **Overview:** explain revenue, orders, customers, and average order value.
2. **Sales:** point out changes over time and any visible trend or seasonality.
3. **Products:** compare the best-performing products or categories.
4. **Customers:** discuss high-value, loyal, and at-risk segments.
5. **Retention:** use cohort results to explain repeat-purchase behavior.
6. **Forecasting:** describe the expected direction of future sales and the uncertainty around it.
7. **Anomalies:** highlight unusual activity that deserves investigation.
8. **Geography:** identify where sales activity is concentrated.

This order moves from business performance to diagnosis and then to action.

## 4. Capture one actionable insight

A useful demo should end with a decision, not only a chart. Examples include:

- prioritizing retention outreach for an at-risk customer segment
- increasing inventory for a consistently strong product category
- investigating a sudden sales spike or drop
- focusing marketing activity on a high-performing region

Record the insight together with the metric or endpoint that supports it.

## 5. Troubleshooting order

If a dashboard section is empty or incorrect, check in this order:

1. the backend process is still running
2. the corresponding API endpoint returns a successful response
3. the response contains the fields expected by the frontend
4. the browser console for JavaScript errors
5. the database and environment configuration

For startup and environment issues, see the troubleshooting notes in the repository README.
