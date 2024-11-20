"""
    @Author: Dhananjay Kumar
    @Date: 04-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 04-10-2024
    @Title: Reverse Number
"""

# Reversing a number using a while loop
def reverse_number_while(n):
    """
    Description:
        This function reverses a given number using a while loop.
        
    Parameters:
        n (int): The number to reverse.
        
    Returns:
        int: The reversed number.
    """
    reverse = 0
    while n != 0:
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n //= 10  # Integer division by 10
    return reverse

# Reversing a number using recursion
def reverse_number_recursive(n, reverse=0):
    """
    Description:
        This function reverses a given number using recursion.
        
    Parameters:
        n (int): The number to reverse.
        reverse (int, optional): The current reversed number. Defaults to 0.
        
    Returns:
        int: The reversed number.
    """
    if n == 0:
        return reverse
    remainder = n % 10
    reverse = reverse * 10 + remainder
    return reverse_number_recursive(n // 10, reverse)

def main():
    try:
        n = int(input("Enter a positive integer to reverse: "))
        if n < 0:
            print("Please enter a positive integer.")
        else:
            reversed_number_while = reverse_number_while(n)
            reversed_number_recursive = reverse_number_recursive(n)

            print(f"Reversed number using while loop: {reversed_number_while}")
            print(f"Reversed number using recursion: {reversed_number_recursive}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
