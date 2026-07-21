# Life Insurance Underwriting & Cash Flow Calculator

A Python CLI tool designed to simulate actuarial underwriting rules, project multi-year policy cash flow liabilities, and display formatted customer quotes.

## Features
- **Defensive Input Handling:** Built using `while` loops and `try/except` blocks to eliminate program crashes from typos or bad inputs.
- **Multi-Factor Risk Pricing Engine:** Underwrites policy premiums dynamically based on age brackets, health risk tiers, tobacco surcharges, and policy term lengths (10, 20, 30 years).
- **Cash Flow Projection Schedule:** Calculates and formats 1, 5, 10, and 20-year cumulative premium totals using custom string formatting.

## Tech Stack
- **Language:** Python 3.14
- **Core Concepts:** Functions, Conditional Logic, Error Handling (`try/except`), String Formatting (`f-strings`)