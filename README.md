# Life Insurance Underwriting & Cash Flow Calculator

A Python CLI tool designed to simulate actuarial underwriting rules, project multi-year policy cash flow liabilities, and display formatted customer quotes.

## Features
- **Defensive Input Handling:** Built using `while` loops and `try/except` blocks to eliminate program crashes from typos or bad inputs.
- **Multi-Factor Risk Pricing Engine:** Underwrites policy premiums dynamically based on age brackets, health risk tiers, tobacco surcharges, and policy term lengths (10, 20, 30 years).
- **Cash Flow Projection Schedule:** Calculates and formats 1, 5, 10, and 20-year cumulative premium totals using custom string formatting.

## Tech Stack
- **Language:** Python 3.14
- **Core Concepts:** Functions, Conditional Logic, Error Handling (`try/except`), String Formatting (`f-strings`)

## Development Roadmap & Goals
- [x] **v1.0 - Foundation & Underwriting Engine:** 
  - Built defensive input handling using `while` loops and `try/except` blocks.
  - Implemented multi-factor risk pricing logic (age brackets, health tiers, tobacco surcharges, term lengths).
  - Designed custom cash flow projection tables using f-string alignment formatting (`:<12`, `:>11.2f`).
- [ ] **v1.1 - Data Retention:** Automatically export quotes to `quotes.csv` for policy persistence.
- [ ] **v1.2 - Portfolio Analytics:** Integrate `pandas` to calculate average monthly rates, total quotes, and risk distributions.
- [ ] **v2.0 - Actuarial Integration:** Connect real SOA (Society of Actuaries) mortality tables to calculate exact death probabilities ($q_x$).

## Learning Log
- **Session 1:** Handled Java-to-Python string formatting transitions, eliminated console crashes via defensive exception catching, and set up Git version control.