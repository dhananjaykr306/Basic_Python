"""
    @Author: Dhananjay Kumar
    @Date: 4-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 04-10-2024
    @Title: Prime Number Checker
"""

def is_prime_number(n):
    """
    Description:
        This function checks if a given number is a prime number.
        
    Parameters:
        n (int): The number to check if it is prime.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False 
    if n == 2:
        return True   
    if n % 2 == 0:
        return False 
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False  
    return True 

def main():
    try:
        n = int(input("Enter a positive integer to check if it's a Prime Number: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            if is_prime_number(n):
                print(f"{n} is a Prime Number.")
            else:
                print(f"{n} is not a Prime Number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
