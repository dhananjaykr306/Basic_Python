import time

"""
    @Author: Dhananjay Kumar
    @Date: 20-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 20-11-2024
    @Title: Stopwatch Program
"""

class Stopwatch:
    
    @staticmethod
    def start_stopwatch():
        """
        Description:
            This function starts the stopwatch and returns the start time.
        
        Returns:
            float: The start time in seconds.
        """
        input("Press Enter to start the stopwatch...")
        start_time = time.time()
        print("Stopwatch started!")
        return start_time

    @staticmethod
    def stop_stopwatch(start_time):
        """
        Description:
            This function stops the stopwatch, calculates the elapsed time
            since the start time, and prints the result.
        
        Parameters:
            start_time (float): The start time of the stopwatch.
        
        Returns:
            float: The elapsed time in seconds.
        """
        input("Press Enter to stop the stopwatch...")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Stopwatch stopped! Elapsed time: {elapsed_time:.2f} seconds")
        return elapsed_time


def main():
    try:
        stopwatch = Stopwatch()
        start_time = stopwatch.start_stopwatch()
        elapsed_time = stopwatch.stop_stopwatch(start_time)
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
