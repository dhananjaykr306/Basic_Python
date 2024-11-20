"""
    @Author: Dhananjay Kumar
    @Date: 03-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 03-10-2024
    @Title:Python Program to check vowel and consonant
"""    

def alp_voworcons(ch):
    """ 
    Description :
        This function is used to find character is vowel or consoennt
    Parameters :
        m = user entered character
    Return :
        It returns each character is vowel or consonent
    """

    if(ch=='a' or ch=='e' or ch == 'i' or ch == 'o' or ch == 'u'):
            return "vowel"
    else:
            return "Consonent"
    
def main():
    
    char = input("Enter the String :")

    alpha = alp_voworcons(char)

    print(f"The Entered character {char} is {alpha} ")

if __name__ == "__main__":
      main()