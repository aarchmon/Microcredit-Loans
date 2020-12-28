# Importation of required libraries. 
import csv
from pathlib import Path

# Program header.
print("\nLoan Analyzer Program\n")

""" 
Part 1: Automate the Calculations

In this first section, we will automate calculations for specific 
loan portfolio summaries. To be more precise, we will perform
the following tasks:

1. Determine amount of loans in the list.
2. Calculate the total of all loans in the list.
3. Calculate the average loan price in the portfolio.
4. Print out all results from tasks 1-3. 
"""

# Header for Part 1.
print("\n============================================")
print("Part 1: Automate the Calculations")
print("--------------------------------------------\n")

# Variables for desired calculations.
num_loans_in_list = None
total_of_loans = None
average_loan = None

# Loan list.
loan_costs = [500, 600, 200, 1000, 450]

# Determine amount of loans in the list. 
num_loans_in_list = len(loan_costs)

# Calculate the total of all loans in the list.
total_of_loans = sum(loan_costs)

# Calculate the average loan price in the portfolio.
average_loan = float(total_of_loans / num_loans_in_list)

# Print out all results from tasks 1-3. 
print(f"Number of loans in list: {num_loans_in_list}")
print(f"Total of loans: ${total_of_loans}")
print(f"Average loan value: ${average_loan: .2f}")

"""
Part 2: Analyze Loan Data

In this section, we will analyze a loan to evaluate its investment. To be
specific, we will carry out the following tasks:

1. Retrieve the loan's future value.
2. Retrieve the loan's remaining months.
3. Print out the loan's future value and remaining months.
4. Using the Present Value formula, calculate the fair value of this loan (20% minimum required return).
5. Print out calculated fair value of loan.
6. Determine if the loan's present value is representative of its fair value.

"""

# Header for Part 2.
print("\n============================================")
print("Part 2: Analyze Loan Data")
print("--------------------------------------------\n")

# Variables for future vale, remaining months, and fair value.
future_value = None
remaining_months = None
fair_value = None

# Loan data.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Retrieve the loan's future value.
future_value = loan.get("future_value")

# Retrieve the loan's remaining months.
remaining_months = loan.get("remaining_months")

# Print out the loan's future value and remaining months.
print(f"Future value: ${future_value}")
print(f"Remaining months on loan: {remaining_months}")

# Using the Present Value formula, calculate the fair value of this loan (20% minimum required return).
discount_rate = 0.2
fair_value = future_value / (1 + discount_rate / 12) ** remaining_months

# Print out calculated fair value of loan.
print(f"Fair value of loan: ${fair_value: .2f}")

# Determine if the loan's present value is representative of its fair value.
def loan_worth(present_val, loan_cost):
    if present_val >= loan_cost:
        print("Loan is worth the cost to purchase. ")
    else:
        print("Loan is too expensive. ")

loan_worth(fair_value, loan.get("loan_price"))

"""
Part 3: Perform Financial Calculations.

For this section, we will perform financial calculations through the utilization of
Python functions on a new loan. We will accomplish the following tasks:

1. Define a new function that will be used to calculate present value.
2. Use this new function to calculate the present value of a new loan 
   with an annual discount rate of 20%. 
3. Print out the present value of this new loan.

"""

# Header for Part 3.
print("\n============================================")
print("Part 3: Perform Financial Calculations")
print("--------------------------------------------\n")

# New loan data.
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
    return present_value

# Use this new function to calculate the present value of a new loan 
#   with an annual discount rate of 20%. 
future_value = new_loan.get("future_value")
remaining_months = new_loan.get("remaining_months")
annual_discount_rate = 0.2
present_value = calculate_present_value(future_value, remaining_months, annual_discount_rate)

# Print out the present value of this new loan.
print(f"The present value of the loan is: ${present_value: .2f}")
