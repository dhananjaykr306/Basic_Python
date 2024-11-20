"""
    @Author: Dhananjay Kumar
    @Date: 03-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 03-10-2024
    @Title: Utility Class for Loan Monthly Payment Calculation
"""

import sys

class Util:
    @staticmethod
    def monthlyPayment(P, Y, R):
        """
        Description:
            Calculates the monthly payment required to pay off a loan based on the principal,
            annual interest rate, and loan duration in years.
        
        Parameters:
            P (float): The principal loan amount.
            Y (int): The loan term in years.
            R (float): The annual interest rate in percentage.
        
        Returns:
            float: The monthly payment amount.
        """
        # Convert annual interest rate to monthly interest rate (decimal form)
        r = (R / 100) / 12
        # Number of months
        n = Y * 12
        
        # Calculate the monthly payment using the formula
        if r != 0:
            M = (P * r * (1 + r)**n) / ((1 + r)**n - 1)
        else:
            M = P / n  # If no interest, just divide the principal by the number of months
        
        return round(M, 2)

def main():
    """
    Description:
        Main function that reads command-line arguments and calculates the monthly loan payment.
    """
    try:
        # Ensure correct number of arguments
        if len(sys.argv) != 4:
            raise ValueError("Please provide exactly 3 arguments: Principal, Years, and Rate")

        # Read command-line arguments
        P = float(sys.argv[1])  # Principal loan amount
        Y = int(sys.argv[2])     # Loan duration in years
        R = float(sys.argv[3])   # Annual interest rate in percentage
        
        # Calculate the monthly payment
        monthly_payment = Util.monthlyPayment(P, Y, R)
        
        # Output the result
        print(f"The monthly payment for the loan is: ${monthly_payment}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()