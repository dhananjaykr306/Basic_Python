"""
    @Author: Dhananjay Kumar
    @Date: 03-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 03-10-2024
    @Title: Utility Class for Temperature Conversion
"""

class Util:
    @staticmethod
    def temperatureConversion(value, scale):
        """
        Description:
            Converts temperature from Fahrenheit to Celsius or vice versa.
        
        Parameters:
            value (float): The temperature value to be converted.
            scale (str): Target scale for conversion, either "C" or "F".
        
        Return:
            float: Converted temperature value.
        """
        if scale.upper() == 'C':
            # Convert Fahrenheit to Celsius
            return round((value - 32) * 5 / 9, 2)
        elif scale.upper() == 'F':
            # Convert Celsius to Fahrenheit
            return round((value * 9 / 5) + 32, 2)
        else:
            raise ValueError("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")

def main():
    """
    Description:
        Main function to demonstrate temperature conversion.
    """
    try:
        temp = float(input("Enter the temperature value: "))
        target_scale = input("Enter the target scale (C for Celsius, F for Fahrenheit): ")
        
        converted_temp = Util.temperatureConversion(temp, target_scale)
        print(f"Converted temperature: {converted_temp}°{target_scale.upper()}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
