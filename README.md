# Life Insurance Underwriting & Cash Flow Calculator

A Python CLI tool designed to simulate actuarial underwriting rules, project multi-year policy cash flow liabilities, and display formatted customer quotes.

## Features
- **Defensive Input Handling:** Built using `while` loops and `try/except` blocks to eliminate program crashes from typos or bad inputs.
- **Multi-Factor Risk Pricing Engine:** Underwrites policy premiums dynamically based on age brackets, health risk tiers, tobacco surcharges, and policy term lengths (10, 20, 30 years).
- **Cash Flow Projection Schedule:** Calculates and formats 1, 5, 10, and 20-year cumulative premium totals using custom string formatting.
- **Dual-Layer Data Persistence:** Automatically appends generated quotes to a local `quotes.csv` file and a relational `insurance_quotes.db` SQLite database with timestamps.

## Tech Stack
- **Language:** Python 3.14
- **Database / File Storage:** SQLite3, CSV (`os`, `csv` modules)
- **Core Concepts:** Functions, Conditional Logic, Error Handling (`try/except`), String Formatting (`f-strings`), Database Persistence

## Development Roadmap & Goals
- [x] **v1.0 - Foundation & Underwriting Engine:** 
  - Built defensive input handling using `while` loops and `try/except` blocks.
  - Implemented multi-factor risk pricing logic (age brackets, health tiers, tobacco surcharges, term lengths).
  - Designed custom cash flow projection tables using f-string alignment formatting (`:<12`, `:>11.2f`).
- [x] **v1.1 - Data Retention:** Automatically export quotes to `quotes.csv` and `insurance_quotes.db` for multi-format policy persistence.
- [ ] **v1.2 - Portfolio Analytics:** Integrate `pandas` to calculate average monthly rates, total quotes, and risk distributions.
- [ ] **v2.0 - Actuarial Integration:** Connect real SOA (Society of Actuaries) mortality tables to calculate exact death probabilities ($q_x$).

## Learning Log
- **Session 1 (Yesterday):** 
  - Stopped the console from crashing on bad user inputs using `while` loops and `try/except` blocks.
  - Styled multi-year cash flow tables cleanly using Python `f-strings`.
  - Initialized Git version control and pushed the initial repository to GitHub.
- **Session 2 (Today):**
  - Added file storage with Python's `csv` and `os` modules so generated quotes stay saved in `quotes.csv` after the program closes.
  - Connected an SQLite database (`insurance_quotes.db`) to store customer names, premiums, and timestamps in a real table.
  - Learned how to troubleshoot Python function errors—specifically passing calculated variables (`premium_monthly`) as arguments into functions and fixing `f-string` syntax bugs.
  - Learned basic software versioning by officially bumping the project milestone from `v1.0` to `v1.1`.