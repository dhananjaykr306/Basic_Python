"""
@Author: Dhananjay Kumar
@Date: 03-10-2024
@Last Modified by: Dhananjay Kumar
@Last Modified time: 03-10-2024
@Title: Python program for coin flipcoin
"""

import random

def filp_coin(num):

    """ 
    Description :
        This function is used to find the Head and Tail percentage
    Parameters :
        num = The Number of times coin to be flip
    Return :
        It returns the fewest number of notes for change
    """
    
    head = 0
    tail = 0
    for i in range(1,num+1):
        val = random.randint(0,1)
        if(val == 0):
            tail += 1
        else:
            head += 1
    head_per = (head/num)*100
    tail_per = (tail/num)*100
    return head_per,tail_per

def main():
    num = int(input("Enter Number of times to flip a coin :"))

    head_per,tail_per = filp_coin(num)

    print("Head Percentage :",head_per)
    print("Tail percentage ",tail_per)

if __name__ == "__main__":
    main()