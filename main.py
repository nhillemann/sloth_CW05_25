'''
Sloth Bytes Weekly Challenge - Calendar Week 05 2025

Task: Write a function that takes time t1 and time t2 and returns the number of hours passed between the two times.

Notes:
Time t1 will always be the starting time and t2, the ending time.
Return the string "no time passed" if t1 is equal to t2.
'''

# My solution:
from datetime import datetime

# Function takes user input, parse it in a time format and calc the passed time
def input_clocktime():
    # Set up time format
    time_format = "%H:%M"

    t1_input = input("Enter start time in HH:MM\n ")
    t2_input = input("Enter end time in HH:MM\n ")

    # Parsing string to datetime object /w error handling
    try:
        t1 = datetime.strptime(t1_input, time_format)
        t2 = datetime.strptime(t2_input, time_format)
    except ValueError:
        # in case of typos or non topic related inputs
        print("Please use only HH:MM format!")
        return

    # Substract start time from end time to calc hours passed
    t3 = t2 - t1

    # Outputs for different types of results
    if t3.total_seconds() == 0:
        print("No time passed.")
    elif t3.total_seconds() < 0:
        print("End time must be later than start time!")
    else:
        hours = t3.seconds // 3600
        minutes = (t3.seconds % 3600) // 60
        print(f"Time passed: {hours:02d}:{minutes:02d}")

if __name__ == '__main__':
    input_clocktime()