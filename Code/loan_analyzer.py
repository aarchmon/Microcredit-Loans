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
