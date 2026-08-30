# Data Quality Checklist

This checklist documents the minimum validation expected before analytical results are treated as trustworthy.

## Completeness

- [ ] Required customer, order, product, and date fields are present.
- [ ] Missing values are measured and reviewed before analysis.

## Uniqueness

- [ ] Duplicate transaction records are identified.
- [ ] Customer and order identifiers follow the expected uniqueness rules.

## Validity

- [ ] Dates can be parsed consistently.
- [ ] Numeric measures use valid ranges and data types.
- [ ] Categorical values use the expected vocabulary.

## Consistency

- [ ] Currency and units are standardized.
- [ ] Customer and product identifiers remain consistent across transformations.

## Analytical Checks

- [ ] Aggregated revenue reconciles with source totals within expected rules.
- [ ] RFM inputs use a clearly defined observation date.
- [ ] Forecasting inputs are ordered chronologically.
- [ ] Anomalies are reviewed against possible business events before being treated as errors.

## Release Gate

A dataset is considered analytics-ready only after critical validation failures have been resolved or explicitly documented.
