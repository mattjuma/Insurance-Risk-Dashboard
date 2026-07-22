import csv
import os
import sqlite3
from datetime import datetime

print("Life Insurance Premium Calculator")

def calculate_premium(age,coverage,health, is_smoker, term_years):
    base = 20
## AGE
    if age <= 30:
        age_factor = 1
    elif age <= 50:
        age_factor = 1.5
    else:
        age_factor = 2
## HEALTH
    if health == "Preferred":
        health_factor = 0.8
    elif health == "Standard":
        health_factor = 1
    elif health == "Substandard":
        health_factor = 1.5
    else:
        health_factor = 1

## Tobacco Surcharge (Smokers pay 2.2x rate)
    smoker_factor = 2.2 if is_smoker else 1.0

#Term Length Multiplier
    term_multipliers = {10: 1.0, 20: 1.25, 30: 1.6}
    term_factor = term_multipliers.get(term_years, 1.0)
##Premium Calculation
    premium = base * age_factor * health_factor * smoker_factor * term_factor * (coverage/100000)

    return premium
def print_policy_schedule(monthly_premium):
    annual_premium = monthly_premium * 12
    milestones = [1, 5, 10, 20]

    print("\n--- POLICY CASHFLOW PROJECTION ---")
    for year in milestones:
        total_paid = annual_premium * year
        print(f"Year {year}: Monthly: ${monthly_premium: .2f} | Total Paid: ${total_paid:.2f}")
    print("-----------------------------------\n")


##SAVE TO DATABSE
def save_quote_to_db(name, age, coverage, health, is_smoker, term_years, premium):
    
#Name
name = input("Name: ")
while True:
    try:
        age = int(input("Age: "))
        if age > 0:
            break
        else:
            print("Age must be greater than 0.")
    except ValueError:
        print("Invalid Input, Please type a number (e.g 25).")
##Coverage
MIN_COV = 50000
while True:
    try:
        coverage = int(input("Coverage amount: "))
        if coverage >= MIN_COV :
            break
        else:
             print("Value must be higher than $50000.")
    except ValueError:
        print("Invalid Input, Please enter a whole number")
#Health
health = input("Risk class (Preferred/Standard/Substandard): ").strip().title()
#tobacco
while True:
    smoker_input = input("Tobacco user? (Yes/No): ").strip().lower()
    if smoker_input in ["yes", "y"]:
        is_smoker = True
        break
    elif smoker_input in ["no", "n"]:
        is_smoker = False
        break
    else:
        print("Please Answer with either 'Yes' or 'No'.")

# Term Length Choice
while True:
    try:
        term_years = int(input("Policy Term Length (10,20, or 30 years): "))
        if term_years in [10, 20, 30]:
            break
        else:
            print("Please choose a standard term: 10, 20, or 30.")
    except ValueError:
        print("Please enter a valid number (10, 20, or 30).")
#Run the Calculaton
premium = calculate_premium(age, coverage, health, is_smoker, term_years)

print()
print("Customer: ", name)
print("Estimated Monthly Premium: $", premium)

##Generate the Schedule
print_policy_schedule(premium)