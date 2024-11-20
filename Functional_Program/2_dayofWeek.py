"""
    @Author: Dhananjay Kumar
    @Date: 03-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 03-10-2024
    @Title: Python Program to Calculate the Day of the Week for a Given Date
"""

from datetime import datetime

def calculate_day_of_week(date_string):
    """ 
    
    Description:
        This function calculates the day of the week for a given date.
    Parameters:
        date_string (str): The date in 'YYYY-MM-DD' format.
    Return:
        str: The name of the day of the week, or an error message if the format is invalid.
    
    """
    try:
        day = datetime.strptime(date_string, "%Y-%m-%d").strftime("%A")
        return day
    except ValueError:
        return "Invalid date format. Use 'YYYY-MM-DD'."

def main():
    """
    Description:
        The main function prompts the user for a date and prints the day of the week.
    """
    date_input = input("Enter a date in 'YYYY-MM-DD' format: ")
    day_of_week = calculate_day_of_week(date_input)
    print(f"The day of the week is: {day_of_week}")

if __name__ == "__main__":
    main()
