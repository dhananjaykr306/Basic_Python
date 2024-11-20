"""
    @Author: Dhananjay Kumar
    @Date: 04-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 04-10-2024
    @Title: Coupon Numbers Simulation
"""
import random

class CouponNumbers:
    
    @staticmethod
    def generate_random_number(n):
        """
        Description:
            This function generates a random number between 1 and n.
            
        Parameters:
            n (int): The total number of distinct coupon numbers.
        
        Returns:
            int: A random number between 1 and n.
        """
        return random.randint(1, n)
    
    @staticmethod
    def process_distinct_coupons(n):
        """
        Description:
            This function simulates the process of generating distinct coupon numbers.
            It generates random numbers until all n distinct coupon numbers are obtained.
            
        Parameters:
            n (int): The total number of distinct coupon numbers.
        
        Returns:
            int: The total number of random numbers generated to obtain all distinct coupons.
        """
        coupons_collected = set()  # To store distinct coupons
        random_count = 0
        
        while len(coupons_collected) < n:
            coupon = CouponNumbers.generate_random_number(n)
            coupons_collected.add(coupon)  # Add the coupon to the set (duplicates are ignored)
            random_count += 1
        
        return random_count


def main():
    try:
        n = int(input("Enter the number of distinct coupon numbers: "))
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            # Simulate the process to generate distinct coupons
            random_count = CouponNumbers.process_distinct_coupons(n)
            print(f"Total random numbers needed to obtain {n} distinct coupons: {random_count}")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()