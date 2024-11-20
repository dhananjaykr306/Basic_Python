"""
    @Author: Dhananjay Kumar
    @Date: 03-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 03-10-2024
    @Title: Python program for Swap Two Numbers problem
"""

def swap(a,b):
    """ 
    Description :
        This function is used to swap the two numbers
    Parameters :
        m = first number
        n = second number
    Return :
        It returns swapped numbers
    """
     
    print("Before Swapping ",a,b)
    t = a
    a = b
    b = t

    '''a = a+b
        b=a-b
        a=a-b
    '''
    print("After Swapping",a,b)

def main():
    a = int(input("Enter First number :"))
    b = int(input("Enter second number :"))

    swap(a,b)

if __name__ == "__main__":
    main()