"""
@Author: Dhananjay Kumar
@Date: 03-10-2024
@Last Modified by: Dhananjay Kumar
@Last Modified time: 03-10-2024
@Title:Python Program to find quotient and remainder
"""

def find_quot(m,n):
    """ 
    Description :
        This function is used to find the Quotient and Remainder of a number
    Parameters :
        m = first number
        n = second number

    Return :
        It returns the Quotient and Reminder of a number
    """
    quot = m//n
    rem = m%n
    return quot,rem

def main():
    m = int(input("Enter the number"))
    n = int(input("Enter the number to divide"))

    quotient,reminder = find_quot(m,n)

    print(f"The Quotient of number is {quotient} and Reminder is {reminder}")

if __name__ == "__main__":
    main()