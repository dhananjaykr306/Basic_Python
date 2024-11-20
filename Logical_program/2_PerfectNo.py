"""
    @Author: Dhananjay Kumar
    @Date: 20-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 20-11-2024
    @Title: Perfect Number Checker
"""

def is_perfect_number(n):
    """
    Description:
        This function checks if a given number is a perfect number.
        
    Parameters:
        n (int): The number to check if it is perfect.
        
    Returns:
        bool: True if the number is a perfect number, False otherwise.
    """
    if n <= 0:
        return False
    
    # Find the sum of proper divisors
    divisors_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:  # Check if i is a divisor
            divisors_sum += i
    
    return divisors_sum == n

def main():
    try:
        n = int(input("Enter a positive integer to check if it's a Perfect Number: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            if is_perfect_number(n):
                print(f"{n} is a Perfect Number.")
            else:
                print(f"{n} is not a Perfect Number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
