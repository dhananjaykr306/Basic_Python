"""
    @Author: Dhananjay Kumar
    @Date: 03-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 03-10-2024
    @Title:Python Program to check even or odd number
"""

def num_evenorodd(n):
    """ 
    Description :
        This function is used to find number is even or odd
    Parameters :
        m = user entered number
    Return :
        It returns number is even or odd
    """
    if(n%2 == 0):
        return "Even"
    else:
        return "Odd"
    
def main():
    n = int(input("Enter the  number"))
    num = num_evenorodd(n)
    print(f"Number is {num}")

if __name__ == "__main__":
    main()