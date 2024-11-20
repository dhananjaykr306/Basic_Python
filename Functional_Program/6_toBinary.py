"""
    @Author: Dhananjay Kumar
    @Date: 03-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 03-10-2024
    @Title: Utility Class for Decimal to Binary Conversion
"""

class Util:
    @staticmethod
    def toBinary(n):
        """
        Description:
            Converts a decimal number to its binary representation with padding to represent a 4-byte (32-bit) string.
        
        Parameters:
            n (int): A non-negative decimal integer to be converted to binary.
        
        Returns:
            str: The binary representation of the number padded to a 32-bit string.
        
        Raises:
            ValueError: If the input is a negative number.
        """
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        
        # Step 1: Calculate the binary representation without padding
        binary_rep = ""
        power = 31  # Start from the highest power of 2 less than or equal to the number
        
        # Decompose n into powers of 2
        for i in range(power, -1, -1):
            if n >= (2 ** i):
                binary_rep += "1"
                n -= (2 ** i)
            else:
                binary_rep += "0"
        
        # Step 2: Return the 32-bit binary string
        return binary_rep

def main():
    """
    Description:
        Main function that takes user input and converts it to binary with padding.
    """
    try:
        n = int(input("Enter a non-negative decimal number: "))
        
        # Convert the decimal number to binary with padding
        binary_value = Util.toBinary(n)
        
        # Output the result
        print(f"The 32-bit binary representation of {n} is: {binary_value}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
