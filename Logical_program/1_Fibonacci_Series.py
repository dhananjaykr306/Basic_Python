"""
    @Author: Dhananjay Kumar
    @Date: 20-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 20-11-2024
    @Title: Fibonacci Series Generator
"""

def fibonacci(n):
    """
    Description:
        This function generates the Fibonacci series up to the nth term.
        
    Parameters:
        n (int): The number of terms in the Fibonacci series to generate.
        
    Returns:
        list: A list containing the Fibonacci series up to the nth term.
    """
    fib_series = [0, 1]  # First two terms of the Fibonacci series
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])  # Add the next term as the sum of the last two terms
        return fib_series

def main():
    try:
        n = int(input("Enter the number of terms in Fibonacci series: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            result = fibonacci(n)
            print(f"The Fibonacci series with {n} terms is: {result}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
