"""
    @Author: Dhananjay Kumar
    @Date: 03-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 03-10-2024
    @Title: Utility Class for Square Root Calculation Using Newton's Method
"""

class Util:
    @staticmethod
    def sqrt(c):
        """
        Description:
            Computes the square root of a non-negative number using Newton's method (also known as Heron's method).
        
        Parameters:
            c (float): A non-negative number for which the square root needs to be calculated.
        
        Returns:
            float: The square root of the number c.
        
        Raises:
            ValueError: If the input number is negative.
        """
        if c < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        
        # Set initial guess
        t = c
        epsilon = 1e-15  # Desired accuracy
        
        # Newton's method iteration until desired accuracy is achieved
        while abs(t - c / t) > epsilon * t:
            t = (c / t + t) / 2
        
        return round(t, 15)  # Round the result to 15 decimal places for accuracy

def main():
    """
    Description:
        Main function that takes input from the user and computes the square root of the given number.
    """
    try:
        c = float(input("Enter a non-negative number to find its square root: "))
        
        # Calculate the square root using Newton's method
        result = Util.sqrt(c)
        
        # Output the result
        print(f"The square root of {c} is approximately: {result}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
