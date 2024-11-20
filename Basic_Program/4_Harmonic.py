"""
@Author: Dhananjay Kumar
@Date: 03-10-2024
@Last Modified by: Dhananjay Kumar
@Last Modified time: 03-10-2024
@Title:Python program for Hormonic series 
"""

def harmonic_series(num):
    """ 
    Description :
            This function is used to find the Nth harmonic series value
    Parameters :
        num = Entered num to find the harmonic series

    Return :
            It returns the Nth harmonic series value
    """
    sum = 0
    if(num>0):
        for i in range(1,num+1):
            sum = sum + 1/i
        return sum
    else:
        print("enter positive number")

def main():
    num = int(input("Enter the number :"))

    hormonic_value = harmonic_series(num)

    print(f"The Haromnic series Nth value is {hormonic_value}")

if __name__ == "__main__":
    main()