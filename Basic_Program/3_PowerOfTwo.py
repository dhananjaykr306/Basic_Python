"""
@Author: Dhananjay Kumar
@Date: 03-10-2024
@Last Modified by: Dhananjay Kumar
@Last Modified time: 03-10-2024
@Title:Power of 2 
"""


def find_pow(num):
    """ 
    Description :
         This function is used to find power of two
    Parameters :
        num = Entered to find the power of 2
    Return :
        It returns the number power of 2 value
    """
    if(num>=0):
        pow =  2 ** num
        return pow
    else:
        print("Please Enter Correct number")

def main():
    n = int(input("Enter the number to calculate power of two "))

    power = find_pow(n)

    print(f"Number Power of Two value {power}")

if __name__ == "__main__":
    main()